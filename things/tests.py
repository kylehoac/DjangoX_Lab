from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Thing

class ThingTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester",
            email="test@email.com",
            password="password1234"
        )
        self.things = Thing.objects.create(
            name="pickle",
            reviewer= self.user,
            rating="10"
        )

    def test_thing_list_view(self):
        response = self.client.get(reverse("thing_list"))
        self.assertContains(response, "pickle")

    def test_thing_detail_view(self):
        response = self.client.get(reverse("thing_detail", args="1"))
        no_response = self.client.get("/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Reviewer: tester")
        self.assertTemplateUsed((response, "thing_detail.html"))

    def test_thing_create_view(self):
        response = self.client.post(
            reverse("thing_create"),
            {
                "name": "Ice Cream",
                "reviewer": self.user.id,
                "rating": "10",
            }, follow=True
        )

        self.assertRedirects(response, reverse("thing_detail",
        args="2"))
        self.assertContains(response, "Rating: 10")