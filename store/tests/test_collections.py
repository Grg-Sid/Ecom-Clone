from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status


class TestCreateCollection:
    def test_if_user_anonymous_return_403(self):
        client = APIClient()
        response = client.post("/store/collections/", {"title": "test"})
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_user_not_admin_return_403(self):
        client = APIClient()
        client.force_authenticate(user={})
        response = client.post("/store/collections/", {"title": "test"})
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_data_is_invalid_return_400(self):
        client = APIClient()
        client.force_authenticate(user={User(is_staff=True)})
        response = client.post("/store/collections/", {"title": ""})
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data["title"] is not None

    def test_if_data_is_valid_return_201(self):
        client = APIClient()
        client.force_authenticate(user={User(is_staff=True)})
        response = client.post("/store/collections/", {"title": "hello"})
        assert response.status_code == status.HTTP_200_OK
        assert response.data["id"] > 0
