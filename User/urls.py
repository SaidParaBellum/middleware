from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from User.views import UserLoginView, RegisterView

urlpatterns = [
    path('login/', UserLoginView.as_view(),name='login'),
    path('sign/', RegisterView.as_view(),name='sign'),

]  +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
