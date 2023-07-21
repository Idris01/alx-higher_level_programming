-- print all tv_shows title and tv_shows_genre id where genre_id is null
SELECT 
	tvg.name genre, 
	COUNT(*) number_of_shows 
	FROM tv_genres tvg JOIN tv_show_genres tvsg 
	ON tvsg.genre_id = tvg.id  
	GROUP BY 1 ORDER BY 2 DESC;
