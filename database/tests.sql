--A00
select count(*) from films;
select * from films order by film_id;
--490
--ok

--A01
select distinct name_ru from films order by 1;
select distinct name_en from films order by 1;
--ok

--A02
select * from films where web_url not like 'https%';
select * from films where poster_url not like 'https%';
select * from films where poster_url_preview not like 'https%';
--ok

--A03
select distinct year from films order by 1;
select * from films where length(cast(year as text)) != 4;
--ok

--A04
select * from films where film_length not like '%:%';
--ok

--A05
select distinct my_vote from films order by 1;
select distinct film_type from films;
select distinct rating_age_limits from films order by 1;
select distinct rating_mpaa from films order by 1;
select distinct premiere_digital from films;
--ok

--A06
select distinct premiere_world_country from films order by 1;
select distinct unnest(countries) from films order by 1;
select distinct unnest(genres) from films order by 1;
--ok

--A07
select * from films where left(imdb_id, 2) != 'tt';
--ok

--A08
select distinct rating from films order by 1;
select distinct rating_imdb from films order by 1;
select distinct rating_film_critics from films order by 1;

select * from films where rating = 0;
select * from films where rating_imdb = 0;
--ok

--A09
select * from films where left(budget, 1) != '$';
--ok

--B00
select count(*) from staff;
--57295
select count(distinct film_id) from staff;
--490

--B01
select * from films f left join staff s on f.film_id = s.film_id
where s.film_id is null;
--ok

--B02
select distinct profession_key from staff;
--ok

--B03
select * from staff where name_en = '';
--ok