from django.shortcuts import render
from django.views.generic.list import ListView
from myVideoApp.models import Membership
# Create your views here.

def index(request):
    context = {}
    return render(request, 'index.html', context)

class MembershipSelectView(ListView):
    models = Membership
