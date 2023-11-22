from django.shortcuts import render

# Create your views here.

def index (requests):
    return render(requests,'index.html')
def test1 (requests):
    return render(requests,'test1.html')
def test2 (requests):
    return render(requests,'test2.html')
def test3 (requests):
    return render(requests,'test3.html')