from django.urls import path
from contact_form import views

urlpatterns = [
    path('contact_form/', views.ContactList.as_view()),
    path('contact_form/<int:pk>/', views.ContactDetail.as_view())
]
