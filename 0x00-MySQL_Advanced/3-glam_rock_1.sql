-- finds difference
SELECT band_name,
	CASE
		WHEN split IS NOT NULL
			THEN split - formed
		ELSE (CURDATE()) - formed
	END AS lifespan
FROM metal_bands
WHERE style = 'Glam rock'
ORDER BY lifespan DESC;
