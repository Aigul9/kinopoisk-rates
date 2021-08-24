select * from films;
select * from staff;
select * from staff where film_id = 1236063 and staff_id = 41477;

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
