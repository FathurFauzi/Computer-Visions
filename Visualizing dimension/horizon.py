import cv2 as cv
import numpy as np

layar = np.zeros((400, 400), dtype="uint8")
pitch = 0 
# Konstanta ini mewakili (Tinggi Kamera * Focal Length)
# Makin besar angkanya, ubin lantai terlihat makin panjang/luas
KONSTANTA_PERSPEKTIF = 2500 

while True:
    layar.fill(0)
    
    tombol = cv.waitKey(10) 
    if tombol == 27: break
    
    # Kontrol Pitch (Mendongak/Menunduk)
    if tombol == ord('-'): KONSTANTA_PERSPEKTIF += 50  
    if tombol == ord('='): KONSTANTA_PERSPEKTIF -= 50  
    if tombol == ord('w'): pitch += 5 
    elif tombol == ord('s'): pitch -= 5

    # Posisi Horizon Dinamis
    horizon_y = 200 + pitch

    # --- GAMBAR GARIS HORIZONTAL (Z-Axis Only) ---
    # Kita loop z dari 1 (paling dekat dengan kaki) ke atas
    for z in range(1, 60):
        # Gunakan rumus pembagian terbalik (1/z)
        # Ingat logika -y kamu: y_cv = Horizon + (Konstanta / z)
        offset_y = KONSTANTA_PERSPEKTIF / z
        
        y = int(horizon_y + offset_y)
        
        # Gambar hanya jika garis berada di bawah horizon (Lantai nyata)
        # dan masih berada di dalam layar (0-400)
        if horizon_y < y < 400:
            # Efek atmosfer: makin jauh (z besar), garis makin redup
            kecerahan = int(max(40, 255 - (z * 4)))
            cv.line(layar, (0, y), (400, y), kecerahan, 1)

    # Garis Horizon Utama sebagai penanda ufuk
    if 0 <= horizon_y <= 400:
        cv.line(layar, (0, horizon_y), (400, horizon_y), 255, 2)

    cv.putText(layar, f"Horizon Y: {horizon_y}", (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.5, 255, 1)
    cv.imshow("Perspektif Garis Z", layar)

cv.destroyAllWindows()