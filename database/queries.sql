select * from films;
select * from staff;
select * from staff where film_id = 1236063 and staff_id = 41477;

--select base fields
select film_id, name_en, year, film_length, date_watched, my_vote, film_type,
       countries, genres, rating, rating_imdb from films;

--directors sorted by count
select s.name_en, count(*), array_agg(f.name_en) as count from staff s
join films f on s.film_id = f.film_id
where profession_key = 'DIRECTOR'
and s.name_en != ''
and film_type = 'FILM'
group by s.name_en
order by 2 desc;

--actors sorted by count
select s.name_en, count(*), array_agg(f.name_en) as count from staff s
join films f on s.film_id = f.film_id
where profession_key = 'ACTOR'
and s.name_en != ''
and film_type = 'FILM'
group by s.name_en
order by 2 desc;

select * from staff s join films f
on s.film_id = f.film_id
where s.name_en = 'David Lynch' and profession_key = 'DIRECTOR';

--average rates by director
select s.name_en,
       round(sum(my_vote) * 1.0 / count(*), 3) as average_votes,
       array_agg(f.name_en) movies,
       array_agg(f.my_vote) my_votes,
       array_agg(f.film_id) as movie_ids
from staff s join films f
on s.film_id = f.film_id
where profession_key = 'DIRECTOR'
and my_vote is not null
and film_type = 'FILM'
and s.name_en != ''
group by s.name_en
having array_length(array_agg(f.name_en), 1) > 1
order by 2 desc, 4 desc;

select * from staff s join films f
on s.film_id = f.film_id
where s.film_id = 428930 and profession_key = 'DIRECTOR';

select * from films f join staff s on f.film_id = s.film_id
where profession_key = 'PRODUCER_USSR';

--Japanese movies
select name_en, my_vote from films where 'Япония' = any(countries);

--fav series
select film_id, name_en, year, date_watched, my_vote, film_type,
       rating, rating_imdb
from films where film_type != 'FILM' and name_en is not null
and my_vote is not null
order by my_vote desc;

--kp rating is lower than imdb
select name_ru, name_en, rating, rating_imdb from films where rating < rating_imdb;
--146

--kp rating is higher than imdb
select name_ru, name_en, rating, rating_imdb from films where rating > rating_imdb;
--301

--kp rating equals to imdb rating
select name_ru, name_en, rating, rating_imdb from films where rating = rating_imdb;
--43

--the most expensive
select name_ru, name_en, gross_ru, gross_usa, gross_world from films
where gross_world is not null order by gross_world desc;

