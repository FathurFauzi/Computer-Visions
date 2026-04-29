import cv2 as cv
import numpy as np
import math

layar = np.zeros((400, 400), dtype="uint8")
kemiringan = 0 
tengah = 200
amplitudo = 180 # Hampir full layar (200 ke atas, 200 ke bawah)

while True:
    layar.fill(0)
    tombol = cv.waitKey(0)
    if tombol == 27: break
    
    if tombol == ord('w'): kemiringan += 5
    elif tombol == ord('s'): kemiringan -= 5

    # 1. Hitung Fase Depan
    rad_depan = math.radians(kemiringan)
    y_depan = int(tengah + amplitudo * math.sin(rad_depan))
    
    # 2. Hitung Fase Belakang (Beda Fase 180 derajat / PI)
    rad_belakang = rad_depan - math.pi 
    y_belakang = int(tengah + amplitudo * math.sin(rad_belakang))

    # --- VISUALISASI HORIZON ---
    # Garis Depan (Putih Tebal)
    cv.line(layar, (50, y_depan), (350, y_depan), 255, 3)
    # Garis Belakang (Abu-abu Tipis)
    cv.line(layar, (80, y_belakang), (320, y_belakang), 100, 1)
    
    # Hubungkan keduanya untuk membuat efek "Plat" atau "Horizon"
    cv.line(layar, (50, y_depan), (80, y_belakang), 150, 1)
    cv.line(layar, (350, y_depan), (320, y_belakang), 150, 1)

    cv.putText(layar, f"Sudut: {kemiringan % 360} deg", (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.5, 255, 1)
    cv.imshow("Simulasi Horizon", layar)

cv.destroyAllWindows()