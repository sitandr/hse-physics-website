from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.course_views.index, name='home'),
    path('about-us', views.course_views.about, name='about'),
    path('create_task',
         views.course_views.create_task, name='create_task'),
    path('create_task?<int:course_id>',
         views.course_views.create_task, name='create_course_task'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('pages/<slug:slug>', views.course_views.course_page, name='pages'),
    path('create_course', views.course_views.create_course, name='create_course'),
    path('profiles/<int:user_id>', views.profile_view.show_profile, name='profile'),
    path('profiles/<int:user_id>/edit', views.profile_view.show_profile, {'edit': True}, name='edit_profile'),
    path('announcements', views.announcement_view.show_announcements, name='announce'),
    path('announcements/edit', views.announcement_view.show_announcements, {'edit': True}, name='write_announce'),
    path('announcements/remove?<int:ann_id>', views.announcement_view.remove_announcement, name='remove_announce'),
]
