from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('task/', views.index,name='indexx'),
    # path('', include('Management.urls'))

]