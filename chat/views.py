from django.shortcuts import render, redirect
from .models import Message
from home.forms import ChatForm


def index(request):
    if request.method == "POST":
        form = ChatForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('user').username
            return redirect(f'{user}/')
    else:
        form = ChatForm()
    return render(request, 'chat/index.html', {'form': form})


def room(request, room_name):
    msgs = Message.objects.filter(room_name=room_name)
    return render(request, 'chat/room.html', {'room_name': room_name, 'msgs': msgs})
