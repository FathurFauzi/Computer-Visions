import cv2
import numpy as np

# 1. Siapkan "Kamus"
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)

# 2. Setup ArucoDetector untuk OpenCV versi 4.7.0+
parameters = cv2.aruco.DetectorParameters()
detector = cv2.aruco.ArucoDetector(aruco_dict, parameters)

# --- [BARU] 3. Setup Kamera Matrix Dummy & Data 3D ---
# Ini syarat wajib agar OpenCV bisa membayangkan ruang 3D
focal_length = 484.55  # Asumsi fokus lensa standar webcam
camera_matrix = np.array([[focal_length, 0, 320.0],   # 320 adalah nilai tengah dari resolusi layar 640
                          [0, focal_length, 240.0],   # 240 adalah nilai tengah dari resolusi layar 480
                          [0, 0, 1]], dtype=np.float32)
dist_coeffs = np.zeros((4,1)) # Asumsi lensa datar (tidak cembung seperti fisheye)

# Ukuran asli marker di dunia nyata (misal: 10 cm = 0.1 meter)
marker_length = 0.091
# Koordinat 3D keempat sudut marker di "Dunia Nyata" (Z selalu 0 karena kertas itu datar)
obj_points = np.array([
    [-marker_length/2,  marker_length/2, 0],
    [ marker_length/2,  marker_length/2, 0],
    [ marker_length/2, -marker_length/2, 0],
    [-marker_length/2, -marker_length/2, 0]
], dtype=np.float32)
# -----------------------------------------------------

# 4. Nyalakan Kamera
cap = cv2.VideoCapture(0)
print("Kamera menyala. Tekan 'q' pada keyboard untuk keluar.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Gagal membaca kamera.")
        break

    # 5. Ubah ke Grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 6. Deteksi Marker
    corners, ids, rejectedImgPoints = detector.detectMarkers(gray)

    # 7. Jika ada marker terdeteksi
    if ids is not None:
        cv2.aruco.drawDetectedMarkers(frame, corners, ids)
        
        # [DIPERBAIKI] Menggunakan loop agar aman jika ada lebih dari 1 marker
        for i in range(len(ids)):
            titik_pojok = corners[i][0] 
            kiri_atas = titik_pojok[0]
            kanan_atas = titik_pojok[1]
            kanan_bawah = titik_pojok[2] # [BARU] Ambil kanan bawah untuk cari titik tengah
            
            # Hitung lebar dalam piksel
            lebar_piksel = np.linalg.norm(kanan_atas - kiri_atas)
            distance = focal_length*marker_length*100/lebar_piksel

            if distance <19.0:
                #draw a green rectangle from (21,67) to (300,300) with thickness of 3 px 
                cv2.rectangle(frame,(81,40),(400,600),(0,0,255),-3)
                cv2.putText(frame, "Too Close!!!", (200, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
                break
                
            # [DIPERBAIKI] Mencari pusat lingkaran tanpa bitwise (>>). 
            # Cukup jumlahkan ujung kiri atas dan kanan bawah, lalu bagi 2.
            pusat_x = int((kiri_atas[0] + kanan_bawah[0]) / 2)
            pusat_y = int((kiri_atas[1] + kanan_bawah[1]) / 2)

            # Tampilkan teks
            teks = f"pixel_wide: {lebar_piksel:.2f} px"
            jarak = f"distance: {distance:.3f} cm"
            x_teks, y_teks = int(kiri_atas[0]), int(kiri_atas[1]) - 15
            x_mili, y_mili = int(kiri_atas[0]), int(kiri_atas[1]) - 30
            
            # [DIPERBAIKI] Menggambar lingkaran persis di tengah marker
            cv2.circle(frame, (pusat_x, pusat_y), int(lebar_piksel/2), (0,0,255), 2)
            cv2.putText(frame, teks, (x_teks, y_teks), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
            cv2.putText(frame, jarak, (x_mili, y_mili), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

            # --- [BARU] INTI DARI KEMIRINGAN (POSE ESTIMATION) ---
            # solvePnP mencocokkan koordinat 3D (obj_points) dengan koordinat 2D di layar (titik_pojok)
            success, rvec, tvec = cv2.solvePnP(obj_points, titik_pojok, camera_matrix, dist_coeffs)
            
            if success:
                # Menggambar sumbu XYZ (Merah, Hijau, Biru) yang akan ikut miring!
                # Panjang garis sumbu diset ke 0.05 meter (5 cm)
                cv2.drawFrameAxes(frame, camera_matrix, dist_coeffs, rvec, tvec, 0.05)
            # -----------------------------------------------------

    cv2.imshow('Prototipe Safety System (Jarak & Kemiringan)', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()