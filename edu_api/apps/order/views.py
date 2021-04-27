from django_redis import get_redis_connection
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView

from order.models import Order, OrderDetail
from order.serializers import OrderModelSerializer,  Order2ModelSerializer


class OrderAPIView(CreateAPIView):
    queryset = Order.objects.filter(is_show=True, is_delete=False)
    serializer_class = OrderModelSerializer


class OrderListAPIView(ListAPIView):

    queryset = Order.objects.filter(is_show=True, is_delete=False)
    serializer_class = Order2ModelSerializer


class OrderSiteAPIView(APIView):

    def get(self, request):
        order_number = request.query_params.get("order_number")
        connection = get_redis_connection("order_site")
        site = connection.get(f"site_{order_number}")
        if not site:
            return Response({"message": "订单已过期或不存在"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"site": site})
