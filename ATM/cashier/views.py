import datetime
from .models import Transaction
from django.utils import timezone
from .cashier_functions import Cashier
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required


def home(request):
    template = 'cashier/home.html'
    context = {'title': 'Home'}

    return render(request, template_name=template, context=context)

def result(request):
    template = 'cashier/result.html'
    msj = ""
    cashier = Cashier()
    if(request.method == 'POST'):
        money = request.POST['money']
        transaction_info = cashier.transact(money)
        # Saves the transaction in the database
        if(money):
            new_trancation = Transaction(amount=money, result=transaction_info[5], transaction_date=timezone.now())
            new_trancation.save()

    return render(request, template_name=template, context={"transaction_information": (transaction_info)})

@login_required
def transactions(request):
    template = 'cashier/transactions.html'
    transactions = Transaction.objects.all()
    return render(request, template_name=template,context={"transactions_list": transactions})
