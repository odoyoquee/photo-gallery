from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

# urlpatterns=[
#     url('^$',views.home,name = 'home'),
#     # url('^$',views.navi,name = 'welcome'),
#     # url('^$',views.camera,name='photo/camera')
# ]

urlpatterns=[
    url('^$',views.photo,name='photo'),
    url(r"^search/", views.search, name="search_results"),
    url(r"^browse/$", views.browse, name="browse"),
    url(r"^location/(\d+)", views.location_filter, name="location"),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
