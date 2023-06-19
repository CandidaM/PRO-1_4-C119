# 1. Carregue o vídeo.
# 2. Inicie o rastreador (o algoritmo embutido no OpenCV).
# 3. Selecione o objeto criando uma caixa delimitadora ao redor do objeto usando o mouse.
# 4. Obtenha o ponto central da caixa delimitadora.
# 5. Trace a trajetória usando pontos centrais


import cv2
import time
import math

p1 = 530
p2 = 300

xs = []
ys = []

video = cv2.VideoCapture("bb3.mp4")

# Carregue o rastreador
tracker = cv2.TrackerCSRT_create()

# Leia o primeiro quadro do vídeo
returned, img = video.read()

# Selecione a caixa delimitadora na imagem (region of interest)
bbox = cv2.selectROI("Rastreando", img, False)

# Inicialize o rastreador em img e na caixa delimitadora
tracker.init(img, bbox)

print(bbox)


def drawBox(img, bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])

    cv2.rectangle(img, (x, y), ((x + w), (y + h)), (255, 0, 255), 3, 1)

    cv2.putText(img, "Rastreando", (75, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)


