from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Booking, Menu

from .serializers import BookingSerializer, MenuSerializer

# Create your views here.


def index(request):
  return render(request, 'index.html', {})


class MenuItemView(ListCreateAPIView):
  queryset = Menu.objects.all()
  serializer_class = MenuSerializer


class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
  queryset = Menu.objects.all()
  serializer_class = MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
  permission_classes = [IsAuthenticated]
  queryset = Booking.objects.all()
  serializer_class = BookingSerializer
