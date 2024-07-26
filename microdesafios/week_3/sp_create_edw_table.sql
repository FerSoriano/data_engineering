-- DROP PROCEDURE edw.create_edw_table(varchar);

CREATE OR REPLACE PROCEDURE edw.create_edw_table(IN table_name character varying)
 LANGUAGE plpgsql
AS $procedure$
begin 
	
	execute format('drop table if exists edw.%I', table_name);
	
	execute format(
		'create table edw.%I(
			id_evento int not null,
			nombre_evento varchar(100),
			fecha_evento date,
			descripcion_evento varchar(500),
			dias_faltantes numeric,
			fuente_prediccion varchar(100)
		)', table_name);
end;
$procedure$
;