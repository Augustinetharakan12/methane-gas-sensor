# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse
from .scripts import serial_ports, get_values
from time import sleep
import serial

def fun(request):
    return render(request,"sensor/sen.html",{ 'serial_ports' : serial_ports() })
