import csv
import editdistance

def baca_label(path_csv):
    data = {}
    with open(path_csv, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data[row['image']] = row['ground_truth']
    return data

def hitung_cer(asli, prediksi):
    selisih = editdistance.eval(asli, prediksi)
    return selisih / max(1, len(asli))
