from django.test import TestCase
from django.contrib.auth.models import User
from . import forms


class CreateUserFormTestCase(TestCase):
    def test_form_valid(self):
        user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'testpass123',
            'password2': 'testpass123',
        }
        form = forms.CreateUserForm(data=user_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        user_data = {
            'username': '',
            'email': 'testuser@example.com',
            'password1': 'testpass123',
            'password2': 'testpass456',  # password2 does not match password1
        }
        form = forms.CreateUserForm(data=user_data)
        self.assertFalse(form.is_valid())


class BookedSeatsFormTestCase(TestCase):
    def test_form_valid(self):
        seats_data = {
            'booked_seats': 'A1, A2, A3',
        }
        form = forms.BookedSeatsForm(data=seats_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        seats_data = {
            'booked_seats': '',
        }
        form = forms.BookedSeatsForm(data=seats_data)
        self.assertFalse(form.is_valid())


class CheckDateFormTestCase(TestCase):
    def test_form_valid(self):
        date_data = {
            'date_start': '2023-04-01',
            'date_end': '2023-04-30',
            'book_date': '2023-04-15',
        }
        form = forms.CheckDateForm(data=date_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        date_data = {
            'date_start': '2023-04-01',
            'date_end': '2023-04-30',
            'book_date': '2023-03-15',  # book_date before date_start
        }
        form = forms.CheckDateForm(data=date_data)
        self.assertFalse(form.is_valid())
