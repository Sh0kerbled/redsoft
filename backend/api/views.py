from django.conf import settings
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from . import paypal as paypal_client
from .models import Subscription
from .serializers import SubscriptionSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_subscription(request):
    PLAN_IDS = {
        "pro": settings.PAYPAL_PRO_PLAN_ID,
        "ultimate": settings.PAYPAL_ULTIMATE_PLAN_ID,
    }

    plan = request.data.get('plan')
    if plan not in PLAN_IDS:
        return Response({'error': 'Invalid plan'}, status=400)

    try:
        sub = paypal_client.create_subscription(
            plan_id=PLAN_IDS[plan],
            user_email=request.user.email,
            return_url=f"{settings.FRONTEND_URL}/payment/success?plan={plan}",
            cancel_url=f"{settings.FRONTEND_URL}/payment/cancel",
        )

        approval_url = next(
            (l['href'] for l in sub['links'] if l['rel'] == 'approve'), None
        )

        return Response({
            'subscription_id': sub['id'],
            'approval_url': approval_url,
        })
    except Exception as e:
        return Response({'error': str(e)}, status=500)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def activate_subscription(request):
    subscription_id = request.data.get('subscription_id')
    plan = request.data.get('plan')

    try:
        sub_data = paypal_client.get_subscription(subscription_id)

        if sub_data['status'] != 'ACTIVE':
            return Response({'error': 'Subscription not active'}, status=400)

        Subscription.objects.update_or_create(
            user=request.user,
            defaults={
                'plan': plan,
                'paypal_subscription_id': subscription_id,
                'status': 'active',
            }
        )

        return Response({'success': True, 'plan': plan})
    except Exception as e:
        return Response({'error': str(e)}, status=500)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def cancel_subscription(request):
    try:
        sub = Subscription.objects.get(user=request.user, status='active')
        paypal_client.cancel_subscription(sub.paypal_subscription_id)
        sub.status = 'cancelled'
        sub.save()
        return Response({'success': True})
    except Subscription.DoesNotExist:
        return Response({'error': 'No active subscription'}, status=404)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_subscription(request):
    try:
        sub = Subscription.objects.get(user=request.user, status='active')
        return Response({'plan': sub.plan, 'status': sub.status})
    except Subscription.DoesNotExist:
        return Response({'plan': 'basic', 'status': 'free'})


@api_view(['POST'])
@permission_classes([AllowAny])
def paypal_webhook(request):
    event_type = request.data.get('event_type')
    resource = request.data.get('resource', {})

    if event_type == 'BILLING.SUBSCRIPTION.CANCELLED':
        sub_id = resource.get('id')
        Subscription.objects.filter(
            paypal_subscription_id=sub_id
        ).update(status='cancelled')

    return Response({'status': 'ok'})