from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from myVideoApp.models import *
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
import stripe


def index(request):
    context = {}
    return render(request, 'index.html', context)

def membership(request):
    object = Membership.objects.all() #selected membership
    current_membership = UserMembership.objects.filter(user = request.user).first() #user membership
    # to display the current membership using current_membership.membership
    subscription_qs = Subscription.objects.filter(user_membership=current_membership).first() #user_subscription
    
    # print(subscription_qs)
    user_membership=current_membership.membership



    selected_membership_type = request.POST.get('membership_type')

    selected_membership_qs=Membership.objects.filter(membership_type=selected_membership_type)
    # if selected_membership_qs.exists():
    selected_membership = selected_membership_qs.first()
    print(selected_membership)
    '''
    ==========================
            VALIDATION
    ==========================
    '''
    if current_membership.membership == selected_membership:
        if subscription_qs != None:
            messages.info(request, "You already have this membership. Your \
                next payment is due {}".format("get this value from stripe"))
            return HttpResponseRedirect(request.META.get('HTTP-REFERER'))

    #assign to the session
    request.session['selected_membership_type']=selected_membership.membership_type
    # return HttpResponseRedirect(reverse('payment'))

    context = {
        'object':object,
        'current_membership':str(current_membership.membership),
    }
    return render(request, 'membership_list.html', context)

# def Payment(request):
#     current_membership = UserMembership.objects.filter(user = request.user).first() #user membership
#     membership_type=request.session['selected_membership_type']
#     selected_membership_qs=Membership.objects.filter(membership_type=membership_type)
    # if selected_membership_qs.exists():
    #     return selected_membership_qs.first()
    # publishKey = settings.STRIPE_PUBLISHABLE_KEY
    # return render(request, 'membership_payment.html')

