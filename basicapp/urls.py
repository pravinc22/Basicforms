from django.urls import path
from basicapp import views

urlpatterns=[
    path('',views.signup_view,name='signup')
]
