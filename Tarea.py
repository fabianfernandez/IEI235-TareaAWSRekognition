import boto3
import time

def log(mensaje):
    FechayHora = time.strftime("%d-%m-%Y %H:%M:%S")
    print(FechayHora +" "+ mensaje)
    return

def compare_faces(sourceFile, targetFile):
    try:
        client=boto3.client('rekognition')
        s3 = boto3.resource('s3')
        bucket = s3.Bucket('iei235')
        bucket.download_file(sourceFile, 'Imagenes/'+sourceFile)
        bucket.download_file(targetFile, 'Imagenes/'+targetFile)
        imageSource=open('Imagenes/'+sourceFile,'rb')
        imageTarget=open('Imagenes/'+targetFile,'rb')
        response=client.compare_faces(SimilarityThreshold=80,
        SourceImage={'Bytes': imageSource.read()},TargetImage={'Bytes': imageTarget.read()})
        #print(response)
        for faceMatch in response['FaceMatches']:
            position = faceMatch['Face']['BoundingBox']
            similarity = str(faceMatch['Similarity'])
            log('INFO: La cara en la posicion:' + str(position['Left']) + ' ' + str(position['Top']) +
            ' tiene una similitud de: ' + similarity + '% de confianza')

        imageSource.close()
        imageTarget.close()
        return len(response['FaceMatches'])
    except Exception as e:
        log("ERROR: "+str(e))
        return 0

def main():
    source_file='luke_skywalker1.jpg'
    list_target_file=['Han_solo.jpg','luke_skywalker1.jpg','luke_skywalkerAdulto1.jpg','luke_skywalkerAdulto2.jpg',
    'luke_skywalkerCaricatura.jpg','luke_skywalkerEdadViejo.jpg','luke_skywalkerFormatoDistinto.bmp',
    'luke_skywalkerFormatoPng.png','luke_skywalkerMismaEdad.jpg','luke_skywalkerVideoJuegoRealista.jpg',
    'luke_junto_a_actor_diferente.jpg','ValorMinimoResolucion1.jpg','ValorMinimoResolucion2.jpg','ValorMaximoResolucion1.jpg','']
    for target_file in list_target_file:
        log("Entrada: imagen de entrada a comparar; "+ target_file)
        face_matches=compare_faces(source_file, target_file)
        log("Salida: cantidad de rostros similares encontrados: "+ str(face_matches))
if __name__ == "__main__":
    main()
