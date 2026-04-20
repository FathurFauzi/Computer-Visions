import cv2
import numpy as np

# 1. Siapkan "Kamus"
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)

# 2. Setup ArucoDetector untuk OpenCV versi 4.7.0+
parameters = cv2.aruco.DetectorParameters()
detector = cv2.aruco.ArucoDetector(aruco_dict, parameters)

# 3. Nyalakan Kamera
cap = cv2.VideoCapture(0)

print("Kamera menyala. Tekan 'q' pada keyboard untuk keluar.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Gagal membaca kamera.")
        break

    # 4. Ubah ke Grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 5. Deteksi Marker menggunakan format baru
    corners, ids, rejectedImgPoints = detector.detectMarkers(gray)

    # 6. Jika ada marker terdeteksi
    if ids is not None:
        cv2.aruco.drawDetectedMarkers(frame, corners, ids)
        
        # Ambil koordinat pojok marker pertama
        titik_pojok = corners[0][0] 
        kiri_atas = titik_pojok[0]
        kanan_atas = titik_pojok[1]

        # Hitung lebar dalam piksel
        lebar_piksel = np.linalg.norm(kanan_atas - kiri_atas)

        # Tampilkan teks
        teks = f"Lebar: {lebar_piksel:.2f} px"
        jarak = f"jarak: {21840/lebar_piksel:.2f} mM"
        x_teks, y_teks = int(kiri_atas[0]), int(kiri_atas[1]) - 15
        x_mili, y_mili = int(kiri_atas[0]), int(kiri_atas[1]) - 30
        cv2.circle(frame,(int(50+kiri_atas[0]),int(kiri_atas[1]+50)), int(lebar_piksel/2), (0,0,255), 2)
        cv2.putText(frame, teks, (x_teks, y_teks), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        cv2.putText(frame, jarak, (x_mili, y_mili), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    cv2.imshow('Prototipe Pengukur Dimensi', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()