from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import UserInput

def home(request):
    log = UserInput.objects.all()
    return render(request, 'home.html', {'log': log })

def calculate(request):
    x = request.POST['num1']
    y = request.POST['num2']
    op = request.POST['operator']
    log = UserInput.objects.all()

    '''if request.POST['add']:
        result = int_x + int_y'''

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
        UserInput.objects.create(user_x = x, user_y = y, user_operator = op, result = result)


    else:
        result = ('Input Error')
    return render(request, 'home.html', {'result': result, 'log': log })


def delete(request, id):
    UserInput.objects.get(id=id).delete()
    log = UserInput.objects.all()
    return render(request, 'home.html', {'log': log })




def home_page(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        # form = CalculationForm(request.POST)
        # check whether it's valid:
        # if form.is_valid():

        operator = (request.POST["operator"])
        x = (request.POST["x"])
        y = (request.POST["y"])
        print("this is x:", x)

        if operator == "+":
            result = (x + y)
        if operator == "-":
            result = (x - y)
        if operator == "*":
            result = (x * y)
        if operator == "/":
            result = (x / y)
        # subject = form.cleaned_data['subject']
        # message = form.cleaned_data['message']
        # sender = form.cleaned_data['sender']
        # cc_myself = form.cleaned_data['cc_myself']
        # recipients = ['info@example.com']
        # if cc_myself:
        #    recipients.append(sender)
        # return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    # else:
    #    form = CalculationForm()

    return render(request, 'home.html')
    # return render(request, 'home.html', {'form': form})


'''
Example

def home_page(request):
    x = []
    for i in range(10):
        x.append(i)
    return HttpResponse("<h1>DataFlair Django Tutorials<//input/h1>The Digits are {0}".format(x))
'''