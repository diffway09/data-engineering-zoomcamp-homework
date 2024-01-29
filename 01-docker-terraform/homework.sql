SELECT * from green_taxi_trips ORDER BY lpep_pickup_datetime desc limit 10;
SELECT * from taxi_zone_data;

-- Question 3. Count records
-- ANS : 15612
SELECT COUNT(*) FROM green_taxi_trips
WHERE DATE(lpep_pickup_datetime) = '2019-09-18'
AND DATE(lpep_dropoff_datetime) = '2019-09-18';

-- Question 4. Largest trip for each day
-- ANS : 2019-09-26
SELECT DATE(lpep_pickup_datetime) ,SUM(trip_distance) 
FROM green_taxi_trips
WHERE DATE(lpep_pickup_datetime) 
IN ('2019-09-18',
	'2019-09-16',
'2019-09-26',
'2019-09-21')
GROUP BY DATE(lpep_pickup_datetime) 
ORDER BY DATE(lpep_pickup_datetime) DESC;

-- Question 5. The number of passengers
-- ANS : "Brooklyn" "Manhattan" "Queens"
SELECT "Borough",SUM(total_amount) 
FROM green_taxi_trips AS trips
INNER JOIN taxi_zone_data AS zone
ON trips."PULocationID" = zone."LocationID"
WHERE DATE(lpep_pickup_datetime) = '2019-09-18'
AND "Borough" != 'Unknown'
GROUP BY "Borough"
HAVING SUM(total_amount) > 50000;

-- Question 6. Largest tip
-- ANS : JFK Airport
SELECT do_zone."Zone"
FROM green_taxi_trips AS trips
INNER JOIN taxi_zone_data AS pu_zone
	ON trips."PULocationID" = pu_zone."LocationID" 
	AND pu_zone."Zone" = 'Astoria'
	AND DATE(trips.lpep_pickup_datetime) BETWEEN '2019-09-01' AND '2019-09-30'
INNER JOIN taxi_zone_data AS do_zone
	ON trips."DOLocationID" = do_zone."LocationID"
ORDER BY tip_amount DESC;