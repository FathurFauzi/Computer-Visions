import cv2 as cv
import numpy as np

# 1. Tambahkan channel warna (3) agar Kuning muncul
layar = np.zeros((400, 400, 3), dtype="uint8")

graf = 1       # Kita kecilkan angkanya agar tidak terlalu cepat di layar
kecepatan = 0
y = 0
x=200
while True :
    layar.fill(0)
    tombol = cv.waitKey(20) & 0xFF # 20ms agar fps lebih stabil
    if tombol == 27: break
    
    if tombol == ord('d'):x+=3
    if tombol == ord('a'):x-=3
    # 2. Rumus Gravitasi (Kecepatan bertambah tiap tick)
    kecepatan += graf
    y += kecepatan
    
    # 3. Logika Pantulan (Bouncing)
    if y >= 300: # 300 karena radius elips kamu cukup besar (100px)
        y = 300
        kecepatan *= -0.7 # Memantul dan kehilangan energi (biar tidak mantul selamanya)
    
    if tombol == ord('n') and y>=300:
        y = 300
        kecepatan *= -100
    # 4. Gambar Elips (Center X kita geser ke 200 agar di tengah)
    # Warna (0, 255, 255) adalah Kuning dalam format BGR
    cv.ellipse(layar, (x, int(y)), (50, 100), 67, 45, 315, (0, 255, 255), -1)

    cv.imshow("Simulasi Gravitasi", layar)

    # Reset jika tekan Space
    if tombol == ord('z'):
        y = 0
        kecepatan = 0

    
cv.destroyAllWindows()