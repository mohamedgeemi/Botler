# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Message


class ChatIndex(APIview):

    def get(self, request, *args, **kwargs):

        chat_queryset = Message.objects.order_by("-created")[:10]
        chat_message_count = len(chat_queryset)

        chat_messages = reversed(chat_queryset)
        
        return render(request, "chat_app/chatroom.html", {
            'chat_messages': chat_messages,
            'chat_message_cout': chat_message_count
        })
