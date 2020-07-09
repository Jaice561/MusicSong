from django.urls import path
from .views import MyPreferenceFormView

app_name = 'preferences'

urlpatterns = [
    path('', MyPreferenceFormView.as_view(), name='my-preference-add-view')
]