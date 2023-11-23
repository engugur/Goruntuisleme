import cv2
import numpy as np
import matplotlib.pyplot as plt

foto = cv2.imread("papatya.jpeg")
w, h = foto.shape[:2]
Hist = np.zeros(256, dtype=int)
for v in range(h):
    for u in range(w):
        i = foto[u, v]
        Hist[i] += 1
print(Hist)
