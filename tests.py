from django.test import TestCase
from django.urls import reverse

from .models import Entry


class JournalViewsTests(TestCase):
    def test_homepage_shows_entries(self):
        Entry.objects.create(title="My first day", content="Today was calm and productive.")

        response = self.client.get(reverse("journal:entry_list"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "My first day")

    def test_create_entry(self):
        response = self.client.post(
            reverse("journal:entry_create"),
            {"title": "New reflection", "content": "A short note for the day."},
        )

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Entry.objects.filter(title="New reflection").exists())
