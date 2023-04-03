from .setup import verifyAge,get_movie_title,get_movie_year,get_movie_director,calculate_movie_rating,is_movie_classic
from .setup import is_movie_blockbuster,is_movie_rated_R,get_movie_genre,get_movie_cast,get_movie_duration
from .setup import add_movie_showing,is_movie_showing_sold_out,get_movie_showings,get_movie_showing,remove_movie_showing
import pytest

def test_verifyAge():
    with pytest.raises(ValueError):
        verifyAge('angela',-1)

def test_get_movie_title():
    movie = {"title": "The Shawshank Redemption", "year": 1994, "director": "Frank Darabont"}
    assert get_movie_title(movie) == "The Shawshank Redemption"

def test_get_movie_year():
    movie = {"title": "The Shawshank Redemption", "year": 1994, "director": "Frank Darabont"}
    assert get_movie_year(movie) == 1994

def test__create_user_book():
    user_book = {
        "user":'testuser',
        "movie_name":'Test Movie',
        "date":'23-04-23',
        "show":1,
        "seats":['A1', 'A2', 'B1', 'B2']
    }
    assert user_book['user'] == 'testuser'
    assert user_book['movie_name'] == 'Test Movie'

def test_get_movie_director():
    movie = {"title": "The Shawshank Redemption", "year": 1994, "director": "Frank Darabont"}
    assert get_movie_director(movie) == "Frank Darabont"

def test_calculate_movie_rating():
    ratings = [9.2, 9.3, 9.3, 9.3, 9.4]
    assert calculate_movie_rating(ratings) == 9.3

def test_is_movie_classic():
    classic_movie = {"title": "The Godfather", "year": 1972, "director": "Francis Ford Coppola"}
    assert is_movie_classic(classic_movie) == False

    non_classic_movie = {"title": "2001: A Space Odyssey", "year": 1968, "director": "Stanley Kubrick"}
    assert is_movie_classic(non_classic_movie) == True

def test_is_movie_blockbuster():
    blockbuster_movie = {"title": "Avatar", "box_office": 2787965087, "director": "James Cameron"}
    assert is_movie_blockbuster(blockbuster_movie) == True

    non_blockbuster_movie = {"title": "The Social Network", "box_office": 224920315, "director": "David Fincher"}
    assert is_movie_blockbuster(non_blockbuster_movie) == False

def test_create_user_movie():
    movie = {
        "user":'testuser',
        "movie_name":'Test Movie',
        "date":'23-04-23',
        "show":1,
        "seats":['A1', 'A2', 'B1', 'B2']
    }
    assert movie['user'] == 'testuser'
    assert movie['movie_name'] == 'Test Movie'


def test_get_movie_genre():
    movie = {"title": "Star Wars: Episode IV - A New Hope", "genre": ["Action", "Adventure", "Fantasy"], "director": "George Lucas"}
    assert get_movie_genre(movie) == ["Action", "Adventure", "Fantasy"]

def test_is_movie_rated_R():
    rated_R_movie = {"title": "Pulp Fiction", "rating": "R", "director": "Quentin Tarantino"}
    assert is_movie_rated_R(rated_R_movie) == True

    non_rated_R_movie = {"title": "The Lion King", "rating": "G", "director": "Roger Allers"}
    assert is_movie_rated_R(non_rated_R_movie) == False

def test_create_user_book8():
    user_book = {
        "user":'testuser',
        "movie_name":'Test Movie',
        "date":'23-04-23',
        "show":1,
        "seats":['A1', 'A2', 'B1', 'B2']
    }
    assert user_book['user'] == 'testuser'
    assert user_book['movie_name'] == 'Test Movie'
    assert user_book ['date'] == '23-04-23'
    assert user_book['show'] == 1
    assert user_book['seats'] == ['A1', 'A2', 'B1', 'B2']

def test_get_movie_cast():
    movie = {"title": "The Dark Knight", "cast": ["Christian Bale", "Heath Ledger", "Aaron Eckhart"], "director": "Christopher Nolan"}
    assert get_movie_cast(movie) == ["Christian Bale", "Heath Ledger", "Aaron Eckhart"]

def test_get_movie_duration():
    movie = {"title": "The Lord of the Rings: The Return of the King", "duration": 201, "director": "Peter Jackson"}
    assert get_movie_duration(movie) == 201

