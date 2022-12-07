from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('property-grid/', property_grid, name='property_grid'),
    path('blog-grid/', blog_grid, name='blog_grid'),
    path('pages/property-single', property_single, name='property_single'),
    path('pages/blog-single', blog_single, name='blog_single'),
    path('pages/agents-grid', agents_grid, name='agents_grid'),
    path('pages/agent-single', agent_single, name='agent_single'),
    path('contact/', contact, name='contact'),
]
