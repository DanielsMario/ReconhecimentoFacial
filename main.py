import cv2  #openCV
import numpy as np

#Agente treinado para Reconhecimento de face
detector_facial = cv2.CascadeClassifier('C:/Users/danie/Documents/Projetos/CursoFaceID/haarcascade_frontalface_default.xml')
#Detecta olhos
detector_olhos = cv2.CascadeClassifier('C:/Users/danie/Documents/Projetos/CursoFaceID/haarcascade_eye.xml')

#Armazenando a imagem em uma variavel
caminho_imagem = r"C:\Users\danie\Documents\Projetos\CursoFaceID\imagens\42dfaeb1-90bc-48f1-8af0-6f5eb7945fa4.jpg"

imagem = cv2.imread(caminho_imagem)
'''print(f"{imagem.shape} = 5.644.800 Px, Cor original com 3 canais de cores")'''
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)#convertendo do formato rgb para o cinza
'''print(f"{imagem_cinza.shape} = 1.881.600 Px, formato em escala de cinza 1 canal")'''


#percorre a imagem procurando uma Face
deteccoes = detector_olhos.detectMultiScale(imagem_cinza, scaleFactor=1.3, minNeighbors=4)
#scalefactor = 1.05 lento mas mais preciso 1.3 mais rapido mas menos preciso
#minNeighbors = número minimo de vizinhos que uma faze precisa ter, 3 mais falsos positivos / 5 menos falsos positivos
#minSize define o tamanho mínimo que um rosto pode ter para ser detectado.

#Mostra as possiveis faces da imagem com X,Y,W,H
for (x,y,w,h) in deteccoes:
    print(f"Póssiveis Faces (X-{x}) (Y-{y}) (W-{w}) (H-{h})")
    cv2.rectangle(imagem, (x, y), (x + w, y + h), (0, 255, 255), 3)

#mostrar a imagem com o reconhecimento do rosto
imagem_redimensionada = cv2.resize(imagem,(600, 400),3)
cv2.imshow("Imagem Redimencionada", imagem_redimensionada)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(f"Existem {len(deteccoes)} Possiveis Faces")#Retorna a quantidade de deteccoes de face na imagem
