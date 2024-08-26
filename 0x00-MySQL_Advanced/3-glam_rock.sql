-- finds difference
SELECT band_name,
	CASE
		WHEN split >= formed
			THEN split - formed
		ELSE 2022 - formed
	END AS lifespan
FROM metal_bands
WHERE LOCATE('Glam rock', style)
ORDER BY lifespan DESC;
