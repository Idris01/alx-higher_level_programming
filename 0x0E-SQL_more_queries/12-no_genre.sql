-- print all tv_shows title and tv_shows_genre id where genre_id is null
SELECT 
	tvs.title,
	tvsg.genre_id 
	FROM tv_shows tvs 
	LEFT OUTER JOIN tv_show_genres tvsg 
	ON tvs.id = tvsg.show_id 
	WHERE tvsg.genre_id IS NULL 
	ORDER BY 1, 2;
