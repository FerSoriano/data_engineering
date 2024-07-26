-- run all the process
CALL edw.unit_test();

-- valid data
select * from stg.eventos_apocalipticos; 
select * from edw.prediccion_fin_mundo;


-- Query 1
select 
	SUM(case when nombre_evento like 'D%' then 1 else 0 end) as D_Events,
	SUM(case when nombre_evento like 'A%' then 1 else 0 end) as A_Events
from edw.prediccion_fin_mundo pfm;

-- Query 2
select 
	id_evento, 
	nombre_evento, 
	fecha_evento, 
	descripcion_evento, 
	dias_faltantes, 
	fuente_prediccion,
	a.Decada,
	b.Promedio_dias_restantes
from(
	select id_evento, 
		nombre_evento, 
		fecha_evento, 
		descripcion_evento, 
		dias_faltantes, 
		fuente_prediccion,
		substring(cast(extract(year from fecha_evento) as text) from 3 for 1) || '0' as Decada
	from edw.prediccion_fin_mundo pfm) a
left join (
	select 
		substring(cast(extract(year from fecha_evento) as text) from 3 for 1) || '0' as Decada,
		ROUND(AVG(dias_faltantes),2) as Promedio_dias_restantes
	from edw.prediccion_fin_mundo pfm
	group by decada
) b
on a.decada = b.decada
order by fecha_evento desc;