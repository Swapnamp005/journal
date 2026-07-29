from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from .models import Entry


class EntryListView(ListView):
    model = Entry
    template_name = "journal/entry_list.html"
    context_object_name = "entries"


class EntryDetailView(DetailView):
    model = Entry
    template_name = "journal/entry_detail.html"
    context_object_name = "entry"


class EntryCreateView(CreateView):
    model = Entry
    fields = ["title", "content"]
    template_name = "journal/entry_form.html"
    success_url = reverse_lazy("journal:entry_list")
