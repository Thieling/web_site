from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages


def view_bienvenidos(request):
    return render(request, "TecHard/base.html")