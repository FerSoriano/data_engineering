create or replace procedure stg.pETL_Desastres()
language plpgsql
as $procedure$
DECLARE
	min_year INT;
begin 
	-- Obtener el resultado de la consulta y almacenarlo en la variable
	SELECT MIN(año) INTO min_year FROM stg.clima;
	
	-- Eliminar tabla temp si existe
	drop table if exists temp_desastres;
	
	-- creamos la tabla temporal
    create temp table temp_desastres AS
	select
		CASE 
	        WHEN c.año between min_year and min_year + 3
	        	THEN  
	        		CAST(min_year as text) || '-' || CAST(min_year + 3 as text)
	        WHEN c.año between  min_year + 4 and min_year + 7
	        	THEN 
	        		CAST(min_year + 4 as text) || '-' || CAST(min_year + 7 as text)
	    END AS Cuatrenio,
	    AVG(c.temperatura) as temp_avg,
	    AVG(c.oxigeno) as oxi_avg,
	    SUM(d.tsunamis) as t_tsunamis,
	    SUM(d.olas_calor) as t_olascalor,
	    SUM(d.terremotos) as t_terremotos,
	    SUM(d.erupciones) as t_erupciones,
	    SUM(d.incendios) as t_incendios,
		AVG((m.r_menor15 + m.r_15_a_30)) as m_jovenes_avg,
	    AVG((m.r_30_a_45 + m.r_45_a_60)) as m_adultos_avg,
	    AVG(m.r_m_a_60) as m_ancianos_avg
	FROM stg.clima c
	left join stg.desastres d 
		on d.año = c.año
	left join stg.muertes m 
		on m.año = c.año 
	group by Cuatrenio;

	-- Insertamos los datos en edw.DESASTRES_FINAL
	insert into edw.desastres_final
	select * from temp_desastres;
   
   
end;
$procedure$;


call stg.pETL_Desastres();

truncate table edw.desastres_final;
select * from edw.desastres_final;



