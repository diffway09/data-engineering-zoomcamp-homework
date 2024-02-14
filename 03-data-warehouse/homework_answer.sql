-- Creating external table referring to gcs path
CREATE OR REPLACE EXTERNAL TABLE `northern-music-411504.ny_taxi.external_green_tripdata`
OPTIONS (
  format = 'parquet',
  uris = ['gs://data-warehouse-green-taxi/green_taxi.parquet']
);

-- Create a non partitioned table from external table
CREATE OR REPLACE TABLE northern-music-411504.ny_taxi.green_tripdata_non_partitioned AS
SELECT * FROM northern-music-411504.ny_taxi.external_green_tripdata;

-- Question 2: 0 MB
SELECT COUNT(DISTINCT PULocationID) FROM northern-music-411504.ny_taxi.external_green_tripdata;

-- Question 2: 6.41 MB
SELECT COUNT(DISTINCT PULocationID) FROM northern-music-411504.ny_taxi.green_tripdata_non_partitioned;

-- Question 3: 1622
SELECT COUNT(fare_amount) FROM northern-music-411504.ny_taxi.green_tripdata_non_partitioned
WHERE fare_amount = 0;

-- Question 4 
-- Creating a partition and cluster table from external table GREEN
CREATE OR REPLACE TABLE northern-music-411504.ny_taxi.green_tripdata_partitioned_clustered
PARTITION BY DATE(lpep_pickup_datetime)
CLUSTER BY PULocationID AS
SELECT * FROM northern-music-411504.ny_taxi.external_green_tripdata;

-- Question 5 : 12.82MB
-- Query non partitioned table GREEN
SELECT DISTINCT(PULocationID)
FROM northern-music-411504.ny_taxi.green_tripdata_non_partitioned
WHERE DATE(lpep_pickup_datetime) BETWEEN '2022-06-01' AND '2022-06-30';

-- Question 5 : 1.12MB
-- Query partitioned + clustered table GREEN
SELECT DISTINCT(PULocationID)
FROM northern-music-411504.ny_taxi.green_tripdata_partitioned_clustered
WHERE DATE(lpep_pickup_datetime) BETWEEN '2022-06-01' AND '2022-06-30';

