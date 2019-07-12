-- Create table to mimic csv
CREATE TABLE Volcano_Data (
	index integer PRIMARY KEY,
    volcano_number varchar(8),
	volcano_name varchar(255),
	country varchar(80),
	primary_volcano_type varchar(30),
	activity_evidence varchar(30),
	last_known_eruption varchar(12),
	region varchar(40),
	subregion varchar(40),
	latitude numeric,
	longitude numeric,
	elevation_in_meters numeric,
	dominant_rock_type varchar(50),
	tectonic_setting varchar(50)
);

-- Import volcano_data_cleaned.csv after creating table

SELECT * FROM volcano_data;

-- Index no longer needed, drop it
ALTER TABLE volcano_data 
DROP COLUMN index;
SELECT * FROM volcano_data;