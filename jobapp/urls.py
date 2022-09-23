from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListCreateApplicationView.as_view()),
    path('<int:pk>/', views.RetrieveUpdateDestroyApplicationView.as_view()),
    path('<int:pk>/status/', views.PartialUpdateStatusApplicationView.as_view())
]
