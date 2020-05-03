from django.conf.urls import url

from adoptions import views


urlpatterns = [
    url(r'^$', views.home, name='pet_home'),
    url(r'^adoptions/(\d+)/', views.pet_detail, name='pet_detail'),
]
