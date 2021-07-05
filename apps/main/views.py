from django.shortcuts import render
import datetime


def home(request):
  today = datetime.date.today()
  now = datetime.datetime.now()
  return render(request, 'main/home.html', context={'today':today,'now': now})

def home_files(request, filename):
    return render(request, filename, {}, content_type="text/plain")

def error_403(request, exception):
  data = {}
  return render(request, '403_csrf.html', data)

def error_404(request, exception):
  data = {}
  return render(request, '404.html', data)


def error_500(request):
  data = {}
  return render(request, '500.html', data)
