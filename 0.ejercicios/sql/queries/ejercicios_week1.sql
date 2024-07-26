-- Ejercicio 1: Extraer agentes cuyo nombre empieza por M o termina en O.
SELECT * FROM agents 
WHERE name LIKE 'M%' or name like '%o'

-- Ejercicio 2: Genera una lista en order alfabetico de todas las ocupaciones de la tabla 'Customer' que contengan la palabra 'Engineer'
SELECT DISTINCT occupation from customers where occupation like '%Engineer%' order by occupation 

-- Ejercicio 3: Devuelve el ID del cliente, Nombre y una columna nueva llamada "Mayor30" que contenga "Si" si el cliente tiene mas de 30 de edad. 
-- "No" en caso contrario
SELECT customerid, name, IIF(Age>=30,"Si","No") AS [Mayor30] FROM customers

-- Ejercicio 4: Devuelve todas las llamadas realizadas a clientes de la profesion de ingenieria y muestre si son mayores o menores de 30
-- asi como si terminaron comprando el producto de esa llamada.
SELECT IIF(cu.Age>30,"Si","No") AS [Mayor30], 
		count(1) AS [Total Llamadas],
		c.productsold 
FROM calls c 
left join customers cu
	on cu.customerid = c.customerid
where cu.occupation  LIKE '%Engineer%'
GROUP BY [Mayor30], c.productsold 

/*
Ejercicio 5: Escribir 2 consultas:
	1) Calcula las ventas y llamadas totales realizadas a los clientes de la profesion de ingenieria
	2) Calcula las mismas metricas para toda la BBDD
*/

SELECT SUM(productsold) AS [Ventas Totales], COUNT(callid) AS [Llamadas Totales] FROM calls c
left join customers cu
	on cu.customerid = c.customerid
where cu.occupation  LIKE '%Engineer%';

SELECT SUM(productsold) AS [Ventas Totales], COUNT(callid) AS [Llamadas Totales] FROM calls;

/*
Ejercicio 6: Escribir una consulta que devuelva:
	Para cada agente: el nombre del agente, la cantidad de llamadas, las llamadas mas largas y mas cortas, 
					  la duracion promedio de las llamadas y la cantidad total de productos vendidos.
	
	Nombre de las columnas: AgentName, NCalls, Shortest, Longest, AvdDuration y TotalSales
	Ordernar por: AgentName en orden alfabetico
*/
SELECT a.name as [AgentName],
	COUNT(c.callid) as [NCalls],
	MIN(c.duration) as [Shortest],
	MAX(c.duration) as [Longest],
	AVG(c.duration) as [AvdDuration],
	SUM (c.productsold) as [TotalSales]
	-- select * from calls where agentid = 10
from agents a
LEFT JOIN calls c ON a.agentid = c.agentid AND c.pickedup = 1
GROUP BY a.name 
ORDER BY a.name 

/*
 Ejercicio 7: Extraer 2 metricas del desempeño de los agentes de ventas:
 	1) Para cada agente, cuantos segundos promedio les toma vender un producto cuando tienen exito.
 	2) Para cada agente, cuantos segundos promedio permanecen en el telefono antes de darse por vencidos cuando no tienen exito
*/
SELECT a.name, a.AvgSucced, b.AvgNotSucced
FROM (
	SELECT a.agentid, a.name,
		   AVG(c.duration) AS [AvgSucced] 
	from agents a 
	LEFT JOIN calls c ON a.agentid = c.agentid
	WHERE c.pickedup = 1 and c.productsold = 1 
	GROUP BY a.name 
	) a
LEFT JOIN 
	(
	SELECT a.agentid, a.name,
		   AVG(c.duration) AS [AvgNotSucced] 
	from agents a 
	LEFT JOIN calls c ON a.agentid = c.agentid
	WHERE c.pickedup = 1 and c.productsold = 0
	GROUP BY a.name
	) b
ON b.agentid = a.agentid























