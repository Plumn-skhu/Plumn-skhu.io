from django.urls import path
from posts import views 
from accounts import views as account_views
urlpatterns=[
    path('base/', views.base, name='base'),
    path('notice/', views.notice, name='notice'),
    path('feedback/', views.feedback, name='feedback'), #피드백
    path('readreport/<int:id>', views.readreport, name='readreport'), # 이의제기
    path('create/', views.create, name='create'),
    path('list/', views.list, name='list'),
    path('read/<int:id>', views.read, name='read'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('scrap/', views.scrap, name='scrap'),
    path('like/', views.like, name='like'),
    path('donate/', views.donate, name='donate'),
    path('pay/', views.pay, name='pay')
]