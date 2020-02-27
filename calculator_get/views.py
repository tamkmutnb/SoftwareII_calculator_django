from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail
import numbers
import decimal


def home(request):
    return render(request, 'home.html')

def calculate(request):
    x = request.POST['num1']
    y = request.POST['num2']
    op = request.POST['operator']

    if x.isnumeric() and y.isnumeric() and op in ('+', '-', '*', '/'):
        int_x = int(x)
        int_y = int(y)
        if op == ('+'):
            result = (int_x + int_y)
        if op == ('-'):
            result = (int_x - int_y)
        if op == ('*'):
            result = (int_x * int_y)
        if op == ('/'):
            result = (int_x / int_y)
    else:
        result = ('Input Error')
    return render(request, 'home.html', {'result': result})
