from django.shortcuts import redirect, render
from rest_framework.generics import ListAPIView,CreateAPIView

from django.views import View
from django.conf import settings

from .models import link
from .serializer import linkSerializer

class ShortenerListAPIView(ListAPIView):
    queryset=link.objects.all()
    serializer_class=linkSerializer

class ShortenerCreateApiView(CreateAPIView):
    serializer_class=linkSerializer


class Redirector(View):
    def get(self,request,shortener_link,*args, **kwargs):
        shortener_link=settings.HOST_URL+'/'+self.kwargs['shortener_link']
        redirect_link=link.objects.filter(shortened_link=shortener_link).first().original_link
        return redirect(redirect_link)