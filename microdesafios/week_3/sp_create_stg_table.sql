-- DROP PROCEDURE edw.create_stg_table(varchar);

CREATE OR REPLACE PROCEDURE edw.create_stg_table(IN table_name character varying)
 LANGUAGE plpgsql
AS $procedure$
begin 
	
	execute format('drop table if exists stg.%I', table_name);
	
	execute format(
		'create table stg.%I(
			id_evento int not null,
			nombre_evento varchar(100),
			fecha_evento date,
			descripcion_evento varchar(500)
		)', table_name);
end;
$procedure$
;