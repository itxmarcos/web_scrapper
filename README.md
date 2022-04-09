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
Se desea elaborar varios crawlers para extraer diversa información acerca de los vinos a nivel nacional para la creación de un dataset y su posterior análisis y extracción de valor a lo largo del tiempo. Para ello, se utilizará la tecnología de web scrapping con el framework de Scrapy en Python y un API.

En el futuro se pretende monitorear los precios de los vinos para aumentar la competitividad de las bodegas españolas.

## Cómo replicar el entorno
Comandos para ejecutar los crawlers:
```bash
cd carrefour_scrapy
scrapy crawl carrefour -o wines_carrefour.csv

cd vivino_API
python vivino.py
```

### Requerimientos
Python 3.9.7, pip 21.2.4
```bash
Scrapy==2.6.1
pandas==1.4.2
```

## Descripción de los directorios
### carrefour_scrapy/wines/spiders/carrefour.py
Con el comando "scrapy startproject <...>" y "scrapy genspider <...> <...>" automáticamente se crean los directorios que se observan dentro de carrefour_scrapy. Lo más destacable ocurre en carrefour.py, donde se recogen todas las urls de vinos tintos, rosados y blancos, se hace click en cada vino de cada página y dentro del mismo se recogen los valores de los campos detallados posteriormente. Automáticamente Scrapy dispone de un atributo output que inserta todo lo extraído en un csv.
### vivino_API/vivino.py
El único fichero es vivino.py donde se recogen todas las páginas JSON del API de Vivino y se van iterando recogiendo los valores de los campos detallados posteriormente. Dichos valores se van insertando en un dataframe de Pandas y al final se convierten en un csv.

## Descripción del dataset 'wines_carrefour.csv'
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

## Descripción del dataset 'wines_vivino.csv'
Campos extraídos:
  - `wine`: el nombre del vino.
  - `winery`: la bodega del vino.
  - `origin`: la Denominación de Origen del vino.
  - `country`: en este caso siempre será España.
  - `variety`: el color del vino (tinto, blanco o rosado).
  - `grape`: el tipo de uva del vino.
  - `price`: el precio del vino en euros.
  - `rating`: la puntuación del 1 al 5 que ha recibido.
  - `body`: el cuerpo del vino en una escala del 1 al 5.
  - `acidity`: la acidez del vino en una escala del 1 al 5.
  - `description`: Un pequeño texto con los aspectos más destacables sobre el vino.
  - `food`: Una lista de comidas con las que se sugiere acompañar el vino.
  - `date`: la fecha de extracción de los datos del crawler.
  - `source`: en este caso siempre será carrefour.

### Datasets
Enlaces al repositorio Zenodo (DOI):
- 'wines_carrefour.csv'[https://zenodo.org/record/6429426]
- 'wines_vivino.csv'[https://zenodo.org/record/6429426]

## License
<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/mcaballero99/carrefour_crawler">Wine Crawler</a> by <span property="cc:attributionName">Marcos Caballero </span> is licensed under <a href="http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY-NC 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1"></a></p>
