from django.shortcuts import render

# Create your views here.
def pending(request):
    return render(request, 'pending.html')