from django.test import TestCase
from django.urls import reverse
from ..models import SetMovie, MovieMaster
from ..forms import SetMovieForm


class SetMovieFormTest(TestCase):

    def setUp(self):
        self.movie = MovieMaster.objects.create(name='Test Movie')
        self.form_data = {
            'active': self.movie.pk,
            'start_time': '04/03/2023',
            'end_time': '04/04/2023',
            'show': '1',
            'price': '10'
        }

    def test_valid_form(self):
        form = SetMovieForm(data=self.form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        self.form_data['active'] = ''  # remove the required field
        form = SetMovieForm(data=self.form_data)
        self.assertFalse(form.is_valid())

    def test_widget_attrs(self):
        form = SetMovieForm()
        self.assertIn('class="form-control"', str(form['active']))
        self.assertIn('class="form-control"', str(form['show']))
        self.assertIn('class="form-control"', str(form['start_time']))
        self.assertIn('class="form-control"', str(form['end_time']))
        self.assertIn('class="form-control"', str(form['price']))

    def test_movie_choice_queryset(self):
        form = SetMovieForm()
        movie_choice = form.fields['active'].queryset
        self.assertQuerysetEqual(movie_choice, MovieMaster.objects.filter(setmovie__isnull=True))