def test_add_movie_showing():
    schedule = {"1:00 PM": {"title": "The Incredibles", "duration": 115, "director": "Brad Bird"}}
    movie = {"title": "Jurassic Park", "duration": 127, "director": "Steven Spielberg"}
    add_movie_showing(schedule, movie, "4:00 PM")
    assert schedule == {"1:00 PM": {"title": "The Incredibles", "duration": 115, "director": "Brad Bird"}, "4:00 PM": {"title": "Jurassic Park", "duration": 127, "director": "Steven Spielberg"}}

def test_create_user_book4():
    book = {
        "user":'testuser',
        "movie_name":'Test Movie',
        "date":'23-04-23',
        "show":1,
        "seats":['A1', 'A2', 'B1', 'B2']
    }
    assert book['user'] == 'testuser'
    assert book['movie_name'] == 'Test Movie'
    assert book ['date'] == '23-04-23'


def test_create_user_book5():
    user = {
        "user":'testuser',
        "movie_name":'Test Movie',
        "date":'23-04-23',
        "show":1,
        "seats":['A1', 'A2', 'B1', 'B2']
    }
    assert user['user'] == 'testuser'
   

def test_remove_movie_showing():
    schedule = {"1:00 PM": {"title": "The Incredibles", "duration": 115, "director": "Brad Bird"}, "4:00 PM": {"title": "Jurassic Park", "duration": 127, "director": "Steven Spielberg"}}
    remove_movie_showing(schedule, "1:00 PM")

def test_get_movie_showing():
    schedule = {"1:00 PM": {"title": "The Incredibles", "duration": 115, "director": "Brad Bird"}, "4:00 PM": {"title": "Jurassic Park", "duration": 127, "director": "Steven Spielberg"}}
    assert get_movie_showing(schedule, "1:00 PM") == {"title": "The Incredibles", "duration": 115, "director": "Brad Bird"}
def test_create_user_book6():
    show_time= {
        "user":'testuser',
        "movie_name":'Test Movie',
        "date":'23-04-23',
        "show":1,
        "seats":['A1', 'A2', 'B1', 'B2']
    }
    assert show_time['show'] == 1
    assert show_time['seats'] == ['A1', 'A2', 'B1', 'B2']


def test_get_movie_showings():
    schedule = {"1:00 PM": {"title": "The Incredibles", "duration": 115, "director": "Brad Bird"}, "4:00 PM": {"title": "Jurassic Park", "duration": 127, "director": "Steven Spielberg"}}
    assert get_movie_showings(schedule) == [("1:00 PM", {"title": "The Incredibles", "duration": 115, "director": "Brad Bird"}), ("4:00 PM", {"title": "Jurassic Park", "duration": 127, "director": "Steven Spielberg"})]

def test_is_movie_showing_sold_out():
    sold_out_showing = {"title": "The Lion King", "duration": 118, "director": "Jon Favreau", "tickets": 0}
    schedule = {"1:00 PM": {"title": "The Incredibles", "duration": 115, "director": "Brad Bird"}, "4:00 PM": sold_out_showing}
    assert is_movie_showing_sold_out(schedule, "4:00 PM") == True
    available_showing = {"title": "The Matrix", "duration": 136, "director": "Lana Wachowski", "tickets": 5}
    schedule["7:00 PM"] = available_showing
    assert is_movie_showing_sold_out(schedule, "7:00 PM") == False

def test_create_user_book():
    user_book = {
        "user":'testuser',
        "movie_name":'Test Movie',
        "date":'23-04-23',
        "show":1,
        "seats":['A1', 'A2', 'B1', 'B2']
    }
    assert user_book['user'] == 'testuser'
    assert user_book['movie_name'] == 'Test Movie'

def test_create_user_book1():
    user_book = {
        "user":'testuser',
        "movie_name":'Test Movie',
        "date":'23-04-23',
        "show":1,
        "seats":['A1', 'A2', 'B1', 'B2']
    }
    assert user_book['user'] == 'testuser'
    assert user_book['movie_name'] == 'Test Movie'
    assert user_book ['date'] == '23-04-23'
    assert user_book['show'] == 1
    assert user_book['seats'] == ['A1', 'A2', 'B1', 'B2']

def test_create__user_book():
    user_book = {
        "user":'testuser',
        "movie_name":'Test Movie',
        "date":'23-04-23',
        "show":1,
        "seats":['A1', 'A2', 'B1', 'B2']
    }
    assert user_book['user'] == 'testuser'
    assert user_book['movie_name'] == 'Test Movie'
    assert user_book['seats'] == ['A1', 'A2', 'B1', 'B2']


