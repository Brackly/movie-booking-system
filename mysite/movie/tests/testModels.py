from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import MovieMaster, SetMovie
from datetime import datetime, timedelta

class SetAdminTestCase(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser(username='admin', password='password')
        self.client.login(username='admin', password='admin')
        self.movie = MovieMaster.objects.create(m_name='Test Movie', m_desc='Test Description')
        self.set_movie = SetMovie.objects.create(active=self.movie, show='Test Show', start_time=datetime.now().date(), end_time=(datetime.now() + timedelta(days=7)).date(), price=100)

    def test_admin_login(self):
        response = self.client.get(reverse('setadmin:adminlogin'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'movie/admin_login.html')

    def test_admin_logout(self):
        response = self.client.get(reverse('setadmin:logout'))
        self.assertEqual(response.status_code, 302)

    def test_dashboard_view(self):
        response = self.client.get(reverse('setadmin:dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'movie/dashboard.html')
        self.assertContains(response, self.movie.m_name)

    def test_add_movie_view(self):
        response = self.client.get(reverse('setadmin:addmovie'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'movie/addmovies.html')

    def test_add_movie_form(self):
        response = self.client.post(reverse('setadmin:addmovie'), {'m_name': 'New Movie', 'm_desc': 'New Description', 'm_image': 'test.jpg'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(MovieMaster.objects.filter(m_name='New Movie').count(), 1)

    def test_set_movie_view(self):
        response = self.client.get(reverse('setadmin:setmovie'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'movie/setmovies.html')

    def test_set_movie_form(self):
        response = self.client.post(reverse('setadmin:setmovie'), {'active': self.movie.pk, 'show': 'New Show', 'start_time': datetime.now().date(), 'end_time': (datetime.now() + timedelta(days=7)).date(), 'price': 200})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(SetMovie.objects.filter(show='New Show').count(), 1)


