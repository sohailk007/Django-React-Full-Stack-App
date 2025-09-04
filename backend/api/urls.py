from django.urls import path
from api.views import NoteListCreate, NoteDelete
from .views import AccountCreateView, AccountListView


urlpatterns = [
    path("notes/", NoteListCreate.as_view(), name='note-list'),
    path('notes/delete/<int:pk>/', NoteDelete.as_view(), name='delete-note'),
    path("accounts/create/", AccountCreateView.as_view(), name="accounts-create"),
    path("accounts/", AccountListView.as_view(), name="accounts-list"),
    
]