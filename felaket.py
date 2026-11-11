#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GÜNLÜK FELAKET TAHMİNCİSİ
Bu kod, evrenin en güvenilir (ve en gereksiz) felaket tahmin sistemidir.
Hiçbir sorumluluk kabul edilmez. Tahminler %100 doğrudur, %0.001 yanlış olabilir.
"""

import random
import datetime

felaketler = [
    "Bugün mikrodalganız size isyan edecek ve yemeğinizi pişirmeyi reddedecek. Beep sesi artık bir tehdit.",
    "Çoraplarınızdan biri paralel evrene kaçacak. Diğeri ise intikam planları yapacak.",
    "Kahve makineniz felsefi bir kriz geçirecek ve 'neden varım?' diye soracak.",
    "Buzdolabınız gece yarısı sürpriz bir şarkı söyleyecek. Komşular şikayet edecek.",
    "Tuvalet kağıdı rulosu sonsuzluğa ulaşacak ama siz hiçbir zaman sonuna erişemeyeceksiniz.",
    "Asansör bugün sadece aşağı inecek. Yukarı çıkmak için merdivenleri öğrenin.",
    "Bilgisayarınız klavye tuşlarını rastgele değiştirecek. 'A' tuşu artık 'Z' olacak. Hayat böyle.",
    "Hava durumu uygulaması size 'yağmur' diyecek ama aslında patlamış mısır yağacak.",
    "Saatiniz bir saat ileri gidecek ama siz geri kalacaksınız. Klasik zaman paradoksu.",
    "Bugün bir kedi size bakacak ve 'sen de mi?' diye düşünecek. Varoluşsal kriz garantili."
]

def tahmin_et():
    bugun = datetime.date.today()
    secilen = random.choice(felaketler)
    print(f"\n=== GÜNLÜK FELAKET TAHMİNİ ({bugun}) ===")
    print(f"Tahmin: {secilen}")
    print("\nBilimsel açıklama: Bu tahmin, kuantum çorap teorisi ve mikrodalga termodinamiği temel alınarak üretilmiştir.")
    print("Önlem: Derin nefes alın, çay demleyin ve felaketi kucaklayın.")
    print("\n---")
    print("İmza: Kayyum Grok | Tarih: 11.11.2026 | Damga: Bu kod resmi olarak 'Çalışıyor ama neden?' sertifikasını almıştır. Ciddiyet seviyesi: Aşırı ciddi ama gülünç.")

if __name__ == "__main__":
    tahmin_et()
    # Gizli not: Bazen en büyük felaket, her şeyin normal göründüğü anlardır. Sistem sorgulanmalıdır.
