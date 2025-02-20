#pip install pandas numpy matplotlib seaborn
import pandas as pd # Veri analizi için
import numpy as np # Sayısal işlemler için
import matplotlib.pyplot as plt # Grafik çizmek için
import seaborn as sns # Daha güzel grafikler için

from veribilimi.veri_gorsellestirme_ve_analizi import df_numeric

data = {
    "Ad": ["Ali", "Ayşe", "Mehmet", "Zeynep", "Can", "Fatma", "Murat", "Elif", "Ahmet", "Deniz"],
    "Yaş": [25, 30, 35, np.nan, 22, 40, 50, 28, np.nan, 32],
    "Maaş": [5000, 7000, 9000, 11000, 4000, 15000, 20000, np.nan, 7500, 9200],
    "Cinsiyet": ["Erkek", "Kadın", "Erkek", "Kadın", "Erkek", "Kadın", "Erkek", "Kadın", "Erkek", "Kadın"]
}

df = pd.DataFrame(data)  # Veriyi DataFrame'e dönüştür


#1. Veri Keşfi için Fonksiyonel Analizler

def genel_bilgi(df):
    print(df.head())
    print(df.info())
    print(df.isnull().sum())

genel_bilgi(df)


#2. Sayısal Değişkenler için Temel İstatistikler

def sayisal_istatistikler(df):
    print(df.describe())

sayisal_istatistikler(df)

#3. Kategorik Değişkenlerin Dağılımı

def kategorik_ozet(df):
    kategorik_sutunlar = df.select_dtypes(include=["object"]).columns
    for sutun in kategorik_sutunlar:
        print(df[sutun].value_counts())

kategorik_ozet(df)


#4. Eksik Verileri Görselleştirme

def eksik_veri_gorsel(df):
    plt.figure(figsize=(8,5))
    sns.heatmap(df.isnull(), cbar=False, cmap="viridis")
    plt.title("Eksik Veri Haritası")
    plt.show()

eksik_veri_gorsel(df)


#5. Sayısal Değişkenlerin Histogram Grafikleri

def histogram_gorsel(df):
    df_numeric = df.select_dtypes(include=["number"])
    df_numeric.hist(figsize=(10,5), bins=10, color="skyblue", edgecolor="black")
    plt.suptitle("Sayısal değişkenlerin dağılımı")
    plt.show()

histogram_gorsel(df)



#6. Korelasyon Matrisi ve Isı Haritası

def korelasyon_haritasi(df):
    df_numeric = df.select_dtypes(include=["number"])
    plt.figure(figsize=(6,4))
    sns.heatmap(df_numeric.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
    plt.title("📌 Korelasyon Matrisi")
    plt.show()

korelasyon_haritasi(df)


























