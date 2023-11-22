from django.urls import path

from core.views import index,test1,test2,test3

urlpatterns = [
    path('',index,name='index'),
    path('test1',test1,name='test1'),
    path('test2',test2,name='test2'),
    path('test3',test3,name='test3')
]