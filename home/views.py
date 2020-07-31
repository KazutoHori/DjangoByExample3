from django.shortcuts import render

# Create your views here.

def show_chart(request):
    return render(request, 'home_base.html')
