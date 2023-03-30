-- a script that displays the max temperature
-- of ecah state (ordered by state name).
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER- BY max_tmp DESC;
