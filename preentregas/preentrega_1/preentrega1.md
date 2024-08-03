# Preentrega No. 1

### Introducción

En este proyecto se creó un proceso de ETL. El tema elegido para la extracción de los datos fueron los **Juegos Olimpicos Paris 2024.** Busqué alguna API publica para obtener la información pero no logré encontrarla. Es por esto que decidí hacer el proceso de la Extracción por medio de Web Scraping, la Transformación fue directo en Python y la carga (_Load_) se hizo a la base de datos en Redshift.

### Estructura Logica

Lo dividi en 2 carpetas:

- db
  - Creé una clase llamada **DatabaseConection()** donde está almacenada la logica para la conexion a la base de datos.
  - Creé metodos para hacer las diferentes consultas e instrucciones:
    - Create
    - Update
    - Insert
    - Select
- etl
  - Creé una clase llamada **Medals()** donde está almacenada la logica para la extraccion de los datos de la pagina de los juegos olimpicos: (https://olympics.com/en/paris-2024/medals)
  - Cree métodos para el proceso de transformación de los datos.
    Toda esta logica se ejecutara desde el archivo **main.py**. Las credenciales para hacer la conexion a la Base de Datos se guardaron en un .env y se accede a ella por medio del modulo OS.
    En este archivo agregué 3 constantes que sirven como banderas para saber que se ejecutará:
- CREATE_TABLES
- CREATE_VIEWS
- RUN_ETL
  Estan almacenan valores booleanos y dan pie a que se ejecutara.

### Validaciones

- La base de datos tiene una columna de fecha que toma la ultima ejecucion del preoceso.
- Solo se puede ejecutar una vez al dia para evitar duplicidad en los datos.

### Estructura Base de Datos en Redshift

- 4 tablas
  - 2 de stage
  - 2 de edw
- 1 vista

#### Justificacion

- **Stage tables:**
  - stg_executionLog
    - Decidi crear una tabla de para llevar el control de las ejecuciones, esta me ayuda a saber que dia se ejecuto el proceso.
  - stg_medallero
    - Aqui almacenaré la informacion del dia de actual, en crudo despues de la transformacion en Python, sin agregarle columnas extras.
    - Esta tabla se truncará al inicio de cada ejecucion.
- **EDW tables:**
  - edw_coutries
    - Creé esta tabla para almacenar los paises y asignarles un ID, esto ayudará a relacionar con las otras tablas para crear diferentes tipos de analisis y vistas.
  - edw_medallero
    - Aqui se almacenara la data historica, dia a dia se guardaran los datos del medallero olimpico.
    - En esta tabla se agregaron 2 columnas mas que son:
      - Country_id
      - is_active
        - esta es una bandera para saber cuales son los datos que estan activos, es decir, los de la ultima ejecucion.
- **EDW Views:**
  - edw_medallero_view
    - Creé esta vista para poder tener de una manera mas legible y resumida la información del medallero olimpico. Está ordenada de manera ascendente por el puesto.
    - Tambien agregué una columna para saber la fecha de cuando fue actualizado.

### Mejoras

En las proximas entregas tratarde mejorar el codigo en Python, separaré la clase de **DatabaseConection()** en diferentes clases para tener un codigo mas legible y mas orientado a objetos. Tambien me enfocare en revisar el performance de la base de datos y en los comentarios que resiba.
