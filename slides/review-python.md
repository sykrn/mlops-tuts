---
author: Syukron Alfarozi
header: Python Programming 
footer: Syukron Abu Ishaq Alfarozi - DTETI FT UGM
paginate: true
marp: true
theme: default
math: mathjax
# class: invert

---
<!--
marpit
theme: gaia
class: lead
style: |
  section {
    display: flex;
    justify-content: space-between;
  }
  .left, .right {
    width: 48%;
  }
-->

<style>
    section {
        background-image: url("Ch-01/LogoUGM.jpg");
        background-repeat: no-repeat;
        background-position: right top;
        background-size:  100px;
        }
</style>


# **Review Pemrograman Python**
### Syukron Abu Ishaq Alfarozi, S.T., Ph.D.


---

![Profile Image](cv.jpg)

---

## **Pengenalan Python**

- Bahasa pemrograman populer, mudah dipelajari.
- Sintaks sederhana, interpretatif (tanpa kompilasi).
- Multi-paradigma: OOP, fungsional, prosedural.
- Komunitas besar dan banyak library.

---

## **Variabel dan Tipe Data**

- Variabel: Menyimpan nilai.
- **Tipe Data**:
  - **int**: Bilangan bulat (contoh: `5`)
  - **float**: Bilangan desimal (contoh: `3.14`)
  - **str**: String/teks (contoh: `"Python"`)
  - **bool**: True/False (contoh: `True`)

---

## **Operator**

- **Aritmatika**: `+`, `-`, `*`, `/`
- **Perbandingan**: `==`, `!=`, `>`, `<`
- **Logika**: `and`, `or`, `not`
- **Penugasan**: `=`, `+=`, `-=`

---

## **Struktur Data Python**

- **List**: Kumpulan elemen yang mutable (contoh: `[1, 2, 3]`)
- **Tuple**: Kumpulan elemen yang immutable (contoh: `(1, 2, 3)`)
- **Dictionary**: Kumpulan key-value (contoh: `{"name": "John", "age": 25}`)
- **Set**: Kumpulan elemen unik (contoh: `{1, 2, 3}`)

---

## **Control Flow (Alur Kontrol)**

- **If-Else**: Percabangan logika.
  ```python
  if x > 0:
      print("Positif")
  else:
      print("Negatif")
  ```
- **Looping**:
  - **For loop**: `for i in range(5):`
  - **While loop**: `while x < 5:`

---

## **Fungsi Input/Output (I/O)**

- **Input**: Mengambil data dari pengguna.
  ```python
  name = input("Enter your name: ")
  print(f"Hello, {name}!")
  ```
- **Output**: Menampilkan data.
  ```python
  print("Hello, World!")
  ```

---

## **Fungsi**

- Blok kode yang dapat digunakan ulang.
- Mendukung parameter dan return value.
  ```python
  def greet(name):
      return f"Hello, {name}!"
  print(greet("Alice"))
  ```

---

## **File Handling**

- Membuka, membaca, menulis file.
  ```python
  with open('file.txt', 'r') as file:
      content = file.read()
  print(content)
  ```
- **Mode**: `r` (baca), `w` (tulis), `a` (append).

---

# **Kesimpulan**

- Python mudah dipelajari dengan sintaks sederhana.
- Mendukung berbagai tipe data, struktur kontrol, dan fungsi.
- Cocok untuk berbagai aplikasi: web, data, dan otomasi.
