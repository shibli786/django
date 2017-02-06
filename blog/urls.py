from django.conf.urls import url 
from . import views


app_name='blog'
urlpatterns=[
url(r'^$',views.post_list,name='post_list'),
url(r'^tag/(?P<tag>[-\w]+)/$',views.post_list,name='post_list_by_tag')
,
url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
	views.post_detail,
	name='post_detail'),
url(r'^(?P<post_id>\d+)/share/',views.share_post,name='share_post')
]
