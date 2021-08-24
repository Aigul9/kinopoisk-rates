from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.types import ARRAY

db_name = 'kinopoisk_db'
db_user = 'postgres'
db_pass = 'postgres'
db_host = 'localhost'
db_port = '5432'

db_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
db = create_engine(db_string)
Session = sessionmaker(bind=db)
Base = declarative_base()


class Film(Base):
    __tablename__ = 'films'
    film_id = Column(Integer, primary_key=True)
    name_ru = Column(String)
    name_en = Column(String)
    web_url = Column(String)
    poster_url = Column(String)
    poster_url_preview = Column(String)
    year = Column(Integer)
    film_length = Column(String)
    date_watched = Column(String)
    my_vote = Column(Integer)
    slogan = Column(String)
    description = Column(String)
    film_type = Column(String)
    rating_mpaa = Column(String)
    rating_age_limits = Column(Integer)
    premiere_ru = Column(String)
    distributors = Column(String)
    premiere_world = Column(String)
    premiere_digital = Column(String)
    premiere_world_country = Column(String)
    premiere_dvd = Column(String)
    premiere_blu_ray = Column(String)
    distributor_release = Column(String)
    countries = Column(ARRAY(String))
    genres = Column(ARRAY(String))
    imdb_id = Column(String)
    rating = Column(Float)
    rating_vote_count = Column(Integer)
    rating_imdb = Column(Float)
    rating_imdb_vote_count = Column(Integer)
    rating_film_critics = Column(String)
    rating_film_critics_vote_count = Column(Integer)
    rating_await = Column(String)
    rating_await_count = Column(Integer)
    rating_rf_critics = Column(String)
    rating_rf_critics_vote_count = Column(Integer)
    gross_ru = Column(Integer)
    gross_usa = Column(Integer)
    gross_world = Column(Integer)
    budget = Column(String)
    marketing = Column(Integer)
    reviews_count = Column(Integer)
    rating_good_review = Column(String)
    rating_good_review_vote_count = Column(Integer)

    def __init__(self, film_id, name_ru, name_en, web_url, poster_url, poster_url_preview, year, film_length,
                 date_watched, my_vote, slogan,
                 description, film_type, rating_mpaa, rating_age_limits, premiere_ru, distributors,
                 premiere_world, premiere_digital, premiere_world_country, premiere_dvd, premiere_blu_ray,
                 distributor_release, countries, genres, imdb_id,
                 rating, rating_vote_count, rating_imdb, rating_imdb_vote_count,
                 rating_film_critics, rating_film_critics_vote_count, rating_await, rating_await_count,
                 rating_rf_critics, rating_rf_critics_vote_count,
                 gross_ru, gross_usa, gross_world, budget, marketing,
                 reviews_count, rating_good_review, rating_good_review_vote_count):
        self.film_id = film_id
        self.name_ru = name_ru
        self.name_en = name_en
        self.web_url = web_url
        self.poster_url = poster_url
        self.poster_url_preview = poster_url_preview
        self.year = year
        self.film_length = film_length
        self.date_watched = date_watched
        self.my_vote = my_vote
        self.slogan = slogan
        self.description = description
        self.film_type = film_type
        self.rating_mpaa = rating_mpaa
        self.rating_age_limits = rating_age_limits
        self.premiere_ru = premiere_ru
        self.distributors = distributors
        self.premiere_world = premiere_world
        self.premiere_digital = premiere_digital
        self.premiere_world_country = premiere_world_country
        self.premiere_dvd = premiere_dvd
        self.premiere_blu_ray = premiere_blu_ray
        self.distributor_release = distributor_release
        self.countries = countries
        self.genres = genres
        self.imdb_id = imdb_id
        self.rating = rating
        self.rating_vote_count = rating_vote_count
        self.rating_imdb = rating_imdb
        self.rating_imdb_vote_count = rating_imdb_vote_count
        self.rating_film_critics = rating_film_critics
        self.rating_film_critics_vote_count = rating_film_critics_vote_count
        self.rating_await = rating_await
        self.rating_await_count = rating_await_count
        self.rating_rf_critics = rating_rf_critics
        self.rating_rf_critics_vote_count = rating_rf_critics_vote_count
        self.gross_ru = gross_ru
        self.gross_usa = gross_usa
        self.gross_world = gross_world
        self.budget = budget
        self.marketing = marketing
        self.reviews_count = reviews_count
        self.rating_good_review = rating_good_review
        self.rating_good_review_vote_count = rating_good_review_vote_count


Base.metadata.create_all(db)
session = Session()
session.commit()
