from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('accounts.urls', namespace="accounts")),
    url(r'chat/^', include('chat_app.urls', namespace="chat_app")),
    url(r'^admin/', admin.site.urls),
]