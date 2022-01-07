from django.urls import path
from myVideoApp.views import *
app_name = 'myVideoApp'

urlpatterns = [
    path('', MembershipSelectView.as_view(), name='select'),
]
