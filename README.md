# IEI235-TareaAWSRekognition

## Descripción
Este programa consiste en una función llamada compare_faces en la cual se compara la similitud entre rostros de dos imagenes a traves de la utilización del servicio de AWS rekognition 'compare faces'. La función recibe dos parametros llamados `"sourceFile"` y `"targetFile"`. El parametro `"sourceFile"` consiste en el nombre de la imagen de control con rostros utilizada como imagen original y el parametro `"targetFile"` consiste en el nombre de una imagen con rostros para ser comparados con la imagen original. Dentro de la función se descargan las imagenes asociadas a los parametros desde el servicio S3 de AWS. Luego la funcion carga las imagenes en variables las cuales son ingresadas a la funcion `"compare_faces"` de AWS rekognition utilizando un porcentaje de confianza de un 80%. AWS rekognition retorna los resultados asociadas a la comparacion de rostros y la funcion compare_faces de python retorna el numero de rostros similares encontrados con al menos un 80% de similitud. En este codigo se compara una imagen con el nombre de `luke_skywalker1.jpg` con un conjunto de posibles imagenes de prueba para determinar la calidad del servicio de AWS rekognition.

## Tecnología:

- Python 3.9.5
- AWS rekognition
- AWS S3
- boto3

## Antes de empezar:

- Instalar python y pip
- Instalar boto3 utilizando el comando `pip boto3`
- Tener o crear una cuenta en AWS
- Crear un bucket en s3 con el nombre de `iei235`
- Subir las imagenes de la carpeta `Imagenes` a el bucket
- Editar o crear el archivo en la direccion `~/.aws/credentials` con:
```
[default]
aws_access_key_id = your_access_key_id
aws_secret_access_key = your_secret_access_key
```
- Para mas información seguir el tutorial de: https://docs.aws.amazon.com/rekognition/latest/dg/faces-comparefaces.html


## Instrucciones de uso

- Ejecutar en la terminal: "python Tarea.py" o utilizar algún IDE para ejecutar el .py
- Observar resultados en la terminal
