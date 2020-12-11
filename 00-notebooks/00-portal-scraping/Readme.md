# Background

file:///C:/Users/butzer/AppData/Local/Temp/1/Characterizing_Land_Surface_Phenology_and_Exotic_A.pdf


# Cloud versus Local Processing

## Links
- http://rangeland.ntsg.umt.edu/data/rap/rap-vegetation-cover/v2/
- https://www.mrlc.gov/data?f%5B0%5D=category%3ARangeland%20-%20Historical%20Time-Series%20%E2%80%93%20BIT

## Details
- Raster Data wrangling (work w/ Tony Butzer):
	- Transfer RAPv2.0 and BITv3 data (1984 to 2019) on annual herbaceous cover into our S3 bucket
	- Transfer DEM and derivatives (e.g. potential annual incident radiation), long-term climate averages, soils data (all on CFLUX), and extended study area extent into our S3 bucket.
-	Pre-process all these data (e.g. common projection and extent) in the cloud as needed
-	Model Database generation:
	-	Query AIM database for developing a shapefile of exotic annual grass cover (%) (already completed?) within our extended study area
	-	Sample NLCD high-resolution estimates of annual herbaceous cover (Rigge is working on getting these data to us; look for an email w/ a file location from me soon).
		-	Stratified sampling by year of observation (n= 30k/yr)
		-	Random sampling (N=1M)
		-	Retain x, y, year of observation, data source (AIM or NLCD), and % cover estimates
	-	Merge queried exotic annual grass cover AIM database and NLCD field and high-resolution grid data 
		-	Two databases total (i.e. simple random sampling + AIM data and stratified random sampling + AIM data)
	-	Develop Jupyter Notebook to extract RAPv2 and BITv2 data coincident with timing of field observation (i.e. 1:1 matching of timing of field observation and estimates of fractional cover) 
		-	Dev will likely have a python script for this which can be run in the cloud w/ tweaking
		-	Extract information on static environmental variables as you’ve done previously and save the shapefile and the attributes (as a csv) in the S3 bucket

