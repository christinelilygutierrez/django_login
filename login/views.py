from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Welcome Page
def index(request):
    try:
        # Method 1
        #template = loader.get_template('login/index.html')
        #context = {'message' : "We are glad that you have arrived safely"}
        #return HttpResponse(template.render(context, request))
        # Method 2
        #context = {'message' : "We are glad that you have arrived safely"}
        # Method 3: Do not use try, except
        #value = get_object_or_404(DBTableName, pk=PUBLICKEY)
        #return render(request, 'login/index.html', context)
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login:account'))
    except:
        raise Http404("An error occurred")
    return render(request, 'login/signin.html')

# Login Page
def signin(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login:account'))
    else:
        return render(request, 'login/signin.html')

# Validate login
def loginValidate(request):
    try:
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('login:account'))
        else:
            raise Exception('Incorrect username and password combination')
    except Exception as badPassword:
        return render(request, 'login/signin.html', {'error_message': badPassword[0],})
    except:
        return render(request, 'login/signin.html', {'error_message': "Error occurred with submission",})

# Logout
def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login:index'))

# Account Page
@login_required
def account(request):
    return render(request, 'login/account.html')
