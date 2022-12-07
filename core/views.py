from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def agent_single(request):
    return render(request, 'agent-single.html')

def agents_grid(request):
    return render(request, 'agents-grid.html')

def blog_single(request):
    return render(request, 'blog-single.html')

def blog_grid(request):
    return render(request, 'blog-grid.html')

def contact(request):
    return render(request, 'contact.html')

def property_single(request):
    return render(request, 'property-single.html')

def property_grid(request):
    return render(request, 'property-grid.html')
