-- print all tv_shows title and tv_shows_genre id
SELECT 
	tvs.title,
	tvsg.genre_id 
	FROM tv_shows tvs 
	LEFT OUTER JOIN tv_show_genres tvsg 
	ON tvs.id = tvsg.show_id ORDER BY 1, 2;
