-- DROP PROCEDURE edw.insert_edw_data();

CREATE OR REPLACE PROCEDURE edw.insert_edw_data()
 LANGUAGE plpgsql
AS $procedure$
begin 
	insert into edw.prediccion_fin_mundo
	select *
	from (
		select 
			ea.id_evento,
			ea.nombre_evento,
			ea.fecha_evento,
			ea.descripcion_evento,
			date_part('day', ea.fecha_evento - now()) as dias_faltantes, 
		 	'Eventos Apocalipticos' as fuente_prediccion
		from stg.eventos_apocalipticos ea
		where is_new = 1
		) a;
end;
$procedure$
;