-- script that lists all the cities of california registered in the database
SELECT id, name -- Query to list all the cities from california
FROM cities
WHERE state_id = ( -- Query to get the id of california
	SELECT id
	FROM states
	WHERE name = california");
