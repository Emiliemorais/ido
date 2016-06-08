from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^budget/$', views.BudgetView.as_view(), name='solicit_budget'),
    url(r'^contacts/$', views.MessageView.as_view(), name='contacts'),

]