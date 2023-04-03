from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from ..forms import AddMovieForm, SetMovieForm
from ..models import MovieMaster, SetMovie


class AddMovieFormTest(TestCase):
    def test_valid_form(self):
        name = 'Test Movie'
        desc = 'A test movie'
        img = SimpleUploadedFile("test_image.jpg", b"content")
        form_data = {'m_name': name, 'm_desc': desc, 'm_image': img}
        form = AddMovieForm(data=form_data, files=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form_data = {'m_name': '', 'm_desc': ''}
        form = AddMovieForm(data=form_data)
        self.assertFalse(form.is_valid())


class SetMovieFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.movie = MovieMaster.objects.create(m_name='Test Movie', m_desc='A test movie')
        
    def test_valid_form(self):
        form_data = {
            'active': self.movie.id,
            'show': 'Morning',
            'start_time': '2023-04-01',
            'end_time': '2023-04-30',
            'price': 1000,
        }
        form = SetMovieForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form_data = {
            'active': '',
            'show': '',
            'start_time': '',
            'end_time': '',
            'price': '',
        }
        form = SetMovieForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_invalid_movie_choice(self):
        SetMovie.objects.create(active=self.movie, show='Morning', start_time='2023-04-01', end_time='2023-04-30', price=10)
        form = SetMovieForm()
        self.assertNotIn(self.movie, form.fields['active'].queryset)
