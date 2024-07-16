from django.contrib import admin
from django.urls import path
from notes import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('notes/', views.get_all_notes, name='All Notes'),
    path('notes/<str:uuid>/', views.get_note_by_id, 'Note')
]
