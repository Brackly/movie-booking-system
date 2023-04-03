
def setup():
    x=input("connecting to database....")

def verifyAge(name: str, age: int) -> str:
    if age < 0:
        raise ValueError("Age cannot be negative.")
    elif age < 18:
        return f"Hi {name}! You are not an adult yet."
    elif age < 65:
        return f"Hello {name}! You are an adult."
    else:
        return f"Good day {name}! You are a senior citizen."

# app/movies.py
# function 1: get movie title
def get_movie_title(movie):
    return movie["title"]


# function 2: get movie year
def get_movie_year(movie):
    return movie["year"]

# function 3: get movie director
def get_movie_director(movie):
    return movie["director"]


# function 4: calculate movie rating
def calculate_movie_rating(ratings):
    return sum(ratings) / len(ratings)

# function 5: check if a movie is a classic
def is_movie_classic(movie):
    if movie["year"] < 1970:
        return True
    return False

def get_movie_duration(movie):
    return movie["duration"]

def get_movie_cast(movie):
    return movie["cast"]

def is_movie_rated_R(movie):
    if "R" in movie["rating"]:
        return True
    return False

def get_movie_genre(movie):
    return movie["genre"]

def is_movie_blockbuster(movie):
    if movie["box_office"] > 1000000000:
        return True
    return False

def main():
    print(verifyAge('angela',10))

def add_movie_showing(schedule, movie, time):
    schedule[time] = movie
def remove_movie_showing(schedule, time):
    del schedule[time]

def get_movie_showing(schedule, time):
    return schedule[time]

def get_movie_showings(schedule):
    return list(schedule.items())

def get_movie_showings(schedule):
    return list(schedule.items())

def is_movie_showing_sold_out(schedule, time):
    if "tickets" in schedule[time]:
        if schedule[time]["tickets"] == 0:
            return True
    return False

if __name__=="__main__":
    main()