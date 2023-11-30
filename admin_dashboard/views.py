from django.shortcuts import render
from django.http import HttpResponse

# CREATE VIEWS
# if function param is unused, use '_', else use 'request'
def index(_):
    return HttpResponse('Welcome to the Index Page')

def staff(_):
    return HttpResponse('This is the Staff Page')
