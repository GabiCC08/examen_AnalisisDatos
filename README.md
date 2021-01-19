# Examen de Analisis de Datos
![Indicaciones](https://github.com/GabiCC08/examen_AnalisisDatos/blob/main/Indicaciones.jpg)

## Explicación:

### Tema: Casas y departamentos en venta.

**1. Script 1.py**
- Se extraen todos los tweets relacionados con: *DepartamentoEnVenta*, *CasaEnVenta*, *VentaDeDepartamento*, *VentaDeCasa* e *Inmobiliaria*.
- Se estable una conexión con el gestor de bases de datos CouchDB.
- Y se guardan los tweets en la base datos *"en_venta"* como archivos json.

**2. Script 2.py**
- Se extraen los campos: *title*, *detail*, *location* y *price*, del sitio web https://www.olx.com.ec/pichincha_g2007376/departamentos-casas-venta_c367/q-departamentos 
- Se forman los archivos json con los datos obtenidos.
- Se estable una conexión con el sistema MongoDB.
- Y se guardan los datos en la colección *"en_venta"* de la base datos *"examen"*.

**3. Script 3.py**
- Se extraen los datos de la analitica de la inmobiliaria *"idealista"* de Facebook.
- Se estable una conexión con el sistema MongoDB.
- Y se guardan los datos en la colección *"en_ventaFB"* de la base datos *"examen"*.

**4. Script 4.py**
- Se crea la base de datos *"examen.db"* en SQLite.
- Se accede a la bd *"examen.db"*, se crea la tabla *"en_venta"* y se ingresan datos referentes a ventas de casas y departamentos (con los campos: *id*, *title*, *location* y *price*).
- Se accede a los datos de la tabla definiendo el *id* como index del dataframe.
- Se transforman a archivo json.
- Se estable una conexión con el sistema MongoDB.
- Y se guardan los datos en la colección *"en_venta"* (donde ya existian documentos previos - Script 2) de la base datos *"examen"*.

**5. Script 5.py**
- Se estable una conexión con el gestor de bases de datos CouchDB.
- Se estable una conexión con el sistema MongoDB.
- Se extraen todos los documentos de la bd *"en_venta"* de CouchDB.
- Y se guardan en la colección *"en_ventaCouch"* de la base datos *"examen"* de MongoDB.

**6. Script 6.py**
- Se estable una conexión con el gestor de bases de datos CouchDB.
- Se estable una conexión con el sistema MongoDB.
- Se extraen todos los documentos de las colecciones de la base datos *"examen"* de MongoDB.
- Y se guardan en la base datos *"en_venta"* de CouchDB.
**7. Script 7.py**
- Se estable una conexión con el gestor de bases de datos CouchDB.
- Se estable una conexión con el servicio de Cloud Database de MongoDB (MongoDB Atlas).
- Se extraen todos los documentos de la bd *"en_venta"* de CouchDB.
- Y se guardan en la colección *"en_venta"* de la base datos *"examen"* de MongoDB Atlas.

**8. Script 8.py**
- Se estable una conexión con el sistema MongoDB.
- Se estable una conexión con el servicio de Cloud Database de MongoDB (MongoDB Atlas).
- Se extraen todos los documentos de las colecciones de la base datos *"examen"* de MongoDB.
- Y se guardan en la colección *"en_venta"* de la base datos *"examen"* de MongoDB Atlas.

**9. Script 9-10.py**
- Se estable una conexión con el servicio de Cloud Database de MongoDB (MongoDB Atlas).
- Se extraen todos los documentos de la coleccion *"en_venta"* de la base datos *"examen"* de MongoDB Atlas.
- Y se guardan en el archivo *"en_venta.csv"*.
- *Nota: Al tener diferentes documentos de diferentes fuentes, no coinciden los atributos (columnas-campos), sin embargo e guardan todos los datos.
