from django.conf.urls import url


from chat_app import views


urlpatterns = [
    #Django Views
    url(r'^chats/$', views.ChatIndex.as_view(), name="index"),
    ]
