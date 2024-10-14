---
author: Syukron Alfarozi
header: Pengantar MLOps
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
<style>
img[alt~="center"] {
  display: block;
  margin: 0 auto;
}
</style>

# Pengantar MLOps

@2024

###### [Syukron Abu Ishaq Alfarozi](#)

![bg right 100%](https://i0.wp.com/neptune.ai/wp-content/uploads/2022/10/MLOps-DevOps.png?ssl=1)

---

![Profile Image](cv.jpg)

---
## Apa itu MLOps?

**MLOps (Machine Learning Operations)** adalah serangkaian praktik untuk merancang, menerapkan, dan memelihara pembelajaran mesin dalam produksi secara terus menerus, andal, dan efisien.

### Tahapan Pembelajaran Mesin

![alt text](image.png)

---

## Mengapa MLOps?

![](https://cloud.google.com/static/architecture/images/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning-1-elements-of-ml.png)

---

## Mengapa MLOps?

- Kolaborasi yang lebih baik antar tim
- Otomatisasi proses deployment
- Monitoring performa model di lingkungan produksi

![alt text](image-1.png)

---
## Apa itu MLOps
- ML + Dev + Ops = MLOps
- Kolaboratif dan eksperimental dalam sifatnya  
- Mengotomatisasi sebanyak mungkin 
- Perbaikan berkelanjutan dari Model ML 
- Standarisasi dan Skalakan

![alt text](image-2.png)

---
## Tahapan dalam MLOps

- **Perancangan**: Memahami konteks masalah dan menetapkan metrik utama
- **Pengembangan**: Pengembangan model ML, eksperimen, dan validasi
- **Penerapan dan Monitoring**: Implementasi model dalam sistem produksi serta pemantauan performa model dan siklus perbaikan

![alt text](image.png)

---
## MLOps LifeCycle

![alt text](image-3.png)

---
## Tahapan MLOps: Perancangan

- Memahami konteks masalah bisnis
- Menetapkan nilai tambah dari model ML
- Menentukan persyaratan bisnis
- Menetapkan metrik kunci yang perlu diukur

![bg right 70%](image-4.png)

---

## Tahapan MLOps: Pengembangan

- Melatih model dengan data yang tersedia
- Eksperimen dengan algoritma, parameter, dan arsitektur model
- Menyiapkan model yang siap untuk di-deploy

![bg right 70%](image-5.png)

---
## Tahapan MLOps: Penerapan dan Monitoring

- Mengintegrasikan model ke dalam sistem bisnis
- Men-deploy model ke lingkungan produksi
- Memastikan performa model dapat dipantau

![bg right 70%](image-6.png)

---

## Pemangku Kepentingan dalam MLOps

**Peran Bisnis:**

- Pemangku kepentingan bisnis: Penentu anggaran dan visi
- Pakar domain (*subject matter expert*): Pengetahuan mendalam tentang data dan validasi model

**Peran Teknis:**

- Data Scientist: Analisis data, pelatihan model
- Data Engineer: Pengumpulan, pemrosesan data
- ML Engineer: Memastikan seluruh siklus MLOps berjalan lancar

---

## Peran dalam ML Lifecycle

![alt text](image-7.png)

---
## ML lifecycle management

![alt text](image-8.png)

---

# MLOps LifeCycle: Perancangan

![w:800 center](image-10.png)

---

## Nilai Tambah dari MLOps

- ML adalah **eksperimental dan tidak pasti**
- Penting untuk **memperkirakan nilai yang diharapkan**
- Membantu dalam:
  - Alokasi sumber daya
  - Penentuan prioritas
  - Pengaturan ekspektasi

![](https://www.datocms-assets.com/2885/1620155106-mlops.png) <!-- Image Placeholder -->

---

## Persyaratan Bisnis

- Siapa **pengguna akhir** dari model ini?
- Seberapa cepat model harus berjalan (**kecepatan**)?
- Seberapa akurat (**akurasi**) hasil model?
- Seberapa transparan prosesnya (**transparansi**)?
- Apakah ada regulasi atau kepatuhan (**compliance**) yang harus dipatuhi?
- Apa **anggaran** dan **ukuran tim** yang tersedia?

![](https://miro.medium.com/max/1024/1*4L9b6Knl_nYZwRKP_TjfxQ.png) <!-- Image Placeholder -->

---
## Metrik Kunci

![w:800 center](image-9.png)

---

# Kualitas Data dan Proses Ingesti

![w:800 center](image-11.png)

---
### Apa itu kualitas data?
  - Ukuran seberapa baik data melayani tujuan yang dimaksudkan.

### Mengapa penting?
  - Kualitas data menentukan kualitas model ML.
  
### Dimensi Kualitas Data:
1. **Akurasi**: Apakah data benar?
2. **Kelengkapan**: Apakah ada data yang hilang?
3. **Konsistensi**: Apakah data sinkron di seluruh sistem?
4. **Ketepatan waktu**: Kapan data tersedia?

---
## Data Ingesti

![w:800 center](etl.png)

---

## Teknik Feature Engineering

- **Apa itu Feature Engineering?**
  - Proses memilih, memanipulasi, dan mengubah data mentah menjadi **fitur** yang digunakan oleh model ML.
  
- **Tujuan**: Meningkatkan performa model dengan memanfaatkan fitur yang relevan.

### Contoh Teknik:
- **Seleksi Fitur**: Memilih fitur yang paling relevan.
- **Feature Store**: Menyimpan dan berbagi fitur yang digunakan di berbagai proyek.
- **Kontrol Versi Data**: Melacak perubahan data untuk menjaga konsistensi.

---

## Pelacakan Eksperimen

- **Mengapa pelacakan eksperimen penting?**
  - Untuk **membandingkan hasil** dari berbagai eksperimen.
  - Memungkinkan **reproduksi eksperimen** di masa depan.
  - Berkolaborasi dengan tim dan melaporkan hasil kepada **pemangku kepentingan**.

  ![w:500 center](0_nowh44j3Oi6NGlBf.webp)

---

### Proses Eksperimen ML:
1. Merumuskan hipotesis.
2. Mengumpulkan data.
3. Mendefinisikan eksperimen.
4. Menyiapkan pelacakan eksperimen.
5. Melatih model.
6. Menguji model dengan test set.
7. Mendaftarkan model terbaik.
8. Visualisasi dan pelaporan hasil.

![bg right 100%](mlflow.jpg)

---

# Monitoring dalam MLOps

Monitoring adalah komponen krusial dalam MLOps untuk memastikan model ML berfungsi dengan baik setelah deployment. Dua fenomena penting yang perlu diperhatikan adalah **Concept Drift** dan **Data Drift**.

---

## Apa itu Concept Drift?

**Concept Drift** terjadi ketika hubungan antara fitur dan target dalam data berubah seiring waktu. Ini dapat menyebabkan model yang sebelumnya akurat menjadi kurang efektif.

![bg w:500 right](image-15.png)

---
### Penyebab Concept Drift:
- Perubahan dalam perilaku pengguna
- Perubahan kondisi pasar
- Pembaruan kebijakan atau regulasi

### Dampak:
- Penurunan akurasi model
- Model menjadi tidak relevan
- Meningkatkan risiko keputusan yang salah

---

## Apa itu Data Drift?

**Data Drift** adalah perubahan dalam distribusi data input yang digunakan oleh model ML, yang dapat mempengaruhi performa model. Meskipun target tetap sama, fitur yang diumpankan ke model berubah.

![bg h:500 right](image-14.png)

---
### Penyebab Data Drift:
- Perubahan cara data dikumpulkan
- Perubahan dalam populasi data
- Musim atau faktor eksternal lainnya

### Dampak:
- Model tidak dapat menangkap pola yang relevan
- Penurunan performa model dalam memberikan prediksi yang akurat

![](https://miro.medium.com/max/700/1*d1MaQuGHDNjbwSP9yATyGQ.png)

---

## Monitoring untuk Mengatasi Drift

### Teknik Monitoring:
- **Statistik Deskriptif**: Memantau statistik data input dan output untuk mendeteksi perubahan.
- **Visualisasi Data**: Menggunakan grafik untuk melihat distribusi data dan perubahan seiring waktu.
- **Model Performance Tracking**: Memantau metrik performa model untuk mendeteksi penurunan akurasi.

---

# Containerization dalam MLOps

Containerization adalah metode yang memungkinkan aplikasi (termasuk model machine learning) untuk dijalankan dalam lingkungan yang terisolasi dan konsisten, yang dikenal sebagai **container**.

![bg right w:500](1_bZP17SmwRZihfAYDr5KBFg.png)

---

## Apa itu Containerization?

- **Containerization** adalah teknik virtualisasi ringan yang membungkus aplikasi dan semua dependensinya ke dalam satu unit yang dapat dijalankan secara konsisten di berbagai lingkungan.
- Container dapat dibangun dan dikelola menggunakan alat seperti **Docker**.

### Keuntungan Containerization:
- **Portabilitas**: Aplikasi dapat dipindahkan antara lingkungan pengembangan, pengujian, dan produksi tanpa masalah.
- **Isolasi**: Mengurangi konflik antara dependensi aplikasi yang berbeda.
- **Skalabilitas**: Memudahkan pengelolaan skala aplikasi dalam lingkungan cloud.

![](https://www.docker.com/sites/default/files/just_one_thing.png)

---

## Proses Deployment dengan Containerization

1. **Pengembangan Model**: Model machine learning dikembangkan dan dilatih di lingkungan lokal.
2. **Membuat Dockerfile**: Menulis Dockerfile untuk mendefinisikan bagaimana image container akan dibangun.
3. **Build Image**: Menggunakan Docker untuk membuat image dari Dockerfile.
4. **Deploy Container**: Menjalankan container dari image di lingkungan produksi.
5. **Monitoring dan Scaling**: Memantau performa container dan menskalakan sesuai kebutuhan.
---
### Contoh Dockerfile:

```dockerfile
# Gunakan base image dari Python
FROM python:3.8

# Set direktori kerja
WORKDIR /app

# Salin file requirements
COPY requirements.txt .

# Install dependensi
RUN pip install -r requirements.txt

# Salin sisa kode aplikasi
COPY . .

# Jalankan aplikasi
CMD ["python", "app.py"]
```

---
# MLOps LifeCycle: CI/CD

![w:10000](https://cloud.google.com/static/architecture/images/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning-2-manual-ml.svg)

---

## Apa itu CI/CD?

- **CI (Continuous Integration)**: Proses otomatis yang mengintegrasikan perubahan kode secara terus menerus ke dalam repository.
- **CD (Continuous Delivery/Deployment)**: Otomatisasi untuk mengirim perubahan kode (dan model ML) ke lingkungan produksi dengan aman dan cepat.

---

## Mengapa CI/CD Penting dalam MLOps?

- **Otomatisasi**: Mengurangi kesalahan manual dalam deploy model ML.
- **Skalabilitas**: Memungkinkan deployment skala besar dengan cepat.
- **Keandalan**: Meningkatkan kepercayaan tim terhadap kode dan model yang dideploy.
- **Iterasi Cepat**: Memungkinkan pengujian dan pengiriman model lebih cepat ke pengguna.

![](https://about.gitlab.com/images/ci_cd/ci_cd_pipeline.jpg)

---

## Proses CI/CD dalam MLOps

1. **Continuous Integration (CI)**
   - Validasi kode dan model secara otomatis.
   - Melakukan linting, testing unit, dan validasi data.
   - Menyimpan dan melacak versi model.

2. **Continuous Delivery (CD)**
   - Deploy model secara otomatis ke staging environment.
   - Pengujian performa model di environment yang mirip dengan produksi.

3. **Continuous Deployment**
   - Deployment model langsung ke produksi setelah semua tahap pengujian.
   - Pemantauan performa model di lingkungan produksi.

---

## Pipeline CI/CD dalam MLOps

### Contoh Pipeline CI/CD untuk Machine Learning:

1. **Pengumpulan Data**: Data Engineer mengupdate dataset.
2. **Training Model**: Model dilatih dengan data baru.
3. **Validasi Model**: Model diuji dengan data test dan dilihat apakah performa meningkat.
4. **Deploy ke Staging**: Model dideploy ke staging untuk pengujian performa lebih lanjut.
5. **Deploy ke Produksi**: Setelah lulus uji, model dideploy ke produksi.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*89Pf5nKluc4Ceqn9TL9eSg.png)

---

## Tools untuk CI/CD dalam MLOps

- **GitHub Actions**: Platform CI/CD yang memungkinkan otomatisasi build, test, dan deployment langsung dari repositori GitHub.
- **GitLab CI/CD**: Platform terintegrasi untuk CI/CD pipeline.
- **Jenkins**: Otomatisasi open-source yang populer untuk CI/CD.
- **Kubeflow**: Platform MLOps untuk otomatisasi pipeline ML.
- **MLflow**: Alat pelacakan eksperimen, penyimpanan model, dan deployment.

![](https://miro.medium.com/max/700/0*bmF0WBcAZVp5bi1T.png)

---

## Tantangan dalam Implementasi CI/CD di MLOps

- **Pengelolaan Data**: Menjaga konsistensi dan kualitas data selama pengembangan.
- **Otomatisasi Model**: Membuat pipeline yang dapat menangani eksperimen model dengan berbagai hyperparameter.
- **Pengujian Model**: Berbeda dengan pengujian aplikasi biasa karena melibatkan performa prediksi.
- **Skalabilitas**: Mengelola pipeline untuk berbagai proyek dengan dataset besar.

---
## Strategi Deployment
![w:1000 center](image-12.png)

---
## MLOps Maturity

![alt text](image-13.png)

---

## Referensi
1. https://hktw-resources.awscloud.com/webinar-slides/introduction-to-mlops
2. https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning
3. https://www.datacamp.com/courses/mlops-concepts
