print("Selamat datang di pulau Harta Karun!")
print("Misi kamu adalah untuk menemukan Harta Karun.")
pilihan_1 = input("Kamu ada di persimpangan jalan, kemana kamu akan pergi? ketik 'kiri' atau 'kanan' .").lower()

if pilihan_1 == "kiri":
    pilihan_2 = input("Kamu menemukan sungai, di tengah tengah sungai itu ada pulau."
                      " ketik 'tunggu' untuk menunggu perahu, ketik'berenang' untuk berenang").lower()
    if pilihan_2 == "tunggu":
        pilihan_3 = input("Kamu tiba di pulau ini tanpa terluka."
                          " Disana ada rumah dengan 3 pintu, ada merah, kuning, dan biru, warna apa yang akan kamu pilih? ").lower()
        if pilihan_3 == "merah":
            print("Ruangan ini terisi dengan api. Game Over!")
        elif pilihan_3 == "kuning":
            print("Kamu Menemukan Harta Karunnya!. Kamu Menang!!!")
        elif pilihan_3 == "biru":
            print("Kamu masuk ke ruangan ini dan dimakan hewan buas. Game Over!")
        else:
            print("Kamu memilih pintu yang tidak ada. Game Over!")
    else:
        print("Kamu diserang oleh buaya yang lapar! Game Over!")
else:
    print("Kamu Terjun ke jurang. Game Over!")
