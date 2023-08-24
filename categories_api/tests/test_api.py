# import get_user_model
from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.urls import reverse
from model_bakery import baker
from rest_framework import status
from rest_framework.test import APITestCase

from categories.models import Category

User = get_user_model()


class CategoryViewTests(APITestCase):
    maxDiff = None

    def setUp(self):
        self.user = User.objects.create_superuser("test-user", "foo@bar.baz", "test-password")
        self.client.force_authenticate(user=self.user)

        category = Category.tree.create(name="Foo category", slug="foo_category", active=True, order=0, parent=None)
        Category.tree.create(name="Child category", slug="child_category", active=True, order=0, parent=category)
        baker.make(
            "SimpleText",
            primary_category=category,
        )
        cache.clear()

    def test_list(self):
        """
        Test list
        """
        url = reverse("categories-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertListEqual(
            response.json(),
            [
                {
                    "name": "Foo category",
                    "slug": "foo_category",
                    "active": True,
                    "thumbnail": None,
                    "thumbnail_width": None,
                    "thumbnail_height": None,
                    "order": 0,
                    "alternate_title": "",
                    "alternate_url": "",
                    "description": None,
                    "meta_keywords": "",
                    "meta_extra": "",
                    "children": [
                        {
                            "active": True,
                            "alternate_title": "",
                            "alternate_url": "",
                            "description": None,
                            "meta_extra": "",
                            "meta_keywords": "",
                            "name": "Child category",
                            "order": 0,
                            "children": [],
                            "flatpage_count": 0,
                            "flatpage_count_cumulative": 0,
                            "more_cats_count": 0,
                            "more_cats_count_cumulative": 0,
                            "slug": "child_category",
                            "other_cats_count": 0,
                            "other_cats_count_cumulative": 0,
                            "simpletext_count": 0,
                            "simpletext_count_cumulative": 0,
                            "simpletext_sec_cat_count": 0,
                            "simpletext_sec_cat_count_cumulative": 0,
                            "slug": "child_category",
                            "thumbnail": None,
                            "thumbnail_height": None,
                            "thumbnail_width": None,
                        }
                    ],
                    "flatpage_count": 0,
                    "flatpage_count_cumulative": 0,
                    "other_cats_count": 0,
                    "other_cats_count_cumulative": 0,
                    "more_cats_count": 0,
                    "more_cats_count_cumulative": 0,
                    "simpletext_count": 1,
                    "simpletext_count_cumulative": 1,
                    "simpletext_sec_cat_count": 0,
                    "simpletext_sec_cat_count_cumulative": 0,
                }
            ],
        )

    def test_detail(self):
        """
        Test detail
        """
        url = reverse("categories-detail", kwargs={"slug": "foo_category"})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertDictEqual(
            response.json(),
            {
                "name": "Foo category",
                "slug": "foo_category",
                "active": True,
                "thumbnail": None,
                "thumbnail_width": None,
                "thumbnail_height": None,
                "order": 0,
                "alternate_title": "",
                "alternate_url": "",
                "description": None,
                "meta_keywords": "",
                "meta_extra": "",
                "flatpage_count": 0,
                "flatpage_count_cumulative": 0,
                "other_cats_count": 0,
                "other_cats_count_cumulative": 0,
                "more_cats_count": 0,
                "more_cats_count_cumulative": 0,
                "simpletext_count": 1,
                "simpletext_count_cumulative": 1,
                "simpletext_sec_cat_count": 0,
                "simpletext_sec_cat_count_cumulative": 0,
            },
        )
