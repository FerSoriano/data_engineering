-- DROP PROCEDURE edw.unit_test();

CREATE OR REPLACE PROCEDURE edw.unit_test()
 LANGUAGE plpgsql
AS $procedure$
begin
	call create_stg_table('eventos_apocalipticos');
	call insert_stg_data();
	call is_new(); 
	call create_edw_table('prediccion_fin_mundo');
	call insert_edw_data();
end;
$procedure$
;