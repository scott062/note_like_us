from django.urls import path

from notes.views import NoteListView, NoteDetailView

urlpatterns = [
    path('notes/', NoteListView.as_view(), name='note_list'),
    path('notes/<uuid:pk>/', NoteDetailView.as_view(), name='note_detail'),
]
