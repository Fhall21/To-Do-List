
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.views.generic import TemplateView

from django.conf import settings
from To_do.views import ToDoListView, ToDoDetailedView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='to_do/index.html')),
    path('todo/api/', ToDoListView.as_view()),
    re_path(r'^todo/api/(?P<pk>[0-9]+)/', ToDoDetailedView.as_view()),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
