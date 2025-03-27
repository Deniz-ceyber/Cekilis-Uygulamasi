# Çekiliş Uygulaması
import random

kişiler = ["Ali", "Veli", "Mehmet", "Ayşe", "Deniz", "Sevde"]

# Çekiliş sayısı
çekiliş_sayisi = 1

def raskele_kisi():
    # Kişiler listesini karıştır
    random.shuffle(kişiler)
    for i in range(çekiliş_sayisi):
        kazanan = random.choice(kişiler)
        # Kullanıcıdan tahmin alın
        kullanici_tahmin = input("Tahminizi Giriniz! ").strip().lower()
        # Kazanan ile kullanıcı tahmini karşılaştır
        if kazanan.lower() == kullanici_tahmin:
            print("Doğru tahmin ettiniz")
        else:
            print(f"Yanlış tahmin\nDoğrusu {kazanan}")
            print("Tekrar Deneyiniz...")

def kisi_ekle():
    yeni_kisi = input("Eklemek istediğiniz kişinin adını girin: ").strip()
    if yeni_kisi:
        kişiler.append(yeni_kisi)
        print(f"{yeni_kisi} listeye eklendi.")
    else:
        print("Geçersiz giriş!")

def listeyi_goster():
    print("Mevcut kişiler listesi:")
    for kisi in kişiler:
        print(kisi)

def ana_menu():
    while True:
        print("\n--- Ana Menü ---")
        print("1. Çekiliş Yap")
        print("2. Yeni Kişi Ekle")
        print("3. Kişiler Listesini Göster")
        print("4. Çıkış")
        secim = input("Seçiminiz (1/2/3/4): ")

        if secim == '1':
            raskele_kisi()
        elif secim == '2':
            kisi_ekle()
        elif secim == '3':
            listeyi_goster()
        elif secim == '4':
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")

ana_menu()