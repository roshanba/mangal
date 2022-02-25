from django.conf.urls import url
from django.urls import path
from django.conf.urls.i18n import i18n_patterns
from jembe import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^reservation/$', views.NewReservation.as_view(), name="reservation"),
    url(r'^contact/$', views.Contact.as_view(), name="contact"),
    url(r'^payments/$', views.payment, name="payment"),
    path('changeLanguage/<lang_code>/', views.changeLanguage, name='changeLanguage')
]