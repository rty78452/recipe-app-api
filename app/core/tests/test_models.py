from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        email = 'uhie@hdosdio.com'
        password = '12345678'
        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email = 'njid@HSIIJSM.COM'
        user = get_user_model().objects.create_user(email, 'fghj193')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'fghj1235')

    def test_create_new_superuser(self):
        user = get_user_model().objects.create_superuser('erty@rtyui.com', 'ewrty5678')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
