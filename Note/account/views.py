from django.http import HttpResponse
from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from account.forms import Amount_user , Debit_form , Debose_form
from account.models import AmountUser , Debose , Debit

"""
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated '\
                                        'successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

"""



@login_required
def bank(request):
    if request.method == 'POST':
        form = Amount_user(request.POST)
        amount_new  =request.POST.get('amount')
        if form.is_valid():
            #cd = form.cleaned_data
            user =  request.user
            b = AmountUser(amount=amount_new,user=user)
            b.save()
    else:
        form = Amount_user()
    return render(request,
                  'account/bank.html',
                  {'section': 'bank' , 'form':form})



def debose_view(request):
    if request.method == 'POST':
        form = Debose_form(request.POST)
        debose_new  =request.POST.get('debose')
        if form.is_valid():
            b = Debose(debose=debose_new)
            b.save()
        after_debose = Debose.amount + Debose.debose    
    else:
        form = Debose_form()
    return render(request,
                  'account/debose.html',
                  {'after_debose': after_debose , 'form':form})





def debit_view(request):
    if request.method == 'POST':
        form = Debit_form(request.POST)
        debit_new  =request.POST.get('debit')
        if form.is_valid():
            user =  request.user
            b = Debit(debit=debit_new)
            b.save()
    else:
        form = Debit_form()
    return render(request,
                  'account/debit.html',
                  {'section': 'bank' , 'form':form})




                