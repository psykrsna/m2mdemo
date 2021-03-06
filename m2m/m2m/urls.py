"""m2m URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from demo.models import Software, Programmer
from rest_framework import routers, serializers, viewsets


class ProgrammerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programmer
        fields = ('username',)


class SoftwareSerializer(serializers.ModelSerializer):
    programmers = serializers.PrimaryKeyRelatedField(many=True, queryset=Programmer.objects.all())
    class Meta:
        model = Software
        fields = ('id', 'name', 'version', 'programmers',)


class SoftwareViewSet(viewsets.ModelViewSet):
    queryset = Software.objects.all()
    serializer_class = SoftwareSerializer


class ProgrammerViewSet(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer


router = routers.DefaultRouter()
router.register(r'software', SoftwareViewSet)
router.register(r'programmer', ProgrammerViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]

'''
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
]
'''
