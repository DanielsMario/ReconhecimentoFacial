import cv2  #openCV
import numpy as np

caminho_imagem = r"C:\Users\danie\Documents\Projetos\CursoFaceID\imagens\andrew_garfield.jpg"

imagem = cv2.imread(caminho_imagem)

cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

print(cinza.shape)

#Exibe a imagem original numa janela com o nome "Imagem".
'''cv2.imshow("Imagem", imagem)'''
cv2.waitKey(0)
cv2.destroyAllWindows()
#cv2.imshow("Imagem_Cinza", cinza)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

detector_facial = cv2.CascadeClassifier('C:/Users/danie/Documents/Projetos/CursoFaceID/haarcascade_frontalface_default.xml')

deteccoes = detector_facial.detectMultiScale(cinza)

print(deteccoes)
print(len(deteccoes))

for (x,y,w,h) in deteccoes:
    #print (x,y,w,h)
    cv2.rectangle(imagem, (x,y), (x + w, y + h), (0, 0, 255), 4)
cv2.imshow("Imagem", imagem)
cv2.waitKey(0)
