# Documentação do Projeto FaceID

## 1. Descrição
Este projeto utiliza a biblioteca OpenCV para reconhecimento facial em imagens estáticas. A detecção de rostos é realizada utilizando um classificador Haar Cascade, um modelo pré-treinado que identifica padrões de rostos em imagens.

---

## 2. Dependências
- Python 3.13
- OpenCV
- NumPy
- Modelo Haar Cascade (`haarcascade_frontalface_default.xml`)

Para instalar as dependências necessárias, execute:
```sh
pip install opencv-python numpy
```

---

## 3. Fluxo do Código

### 3.1. Carregamento da Imagem
```python
caminho_imagem = r"C:\Users\danie\Documents\Projetos\CursoFaceID\andrew_garfield.jpg"
imagem = cv2.imread(caminho_imagem)
```
- O caminho da imagem é definido utilizando uma **raw string** (`r"..."`) para evitar problemas com caracteres de escape (`\`).
- `cv2.imread()` carrega a imagem do caminho fornecido. Se o caminho estiver incorreto, `imagem` será `None`.

### 3.2. Conversão para Tons de Cinza
```python
cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
print(cinza.shape)
```
- A imagem é convertida para escala de cinza para reduzir a quantidade de pixels e melhorar a eficiência da detecção.
- `cv2.COLOR_BGR2GRAY` converte de **BGR** (formato padrão do OpenCV) para **tons de cinza**.
- O `print(cinza.shape)` exibe as dimensões da imagem convertida (altura, largura).

### 3.3. Exibição da Imagem
```python
cv2.imshow("Imagem", imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
- `cv2.imshow()` exibe a imagem original em uma janela.
- `cv2.waitKey(0)` faz com que o programa espere o usuário pressionar uma tecla antes de continuar.
- `cv2.destroyAllWindows()` fecha todas as janelas do OpenCV.

### 3.4. Detecção Facial
```python
detector_facial = cv2.CascadeClassifier('C:/Users/danie/Documents/Projetos/CursoFaceID/haarcascade_frontalface_default.xml')
deteccoes = detector_facial.detectMultiScale(cinza)
```
- O modelo Haar Cascade é carregado para identificar rostos na imagem.
- `detectMultiScale(cinza)` detecta rostos na imagem convertida para escala de cinza e retorna uma lista de coordenadas dos retângulos que envolvem os rostos detectados.

### 3.5. Saída da Detecção
```python
print(deteccoes)
print(len(deteccoes))
```
- Exibe as coordenadas `(x, y, largura, altura)` dos rostos detectados.
- Exibe o total de rostos identificados na imagem.

### 3.6. Desenho dos Retângulos nos Rostos Detectados
```python
for (x, y, w, h) in deteccoes:
    cv2.rectangle(imagem, (x, y), (x + w, y + h), (0, 255, 255), 4)
cv2.imshow("Imagem", imagem)
cv2.waitKey(0)
```
- Percorre a lista de detecções e desenha um **retângulo** amarelo ao redor de cada rosto detectado.
- O retângulo é definido por `(x, y)` (canto superior esquerdo) e `(x + w, y + h)` (canto inferior direito).
- `cv2.rectangle(imagem, (x,y), (x+w, y+h), (0,255,255), 4)`:
  - `(0, 255, 255)`: Cor amarela (BGR).
  - `4`: Espessura da linha do retângulo.

---

## 4. Como Executar o Código
1. Certifique-se de que o arquivo **haarcascade_frontalface_default.xml** está no local correto.
2. Execute o script Python:
   ```sh
   python main.py
   ```
3. A imagem será exibida com os rostos detectados em destaque.

---

## 5. Possíveis Problemas e Soluções
| Problema | Causa Provável | Solução |
|----------|---------------|----------|
| `NoneType` error ao carregar a imagem | Caminho da imagem está incorreto | Verifique se o arquivo existe e o caminho está correto |
| Nenhum rosto detectado | Iluminação ruim ou imagem desfocada | Teste com outra imagem ou ajuste os parâmetros de detecção |
| Erro no carregamento do Haar Cascade | Caminho do XML incorreto | Baixe o arquivo novamente do repositório do OpenCV |

---

## 6. Referências
- [Documentação do OpenCV](https://docs.opencv.org/)
- [Modelos Haar Cascade do OpenCV](https://github.com/opencv/opencv/tree/master/data/haarcascades)

---

### 📌 **Conclusão**
Este projeto demonstra como carregar imagens, convertê-las para escala de cinza e aplicar detecção facial utilizando o OpenCV. O modelo Haar Cascade permite identificar rostos em imagens estáticas de maneira eficiente.

