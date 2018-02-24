from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, response
from .models import Stock
from .serializers import StockSerializer
from django.template.context_processors import request

# List all the companies stocks
# stocks/
class StockList(APIView):
    
    def get(self, request):
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks, many=True)
        return Response(serializer.data) 
    
    def post(self, request):
        stockSerializer = StockSerializer(data=request.data)
        if (stockSerializer.is_valid()):
            stockSerializer.save()
            return Response(stockSerializer.data, status=status.HTTP_201_CREATED)
        return Response(stockSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class StockDetails(APIView):
    
    def get(self,request,pk):
        try:
            stock = Stock.objects.get(pk=pk)
        except Stock.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = StockSerializer(stock, many=False)
        return Response(serializer.data)
    
    def post(self):
        pass