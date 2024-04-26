from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    res=HttpResponse("""<html><body bgcolor=yellow><center>
    <h1>welcome to lokesh it </h1></center></body></html>""")
    return res
