from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('create_task',
         views.create_task, name='create_task'),
    path('create_task?<int:course_id>',
         views.create_task, name='create_course_task'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('pages/<slug:slug>', views.course_page, name='pages'),
    path('create_course', views.create_course, name='create_course'),
    path('profiles/<int:user_id>', views.show_profile, name='profiles'),
]

