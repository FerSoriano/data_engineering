-- DROP PROCEDURE edw.is_new();

CREATE OR REPLACE PROCEDURE edw.is_new()
 LANGUAGE plpgsql
AS $procedure$
BEGIN
    -- Verificar si la columna ya existe para evitar errores
    IF NOT EXISTS (
        SELECT 1
        FROM information_schema.columns
        WHERE table_schema = 'stg'
        AND table_name = 'eventos_apocalipticos'
        AND column_name = 'is_new'
    ) THEN
    -- Agregar la columna is_new si no existe
    ALTER TABLE stg.eventos_apocalipticos
	    ADD COLUMN is_new INT NULL;
		END IF;
	-- Actualizar la columna is_new
    UPDATE stg.eventos_apocalipticos
    SET is_new = case
	    			when id_evento NOT IN (SELECT id_evento FROM edw.prediccion_fin_mundo) then 1
	    			else 0
	    		end;
   
END;
$procedure$
;