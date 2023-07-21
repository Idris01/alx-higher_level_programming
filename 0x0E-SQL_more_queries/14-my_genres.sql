-- List all genres of show Dexter
SELECT 
tvg.name 
FROM tv_genres tvg 
JOIN tv_show_genres tvsg 
ON tvg.id = tvsg.genre_id 
JOIN tv_shows tvs ON tvs.id = tvsg.show_id 
WHERE tvs.title = 'Dexter' 
ORDER BY tvg.name;
