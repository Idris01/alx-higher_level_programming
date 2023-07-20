-- List all tvshow titles and genre_id order by titles and then genre_id
SELECT 
	tvs.title,
	tvg.genre_id  
FROM  tv_shows tvs 
JOIN tv_show_genres tvg ON tvg.show_id = tvs.id
JOIN tv_genres tvge ON tvge.id = tvg.genre_id
ORDER BY tvs.title, tvg.genre_id ASC;
