from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token
from rest_framework.generics import RetrieveAPIView
from rest_framework import permissions

from .forms import UserForm, UserLoginForm
from .serializers import UserSerializer

from braces.views import LoginRequiredMixin


class UserFormView(View):
    form_class = UserForm
    template_name = 'accounts/registrations_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name , {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    token, created = Token.objects.get_or_create(user=user)
                    request.session['auth'] = token.key
                    login(request,user)
                    return redirect('accounts:chat_app')

        return render(request, self.template_name, {'form': form})


class LoginView(View):
    form_class = UserLoginForm
    template_name = 'accounts/login_form.html'

    def get(self, request):
        # if request.user.is_authenticated():
        #     return redirect('accounts:chat_app')
        form = self.form_class(None)
        return render(request, self.template_name , {'form': form})

    def post(self, request):
        form = self.form_class(None)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                token, created = Token.objects.get_or_create(user=user)
                request.session['auth'] = token.key
                login(request, user)
                return redirect('accounts:app')
            else:
                return HttpResponse("Inactive User")

        return render(request, self.template_name, {'form': form, 'Message': "User is not exist, Please register!"})



class LogoutView(View):
    def get(self, request):
        request.user.auth_token.delete()
        logout(request)
        return redirect('accounts:login')



class UserProfile(RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()

    def get_object(self):
        return self.request.user


class AppRedirect(View):
    template_name = 'accounts/app.html'

    def get(self, request):
        return render(request, self.template_name)


