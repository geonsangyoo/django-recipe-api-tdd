from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_successful(self):
        """Test creating a new user with an email is successful"""
        email = "geonsangyoo@gmail.com"
        password = "TestPassword1234"
        user = get_user_model().objects.create(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(password == user.password)

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = "geonsangyoo@GMAIL.COM"
        user = get_user_model().objects.create_user(email=email,
                                                    password="test123")

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "teset123")

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            "test@gmail.com", "test123")

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
