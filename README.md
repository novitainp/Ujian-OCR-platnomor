# OCR Plat Nomor Kendaraan – LM Studio

Proyek ini adalah tugas akhir mata kuliah **Computer Vision (AAS)**, dengan tujuan mengenali **plat nomor kendaraan** dari gambar menggunakan **Visual Language Model (VLM)** lewat bantuan **LM Studio**.

## Tools & Teknologi yang Dipakai

- Python 3.11
- LM Studio (`llava-llama-3-8b-v1_1`)
- Library Python: `requests`, `csv`, `base64`, `re`
- Format input: Gambar JPEG dari plat nomor kendaraan
- Output: File `hasil_proses.csv` yang berisi hasil prediksi & nilai evaluasi CER

## Cara Menjalankan Program

1. Jalankan **LM Studio**, pastikan model multimodal (`llava-llama-3-8b-v1_1`) sudah aktif.
2. Pastikan **API-nya aktif** di alamat: `http://localhost:1234`
3. Masukkan gambar plat nomor ke folder: `dataset/test/`
4. Jalankan perintah ini di terminal:

```bash
python main.py
