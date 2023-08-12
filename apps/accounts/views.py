from django.shortcuts import render

# Create your views here.
def AccountsView(request):
    return render(request, 'accounts.html')