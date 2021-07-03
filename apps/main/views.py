from django.shortcuts import render
import datetime


def home(request):
  today = datetime.date.today()
  # today = datetime.datetime.now()
  return render(request, 'main/home.html', context={'today':today})

def home_files(request, filename):
    return render(request, filename, {}, content_type="text/plain")
