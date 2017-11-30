from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import login, logout_then_login
from django.contrib.auth.views import logout
#from django.conf.urls import include

urlpatterns = [
    url(r'^accounts/',include('allauth.urls')),
    url(r'^$', views.inicio, name='inicio_vista'),
    url(r'^home/$', views.index, name="home_vista"),
    url(r'^Chihuahua/$', views.raza_Chihuahua, name="home_Chihuahua"),
    url(r'^Poodle/$', views.raza_Poodle, name="home_Poodle"),
    url(r'^Labrador/$', views.raza_Labrador, name="home_Labrador"),
    url(r'^Pitbull/$', views.raza_Pitbull, name="home_Pitbull"),
    url(r'^Pastor Aleman/$', views.raza_Pastor, name="home_Pastor"),
    url(r'^Husky/$', views.raza_Husky, name="home_Husky"),
    url(r'^Otro/$', views.raza_Otro, name="home_Otro"),
    url(r'^misPost/$', views.misPost, name="misPost_nombre"),
    url(r'profile/(?P<username>[a-zA-Z0-9]+)$', views.get_user_profile),
    url(r'^perfil/$', views.perfil_view, name="perfil_vista"),
    url(r'^vista1/$', views.vista1_view, name='vista1'),
    url(r'^post_create/$', views.post_create, name='create'),
    url(r'^post_detail/(?P<abc>\d+)/$', views.post_detail, name='detalle'),
    url(r'^post_update/(?P<abc>\d+)/$', views.post_update, name='editar'),
    url(r'^post_delete/$', views.post_delete, name='borrar'),
    url(r'^login/$', login, {'template_name': 'app/index_login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'app/logout.html'}  , name="logout"),
    url(r'^logout-then-login/$', logout_then_login, name='logout_then_login'),
    #url(r'^$', login, {'template_name': 'app/login.html'}  , name="login"),
    url(r'^registrate/$', views.registrate.as_view(), name="Registrate"),
 ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
