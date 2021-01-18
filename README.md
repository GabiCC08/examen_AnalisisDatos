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
