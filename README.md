# session-3
Treasure Island Adventure is a simple text-based interactive game built using Python. The player must make a series of decisions to find the hidden treasure. Each choice affects the outcome of the game.
# 🏝️ Treasure Island Adventure Game

## 📖 Overview

Treasure Island Adventure is a simple text-based interactive game built using Python.  
The player must make the correct decisions to find the hidden treasure. Each choice determines whether the player wins or loses the game.

This project is designed for beginners who are learning Python fundamentals and control flow logic.

---

## 🎮 How to Play

1. Run the Python script.
2. Follow the on-screen instructions.
3. Type your choices carefully (kiri, kanan, tunggu, berenang, merah, kuning, biru).
4. Make the correct decisions to win the treasure.

---

## 🧠 Concepts Used

- `if`, `elif`, `else` conditional statements
- Nested condition logic
- User input with `input()`
- String handling using `.lower()`
- Basic game flow structure

---

## 💻 Game Code

```python
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
```

---

## 🖥 Example Gameplay

```
Selamat datang di pulau Harta Karun!
Misi kamu adalah untuk menemukan Harta Karun.
Kamu ada di persimpangan jalan...
```

---

## 🛠 Requirements

- Python 3.x

---

## 👤 Author

Andrian Wijaya

---

## 📜 License

This project is created for educational purposes.
