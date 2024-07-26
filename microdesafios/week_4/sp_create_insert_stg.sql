create or replace procedure stg.sp_create_insert_stg()
language plpgsql
as $procedure$
begin 
	
		-- 1. crear tabla clima futuro global
		drop table if exists stg.clima;
		
		CREATE TABLE stg.clima
		(año INT NOT NULL PRIMARY KEY,
		Temperatura FLOAT NOT NULL,
		Oxigeno FLOAT NOT NULL);
		
		-- Insertar valores manualmente
		INSERT INTO stg.clima VALUES (2023, 22.5,230);
		INSERT INTO stg.clima VALUES (2024, 22.7,228.6);
		INSERT INTO stg.clima VALUES (2025, 22.9,227.5);
		INSERT INTO stg.clima VALUES (2026, 23.1,226.7);
		INSERT INTO stg.clima VALUES (2027, 23.2,226.4);
		INSERT INTO stg.clima VALUES (2028, 23.4,226.2);
		INSERT INTO stg.clima VALUES (2029, 23.6,226.1);
		INSERT INTO stg.clima VALUES (2030, 23.8,225.1);
		
		-- 2. crear tabla desastres proyectados globales
		drop table if exists stg.desastres;
		
		CREATE TABLE stg.desastres
		(año INT NOT NULL PRIMARY KEY,
		Tsunamis INT NOT NULL,
		Olas_Calor INT NOT NULL,
		Terremotos INT NOT NULL,
		Erupciones INT NOT NULL,
		Incendios INT NOT NULL);
		
		-- Insertar valores manualmente
		INSERT INTO stg.desastres VALUES (2023, 2,15, 6,7,50);
		INSERT INTO stg.desastres VALUES (2024, 1,12, 8,9,46);
		INSERT INTO stg.desastres VALUES (2025, 3,16, 5,6,47);
		INSERT INTO stg.desastres VALUES (2026, 4,12, 10,13,52);
		INSERT INTO stg.desastres VALUES (2027, 5,12, 6,5,41);
		INSERT INTO stg.desastres VALUES (2028, 4,18, 3,2,39);
		INSERT INTO stg.desastres VALUES (2029, 2,19, 5,6,49);
		INSERT INTO stg.desastres VALUES (2030, 4,20, 6,7,50);
		
		-- 3. crear tabla muertes proyectadas por rangos de edad
		drop table if exists stg.muertes;
		
		CREATE TABLE stg.muertes
		(año INT NOT NULL PRIMARY KEY,
		R_Menor15 INT NOT NULL,
		R_15_a_30 INT NOT NULL,
		R_30_a_45 INT NOT NULL,
		R_45_a_60 INT NOT NULL,
		R_M_a_60 INT NOT NULL);
		
		-- Insertar valores manualmente
		INSERT INTO stg.muertes VALUES (2023, 1000,1300, 1200,1150,1500);
		INSERT INTO stg.muertes VALUES (2024, 1200,1250, 1260,1678,1940);
		INSERT INTO stg.muertes VALUES (2025, 987,1130, 1160,1245,1200);
		INSERT INTO stg.muertes VALUES (2026, 1560,1578, 1856,1988,1245);
		INSERT INTO stg.muertes VALUES (2027, 1002,943, 1345,1232,986);
		INSERT INTO stg.muertes VALUES (2028, 957,987, 1856,1567,1756);
		INSERT INTO stg.muertes VALUES (2029, 1285,1376, 1465,1432,1236);
		INSERT INTO stg.muertes VALUES (2030, 1145,1456, 1345,1654,1877);
	
end;
$procedure$;
