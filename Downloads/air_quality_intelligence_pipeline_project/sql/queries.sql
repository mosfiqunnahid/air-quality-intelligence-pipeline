-- Air Quality Intelligence Pipeline SQL Queries

SELECT COUNT(*) AS total_records FROM air_quality_measurements;

SELECT parameter, AVG(value) AS avg_value
FROM air_quality_measurements
GROUP BY parameter
ORDER BY avg_value DESC;

SELECT parameter, MAX(value) AS max_value
FROM air_quality_measurements
GROUP BY parameter
ORDER BY max_value DESC;

SELECT parameter, value, unit, latitude, longitude, datetime_utc
FROM air_quality_measurements
ORDER BY value DESC
LIMIT 20;

SELECT parameter, COUNT(*) AS measurement_count
FROM air_quality_measurements
GROUP BY parameter
ORDER BY measurement_count DESC;
