<div style="width: 100%; clear: both;">
  <div style="float: left; width: 50%;">
    <img src="http://www.uoc.edu/portal/_resources/common/imatges/marca_UOC/UOC_Masterbrand.jpg" align="left">
  </div>
  <div style="float: right; width: 50%;">
    <p style="margin: 0; padding-top: 22px; text-align:right;">PRA1 · Tipología y ciclo de vida de los datos</p>
    <p style="margin: 0; text-align:right; padding-button: 100px;">Marcos Caballero, Abril 2022</p>
    <p style='color: #105269; font-size: 18px; text-align:right; font-family: verdana'><b>  Máster Ciencia de Datos</b></p>
  </div>
</div>
<div style="width:100%;">&nbsp;</div>

# <b><u> Crawler precios de vinos </b></u>

## <b> Introducción </b>
Se desea elaborar un crawler para extraer diversa información acerca de los vinos a nivel nacional para la creación de un dataset y su posterior análisis y extracción de valor a lo largo del tiempo. Para ello, se utilizará la tecnología de web scrapping con el framework de Scrapy en Python.

En el futuro se pretende monitorear los precios de los vinos para aumentar la competitividad de las bodegas españolas.

## Cómo replicar el entorno
Comando para ejecutar el crawler: scrapy crawl carrefour -o wines_carrefour.csv
### Requerimientos
```bash
Scrapy==2.6.1
```
## Descripción del dataset 'Wines.csv'
Campos extraídos:
  - `wine`: el nombre del vino.
  - `winery`: la bodega del vino.
  - `origin`: la Denominación de Origen del vino.
  - `country`: en este caso siempre será España.
  - `variety`: el color del vino (tinto, blanco o rosado).
  - `price`: el precio del vino en euros.
  - `acidity`: la acidez del vino en g/l.
  - `alcohol_percentage`: el volumen de alcohol.
  - `date`: la fecha de extracción de los datos del crawler.
  - `source`: en este caso siempre será carrefour.

### Dataset
Enlace al repositorio Zenodo (DOI): 'Wines.csv'[URL_enlace]

## License:
<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/mcaballero99/carrefour_crawler">Wine Crawler</a> by <span property="cc:attributionName">Marcos Caballero </span> is licensed under <a href="http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY-NC 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1"></a></p>

## Bibliografía
- https://blog.appliedinformaticsinc.com/manipulate-scrapy-start_urls-before-a-request-is-made/
- https://stackoverflow.com/questions/9322219/how-to-generate-the-start-urls-dynamically-in-crawling