from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_successful(self):
        """ Test creating a new user with an email is successful """

        email = 'geonsangyoo@gmail.com'
        password = 'TestPassword1234'
        user = get_user_model().objects.create(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(password == user.password)
