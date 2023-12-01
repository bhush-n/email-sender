
from django.urls import path
from .views import send_email, view_emails, index, delete_email

urlpatterns = [
    path('', index, name='index'),
    path('send_email/', send_email, name='send_email'),
    path('view_emails/', view_emails, name='view_emails'),
    path('delete_email/', delete_email, name='delete_email'),
]
