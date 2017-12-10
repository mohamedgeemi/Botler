from django.conf.urls import url

from accounts import views

urlpatterns = [
    url(r'^$', views.LoginView.as_view(), name="login"),
    url(r'^logout/$', views.LogoutView.as_view(), name="logout-user"),
    url(r'^register/$', views.UserFormView.as_view(), name="register"),
    url(r'^me/$', views.UserProfile.as_view(), name="user-profile"),
    url(r'^todo/$', views.AppRedirect.as_view(), name="chat_app"),
]