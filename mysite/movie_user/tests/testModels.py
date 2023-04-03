from django.test import TestCase
from django.contrib.auth.models import User
from datetime import date
from .models import UserBook, BookedSeatsModel


class UserBookModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.user_book = UserBook.objects.create(
            user=self.user,
            movie_name='Test Movie',
            date=date.today(),
            show=1,
            seats='A1,A2,B1,B2'
        )

    def test_user_book_creation(self):
        self.assertEqual(UserBook.objects.count(), 1)

    def test_user_book_fields(self):
        self.assertEqual(self.user_book.user, self.user)
        self.assertEqual(self.user_book.movie_name, 'Test Movie')
        self.assertEqual(self.user_book.date, date.today())
        self.assertEqual(self.user_book.show, 1)
        self.assertEqual(self.user_book.seats, 'A1,A2,B1,B2')


class BookedSeatsModelTestCase(TestCase):
    def setUp(self):
        self.booked_seats = BookedSeatsModel.objects.create(
            movie_name='Test Movie',
            date=date.today(),
            time=1,
            seats='A1,A2,B1,B2',
            number=4
        )

    def test_booked_seats_creation(self):
        self.assertEqual(BookedSeatsModel.objects.count(), 1)

    def test_booked_seats_fields(self):
        self.assertEqual(self.booked_seats.movie_name, 'Test Movie')
        self.assertEqual(self.booked_seats.date, date.today())
        self.assertEqual(self.booked_seats.time, 1)
        self.assertEqual(self.booked_seats.seats, 'A1,A2,B1,B2')
        self.assertEqual(self.booked_seats.number, 4)
