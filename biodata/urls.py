
from django.conf.urls import url

from . import views
from .views import displayuser, displayuserdet


urlpatterns = [
    url(r'home',displayuser.as_view()),
    url(r'^user/(?P<slug>\w+)/$',views.displayuserdet.as_view(),name='candidate'),
    url(r'apply',views.applyuser,name='apply')

]