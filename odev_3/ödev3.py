import cv2
import numpy as np

def pirinc_say(goruntu):
    gri = cv2.cvtColor(goruntu, cv2.COLOR_BGR2GRAY)

    # Gürültüyü azaltmak için bulanıklaştırma uygula
    bulanık = cv2.GaussianBlur(gri, (5, 5), 0)

    # Kenarları tespit etmek için Canny kenar dedektörünü kullan
    kenarlar = cv2.Canny(bulanık, 0, 50)

    # Morfolojik işlemler uygula (aşındırma ve genişletme)
    kernel = np.ones((5, 5), np.uint8)
    kenarlar = cv2.morphologyEx(kenarlar, cv2.MORPH_CLOSE, kernel)

    # sayac (sınırlayıcı çizgi) tespiti yap
    sayac, _ = cv2.findContours(kenarlar, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Pirinç sayısı
    cekırdek_sayisi = len(sayac)

    # Konturları çiz(yeşil)
    cv2.drawContours(goruntu, sayac, -1, (0, 0, 255), 2)

    # Pirinç sayısını ekrana yazdır
    cv2.putText(goruntu, f"Cekirdek Sayisi: {cekırdek_sayisi}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    return goruntu

# Web kamera bağlantısını başlat
cap = cv2.VideoCapture(0)

while True:
    # Kameradan bir frame al
    ret, goruntu = cap.read()

    # Pirinç sayımı fonksiyonunu çağır
    fonk = pirinc_say(goruntu)

    # Görüntüyü ekrana göster
    cv2.imshow('Web Kamera - Pirinç Sayımı', fonk)

    # Çıkış için 'q' tuşuna basın
    if cv2.waitKey(1) & 0xFF == ord(' '):
        break


cap.release()
cv2.destroyAllWindows()