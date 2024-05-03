from django.shortcuts import render

def chat(request):
    return render(request, "index.html")

def room(request, room_name):
    return render(request, "room.html", context={"room_name": room_name})