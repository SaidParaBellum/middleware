import datetime
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from django.shortcuts import render

# Create your views here.

def index(request):
    name = 'Saidkamol hello my friend'
    num_list = [1,2,3,4,5]
    dt = datetime.datetime.now()
    return render(request,
                  'index.html',
                  {'name': name,
                        'num_list': num_list,
                        'dt': dt})


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('protected')
        return render(request, 'login.html', {'error': 'Неправильное имя пользователя или пароль.'})

class ProtectedView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'protected.html')
        return redirect('login')

class AdminPageView(View):
    def get(self, request):
        if request.user.is_authenticated and request.user.is_superuser:
            return render(request, 'admin_page.html')
        return redirect('login')

class ErrorView(View):
    def get(self, request):
        return render(request, 'error_page.html')
