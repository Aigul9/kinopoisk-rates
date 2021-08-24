from database.db_connect import session, Film, Staff
from kp import logger


def load_film(f, orig_f):
    film_id = f['data']['filmId']
    exist = session.query(Film).filter(Film.film_id == film_id).first() is not None
    if exist:
        logger.error(f['data']['filmId'])
        return
    logger.info(f['data']['filmId'])
    if len(orig_f) < 9:
        my_vote = None
    else:
        my_vote = orig_f[8]
    film = Film(
        film_id,
        f['data']['nameRu'],
        f['data']['nameEn'],
        f['data']['webUrl'],
        f['data']['posterUrl'],
        f['data']['posterUrlPreview'],
        f['data']['year'],
        f['data']['filmLength'],
        orig_f[7],
        my_vote,
        f['data']['slogan'],
        f['data']['description'],
        f['data']['type'],
        f['data']['ratingMpaa'],
        f['data']['ratingAgeLimits'],
        f['data']['premiereRu'],
        f['data']['distributors'],
        f['data']['premiereWorld'],
        f['data']['premiereDigital'],
        f['data']['premiereWorldCountry'],
        f['data']['premiereDvd'],
        f['data']['premiereBluRay'],
        f['data']['distributorRelease'],
        [i['country'] for i in f['data']['countries']],
        [i['genre'] for i in f['data']['genres']],
        f['externalId']['imdbId'],
        f['rating']['rating'],
        f['rating']['ratingVoteCount'],
        f['rating']['ratingImdb'],
        f['rating']['ratingImdbVoteCount'],
        f['rating']['ratingFilmCritics'],
        f['rating']['ratingFilmCriticsVoteCount'],
        f['rating']['ratingAwait'],
        f['rating']['ratingAwaitCount'],
        f['rating']['ratingRfCritics'],
        f['rating']['ratingRfCriticsVoteCount'],
        f['budget']['grossRu'],
        f['budget']['grossUsa'],
        f['budget']['grossWorld'],
        f['budget']['budget'],
        f['budget']['marketing'],
        f['review']['reviewsCount'],
        f['review']['ratingGoodReview'],
        f['review']['ratingGoodReviewVoteCount'],
    )
    session.add(film)


def load_staff(s, film_id):
    print(s)
    staff = Staff(
        s['staffId'],
        film_id,
        s['nameRu'],
        s['nameEn'],
        s['description'],
        s['professionText'],
        s['professionKey']
    )
    session.add(staff)
    logger.info(f'{film_id}, {s["nameRu"]}')
