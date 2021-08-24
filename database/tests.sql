--A00
select count(*) from films;
select * from films order by film_id;
--490

--A01
select name_ru from films order by 1;
select name_en from films order by 1;

--A02
select * from films where web_url not like 'https%';
select * from films where poster_url not like 'https%';
select * from films where poster_url_preview not like 'https%';

--A03
select distinct year from films order by 1;
select * from films where length(year) != 4;

--A04
select * from films where film_length not like '%:%'

--A05
select distinct my_vote from films order by 1;
select distinct film_type from films;
select distinct rating_age_limits from films order by 1;
select distinct rating_mpaa from films order by 1;
select distinct premiere_digital from films;

--A06
select distinct premiere_world_country from films;
select distinct unnest(countries) from films;
select distinct unnest(genres) from films;

--A07
select * from films where left(imdb_id, 2) != 'tt';

--A08
select distinct rating from films order by 1;
select distinct rating_imdb from films order by 1;
select distinct rating_film_critics from films order by 1;

--A09
select * from films where left(budget, 1) != '$'

