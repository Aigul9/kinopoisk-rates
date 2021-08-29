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

select s.name_en, count(*), unnest(array_agg(f.name_ru)) as count from staff s
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

--most rated movies by country
select country,
       round(sum(my_vote) * 1.0 / count(*), 2) as res,
       sum(my_vote) as sum_votes,
       count(*) films_count,
       array_agg(my_vote) my_votes,
       array_agg(name_ru) movies
from
(select name_ru, unnest(countries) as country, my_vote from films
    where my_vote is not null) t
group by country
having count(*) > 2
order by res desc;

--by genres
select genre,
       round(sum(my_vote) * 1.0 / count(*), 2) as res,
       sum(my_vote) as sum_votes,
       count(*) films_count,
       array_agg(my_vote) my_votes,
       array_agg(name_ru) movies
from
(select name_ru, unnest(genres) as genre, my_vote from films
    where my_vote is not null) t
group by genre
order by res desc;

--by year
select
       case
           when 1920 < year and year <= 1930 then '1920-1930'
           when 1930 < year and year <= 1940 then '1930-1940'
           when 1940 < year and year <= 1950 then '1940-1950'
           when 1950 < year and year <= 1960 then '1950-1960'
           when 1960 < year and year <= 1970 then '1960-1970'
           when 1970 < year and year <= 1980 then '1970-1980'
           when 1980 < year and year <= 1990 then '1980-1990'
           when 1990 < year and year <= 2000 then '1990-2000'
           when 2000 < year and year <= 2010 then '2000-2010'
           when 2010 < year and year <= 2020 then '2010-2020'
           when 2020 < year and year <= 2030 then '2020-2030'
           else 'else'
           end as years,
       round(sum(my_vote) * 1.0 / count(*), 2) as res,
       sum(my_vote) as sum_votes,
       count(*) films_count,
       array_agg(my_vote) my_votes,
       array_agg(name_ru) movies
from films
where my_vote is not null
group by years
order by res desc;