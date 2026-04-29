import cv2 as cv
import numpy as np

# Inisialisasi layar
layar = np.zeros((400, 400), dtype="uint8")
kemiringan = 200  # Mulai dari tengah layar (Y-axis)
font = cv.FONT_HERSHEY_SIMPLEX

print("Tekan 'w' untuk ke atas, 'a' untuk ke bawah. 'Esc' untuk keluar.")

while True:
    layar.fill(0) # Bersihkan dulu
    
    # 1. Hitung logika (pindahkan waitKey ke atas)
    tombol = cv.waitKey(0) 
    if tombol == 27: break
    
    if tombol == ord('w'):
        kemiringan -= 10
    elif tombol == ord('s'):
        kemiringan += 10
    
    kemiringan = np.clip(kemiringan, 50, 350)

    # 2. Gambar semua yang mau ditampilkan
    cv.putText(layar, f"Posisi Y: {kemiringan}", (10, 30), font, 0.5, 255, 1)
    
    try:
        char_tombol = chr(tombol) if 32 <= tombol <= 126 else "?"
        cv.putText(layar, char_tombol, (180, kemiringan), font, 2, 255, 5)
    except:
        pass

    # 3. BARU TAMPILKAN (Jendela akan update dengan posisi terbaru)
    cv.imshow("Detektif Tombol", layar)
cv.destroyAllWindows()