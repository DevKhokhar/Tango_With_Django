from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/', views.about, name='about'),
        url(r'^add_category/$', views.add_category, name='add_category'),
        url(r'^add_page/$', views.add_page, name='add_page'),
        url(r'^category/(?P<category_name_url>\w+)/$', views.category, name='category'),
)