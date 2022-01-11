from django.shortcuts import render
from django.views.generic.list import ListView
from myVideoApp.models import *

def index(request):
    context = {}
    return render(request, 'index.html', context)

def membership(request):
    object = Membership.objects.all()
    current_membership = UserMembership.objects.filter(user = request.user).first()
    # print(current_membership.membership)

    context = {
        'object':object,
        'current_membership':str(current_membership.membership),
    }
    return render(request, 'membership_list.html', context)

