from django.urls import path
from .views import HomePage

app_name='calculator'

urlpatterns = [
    path('', HomePage.as_view(), name="homepage"),
]