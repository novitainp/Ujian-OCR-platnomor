import os
import csv
import base64
import requests
import re
from tools_ocr import hitung_cer, baca_label

# Konfigurasi LM Studio
API_URL = "http://localhost:1234/v1/chat/completions"
HEADERS = {"Content-Type": "application/json"}
MODEL = "llava-llama-3-8b-v1_1"

# Lokasi folder dan file
FOLDER_GAMBAR = "dataset/test"
FILE_LABEL = "data_label.csv"
FILE_HASIL = "hasil_proses.csv"

def encode_gambar(path):
    with open(path, "rb") as file:
        return base64.b64encode(file.read()).decode("utf-8")

def ambil_teks_plat(respon):
    kandidat = re.findall(r'[A-Z0-9]{4,10}', respon.upper())
    if kandidat:
        return kandidat[0]
    return "TIDAK_TERDETEKSI"

def kirim_ke_model(encoded_img):
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": [
                {"type": "text", "text": "What is the license plate number shown in this image? Respond only with the plate number."},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{encoded_img}"}}
            ]}
        ],
        "temperature": 0.2,
        "max_tokens": 100
    }

    try:
        response = requests.post(API_URL, headers=HEADERS, json=payload)
        isi = response.json()['choices'][0]['message']['content'].strip()
        return ambil_teks_plat(isi)
    except Exception as err:
        print(f"Error saat prediksi: {err}")
        return "GAGAL"

def jalan_program():
    print("Memulai proses OCR plat nomor...")
    data_label = baca_label(FILE_LABEL)

    with open(FILE_HASIL, mode='w', newline='', encoding='utf-8') as file:
        tulis = csv.writer(file)
        tulis.writerow(["nama_file", "label_asli", "hasil_prediksi", "nilai_CER"])

        for nama_file, label in data_label.items():
            path_gambar = os.path.join(FOLDER_GAMBAR, nama_file)
            if not os.path.exists(path_gambar):
                print(f"File tidak ditemukan: {nama_file}")
                continue

            print(f"Memproses: {nama_file}")
            encoded = encode_gambar(path_gambar)
            hasil_prediksi = kirim_ke_model(encoded)
            cer = hitung_cer(label, hasil_prediksi)

            print(f"{nama_file} | Asli: {label} | Prediksi: {hasil_prediksi} | CER: {cer:.2f}")
            print("-" * 60)

    print("Selesai. Laporan disimpan di:", FILE_HASIL)

if __name__ == "__main__":
    jalan_program()
