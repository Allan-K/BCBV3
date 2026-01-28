from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path('', views.index, name='index'),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("sign_up/", views.sign_up, name="sign_up"),
    path('music', views.music, name='music'),
    path('search_music/', views.search_music, name='search_music'),
    path('add_tune/', views.add_tune, name='add_tune'),
    path('confirm/', views.confirm, name='confirm'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('add_testimonial_item/', views.add_testimonial_item, name='add_testimonial_item'),
    path('edit_testimonial/<int:id>', views.edit_testimonial, name='edit_testimonial'),
    path('delete_testimonial_item/<int:id>', views.delete_testimonial_item, name='delete_testimonial_item'),
    path('events/', views.events, name='events'),
    path('add_events_item/', views.add_events_item, name='add_events_item'),
    path('links/', views.links, name='links'),
    path('add_link/', views.add_link, name='add_link'),
    path('delete_link/<int:id>', views.delete_link, name='delete_link'),
    path('gallery/', views.gallery, name='gallery'),
    path('add_gallery_item/', views.add_gallery_item, name='add_gallery_item'),
    path('edit_gallery/<int:id>', views.edit_gallery, name='edit_gallery'),
    path('delete_gallery_item/<int:id>', views.delete_gallery_item, name='delete_gallery_item'),
    path('hire_us/', views.hire_us, name='hire_us'),
]
if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)