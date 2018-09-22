# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect,HttpResponse
from .models import *
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'first/index.html')

def create(request):
    if request.method == "POST":
        error= User.object.creating_db(request.POST)
        if len(error)>0:
            for error in error:
                messages.error(request, error)
            return redirect("new:index")
        else:
            return redirect("new:index")
def login(request):
    print "login"
    return redirect('/')
