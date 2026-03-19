from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

User = get_user_model()


class UsersTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(name="John", email="john@example.com")

    def test_user_update_flow(self):
        update_url = reverse("users:update", kwargs={"pk": self.user.pk})
        list_url = reverse("users:index")

        # Отправка POST-запроса на изменение
        self.client.post(update_url, data={"name": "Bob", "email": self.user.email})

        # Переход на страницу списка пользователей
        response = self.client.get(list_url)

        # Проверяем, что новое имя отрисовано в HTML
        self.assertContains(response, "Bob")
        self.assertNotContains(response, "John")