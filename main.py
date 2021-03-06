import database.db_load as db
import kp
from decouple import config


if __name__ == '__main__':
    # pages = kp.get_pages(int(config('COUNT')))
    # for page_no in range(1, 2):
    #     data = kp.extract_data(config('USER_ID'), page_no + 1)
    #     kp.save(page_no + 1, data)

    # all_films = kp.load_games('data/')
    all_films = kp.load_data('data/2')
    kp.logger.info(len(all_films))
    for orig_film in all_films:
        film_id = kp.get_movie_attr(orig_film[1])[1]
        extracted_film = kp.extract_data_api(film_id, config('API_KEY'))
        extracted_staff = kp.extract_staff_api(film_id, config('API_KEY'))
        load_status = db.load_film(extracted_film, orig_film)
        if not load_status:
            continue
        for staff in extracted_staff:
            db.load_staff(staff, film_id)
        db.session.commit()

db.session.close()
