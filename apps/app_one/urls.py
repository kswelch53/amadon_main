#app-level url code:
from django.conf.urls import url, include
from . import views

urlpatterns = [
    # url(r'^$', views.index),
    url(r'^$', views.index3, name="index"),
    url(r'^process_order$', views.process_order, name="process_order"),
    url(r'^checkout$', views.checkout, name="checkout"),
    url(r'^clear$', views.clear, name="clear"),

]
