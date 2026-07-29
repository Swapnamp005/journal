from django.urls import path

from .views import EntryCreateView, EntryDetailView, EntryListView

app_name = 'journal'

urlpatterns = [
    path('', EntryListView.as_view(), name='entry_list'),
    path('entries/new/', EntryCreateView.as_view(), name='entry_create'),
    path('entries/<int:pk>/', EntryDetailView.as_view(), name='entry_detail'),
]
