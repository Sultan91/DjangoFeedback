from django.conf.urls import url
from . import views

urlpatterns = [
    # feedback/90/
    url(r'^(?P<feedback_id>[0-9]+)/$', views.detail, name='details of feedback'),
    url(r'^$', views.index, name='all feedbacks'),
    url(r'^feedback_create/$', views.feedback_create_view, name='create feedback form')

]