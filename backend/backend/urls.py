from django.contrib import admin
from django.urls import path
from notes import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.get_routes, name='routes'),

    path('notes/', views.get_notes, name="notes"),
    path('notes/create/', views.add_note, name="create-note"),
    path('notes/<int:pk>/', views.get_note_by_id, name="note"),
    path('notes/<int:pk>/modify/', views.modify_note, name="update-note"),
    path('notes/<int:pk>/delete/', views.delete_note, name="delete-note"),
]
