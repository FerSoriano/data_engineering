create or replace procedure stg.sp_create_insert_edw()
language plpgsql
as $procedure$
begin 
	
		drop table if exists edw.DESASTRES_FINAL;
		
		CREATE TABLE edw.DESASTRES_FINAL
		(Cuatrenio varchar(20) NOT NULL PRIMARY KEY,
		Temp_AVG FLOAT NOT NULL, 
		Oxi_AVG FLOAT NOT NULL,
		T_Tsunamis INT NOT NULL,
		T_OlasCalor INT NOT NULL,
		T_Terremotos INT NOT NULL, 
		T_Erupciones INT NOT NULL,
		T_Incendios INT NOT NULL,
		M_Jovenes_AVG FLOAT NOT NULL,
		M_Adutos_AVG FLOAT NOT NULL,
		M_Ancianos_AVG FLOAT NOT NULL);
	
end;
$procedure$;
