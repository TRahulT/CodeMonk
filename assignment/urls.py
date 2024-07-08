from django.urls import path
from .views import upload_paragraphs,search_word,CustomUserLoginView,custom_user_create

urlpatterns = [
    path('customuser_add/', custom_user_create, name="customuser-add"),
    path('customuser-login/', CustomUserLoginView.as_view(), name='customuser-login'),
    path('upload/', upload_paragraphs, name='upload_paragraphs'),
    path('search/<str:word>/', search_word, name='search_word'),
]
