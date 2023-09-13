## Tugas 2

**Nama    : Cheeryl Aisyah Retnowibowo**

**NPM     : 2206813706**

**Kelas   : PBP C**

# *Stock Els*

## Link Adaptable: [Stock Els](https://stock-els.adaptable.app)

===========================================

### 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- [x] **Membuat sebuah proyek Django baru.**
    
    Diawali dengan pembuatan direktori lokal dengan nama sesuai dengan aplikasi yang diinginkan, yaitu `stock_els`. Setelah itu, buat dan aktifkan *virtual environment* pada direktori yang sama dengan tujuan agar *package* dan *dependencies* tidak bertabrakan dengan proyek lainnya dengan menggunakan perintah berikut:
    ```
    python -m venv env
    ```
    ```
    env\Scripts\activate.bat
    ```
    Langkah selanjutnya adalah buat file `requirements.txt`, tambahkan dan *install* *dependencies* tersebut.
    ```
    pip install -r requirements.txt
    ```
    Untuk membuat sebuah proyek Django, jalankan perintah berikut:
    ```
    django-admin startproject stock_els .
    ```
    Konfigurasi proyek dengan menetapkan nilai `["*"]` pada `ALLOWED_HOSTS` di file `settings.py` dengan tujuan agar kita terdaftar sebagai *host* yang diizinkan untuk mengakses aplikasi web. Sebagai tambahan, untuk mengabaikan berkas dan direktori yang tidak diperlukan, buat *file* `.gitignore`.

- [x] **Membuat aplikasi dengan nama `main` pada proyek tersebut.**
    
    Untuk membuat aplikasi dengan nama `main` pada *folder* utama, jalankan perintah berikut:
    ```
    python manage.py startapp main
    ```

- [x]  **Melakukan routing pada proyek agar dapat menjalankan aplikasi `main`.**
    
    Setelah terbentuk *folder* baru dengan nama `main` di dalam *folder* utama `stock_els` , tambahkan `main` pada variabel `INSTALLED_APPS` dalam *file* `settings.py` sehingga proyek dapat mendaftarkan dan menjalankan aplikasi `main`.

- [x]  **Membuat model pada aplikasi `main` dengan nama `Item` dan memiliki atribut wajib sebagai berikut.**
    * `name` sebagai nama item dengan tipe `CharField`.
    * `amount` sebagai jumlah item dengan tipe `IntegerField`.
    * `description` sebagai deskripsi item dengan tipe `TextField`.
    
    Pembuatan model tersebut dilakukan dengan menambahkan atribut tersebut dan atribut lain yang diinginkan beserta tipe datanya yang sesuai pada *file* `models.py` di dalam *folder* aplikasi `main`.
    Jika melakukan perubahan model, lakukan migrasi model agar Django dapat mengetahui adanya perubahan pada model basis data dengan menjalankan perintah `python manage.py makemigrations`, lalu diikuti dengan perintah `python manage.py migrate`.

- [x] **Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.**
    
    Untuk melakukan langkah ini, buka *file* `views.py` pada *folder* aplikasi `main` dan tambahkan baris impor `from django.shortcuts import render` untuk mengimpor fungsi *render* yang digunakan untuk me-*render* tampilan HTML dengan data yang diberikan. Selain itu, tambahkan pula fungsi `show_main` yang diisi dengan nama, npm, dan kelas. Di akhir baris, tambahkan kode `return render(request, "main.html", context)` untuk me-*render* tampilan `main.html` dengan menggunakan fungsi `render`.

- [x] **Membuat sebuah routing pada `urls.py` aplikasi `main` untuk memetakan fungsi yang telah dibuat pada `views.py`.**
    
    Pembuatan *routing* pada `urls.py` aplikasi `main` dilakukan dengan pembuatan *file* `urls.py` dalam *folder* `main`. Setelah itu, lakukan impor `path` dari `django.urls` dan impor `show_main` dari `main.views`. Definisikan `app_name` dengan `'main'` untuk memberikan nama unik pada pola URL aplikasi dan buatlah varibel `urlpatterns` menjadi:
    ```
    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
    ```
    Pada fungsi `path`, terdapat parameter pertama yaitu `''` agar halaman aplikasi tersebut muncul pada halaman utama *local path*. Parameter kedua adalah `show_main` yang berfungsi sebagai tampilan yang akan muncul ketika URL terkait diakses. Parameter ketiga yaitu `name` adalah untuk mengakses fungsi `show_main`.
    
- [x] **Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.**
    
    Untuk melakukan *deployment* ke Adaptable, unggah proyek terlebih dahulu ke repositori GitHub. Buat repositori GitHub baru dengan `stock-els` dan *visibility public* agar dapat dilihat orang lain. Lalu, sambungkan *folder* repositori lokal dengan repositori GitHub tersebut dengan melakukan `add`, `commit`, dan `push`.

    Setelah repositori GitHub selesai dibuat, *login* Adaptable dengan akun GitHub yang sama. Tekan tombol `New App` dan pilih `Connect an Existing Repository` lalu pilih repositori proyek `stock_els`. Selanjutnya, gunakan `Python App Template` sebagai *deploy template*-nya, `Postgre SQL` sebagai *database type*, dan sesuaikan versi python yang digunakan (`3.11`). Setelah itu, jalankan perintah `python manage.py migrate && gunicorn stock_els.wsgi` pada `Start Command`. Masukkan nama aplikasi (`stock-els`), ceklis bagian `HTTP Listener on PORT`, dan klik `Deploy App` untuk memulai *deployment process*.

- [x] **Membuat sebuah `README.md` yang berisi tautan menuju aplikasi Adaptable yang sudah di-deploy, serta jawaban dari beberapa pertanyaan yang diminta.**
    
    Menambahkan *file* `README.md` pada *folder* utama dan menjawab pertanyaan-pertanyaan yang diminta. Setiap melakukan perubahan pada *file* ini, lakukan perintah `add`, `commit`, dan `push` agar jawaban dapat tersinkronisasi dengan yang ada di repositori GitHub.

### 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
<img width="2142" alt="Flowchart Django" src="https://github.com/cheerylaisyah/stock_els/assets/113777425/fcf6bebf-0c9b-49e7-b0d5-2ce05c7030db">

### 3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

    *Virtual environment* adalah *tools* untuk mengisolasi *package* dan *dependencies* pada suatu proyek. Dengan *virtual environment*, kita dapat mengerjakan banyak proyek aplikasi dengan kebutuhan *library* beragam tanpa harus mengganggu proyek aplikasi lainnya. Dengan kata lain, *virtual environment* akan membuat pengelolaan dependensi proyek menjadi lebih mudah dan efisien.

    Pembuatan aplikasi *web* berbasis Django tetap bisa dilakukan tanpa menggunakan *virtual environment*, namun akan menjadi lebih sulit karena terdapat beberapa potensi masalah yang dapat muncul seperti, salah satunya adalah tabrakan antara proyek satu dengan proyek lainnya, khususnya jika keduanya memiliki dependensi yang berbeda. Oleh karena itu, penggunaan *virtual environment* dalam pembuatan aplikasi web berbasis Django sangatlah dianjurkan.

### 4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
    a. **MVC (Model-View-Controller)**:
        MVC adalah sebuah konsep arsitektur yang membagi kode pada aplikasi menjadi tiga komponen sehingga pemeliharaan dan pengoptimalan sistem menjadi lebih mudah. Cara kerja ini populer disebut dengan *separation of concerns*. 
        * *Model*: Mengelola dan berhubungan langsung dengan *database*.
        * *View*: Menyajikan tampilan informasi kepada pengguna
        * *Controller*: Menghubungkan *Model* dan *Vview* dalam setiap proses *request* dari *user*. 
        Alur kerja MVC yaitu *Controller* berinteraksi dengan *user*, lalu meneruskan perintah *user* ke *model* untuk menampilkan data yang diminta. Selanjutnya *model* akan memberikan data tersebut ke *Controller* agar ditampilkan oleh *View*. 

    b. **MVT (Model-View-Template)**:
        MVT adalah sebuah konsep arsitektur yang digunakan dalam pengembangan web untuk memisahkan komponen-komponen utama dari sebuah aplikasi. Konsep ini memungkinkan pengembang web untuk mengorganisasi dan mengelola kode dengan lebih terstruktur.
        * *Model*: Menyimpan data dan logika aplikasi.
        * *View*: Menampilkan data dari *Model* dan menghubungkannya dengan *Template*.
        * *Template*: Menentukan tampilan antarmuka pengguna.
        Alur kerja MVT yaitu permintaan yang masuk ke dalam *server* akan diproses melalui *urls* untuk diteruskan ke *View* yang didefinisikan oleh pengembang untuk memproses permintaan tersebut. Apabila terdapat proses yang membutuhkan keterlibatan *database*, maka nantinya *View* akan memanggil *query* ke *Model* dan *database* akan mengembalikan hasil dari *query* tersebut ke *View*. Setelah permintaan telah selesai diproses, hasil proses tersebut akan dipetakan ke dalam HTML yang sudah didefinisikan sebelum akhirnya HTML tersebut dikembalikan ke pengguna sebagai *respons*.

    c. **MVVM (Model-View-ViewModel)**:
        MVVM adalah sebuah arsitektur atau pola desain *software*, yang memisahkan logika bisnis dengan logika presentasi atau kontrol antarmuka pengguna (UI) menjadi tiga lapisan sehingga membuat aplikasi lebih mudah dikembangkan dan diuji karena minim masalah. 
        - *Model*: Menyimpan logika bisnis dan data aplikasi.
        - *View*: Bertanggung jawab menentukan struktur, tata letak, teks, gambar, dan elemen antarmuka lainnya yang nantinya dilihat oleh pengguna.
        - *ViewModel*: *Layer ViewModel* berada di antara *layer View* dan *Model*, dan berfungsi sebagai penghubung keduanya. 
        Alur proses MVVM adalah *ViewModel* mendapatkan *input* dari *View* mengenai aktivitas pengguna, dan melakukan *2-way data binding*. Perubahan pada elemen dalam kumpulan data secara otomatis diperbarui dalam kumpulan data terikat, dan menentukan fungsi UI. Setelah mendapatkan data, *ViewModel* meneruskannya ke *layer Model* untuk dimanipulasi dan disimpan. Perubahan status yang terjadi selama proses tersebut akan diumumkan melalui notifikasi perubahan dan akan dikirimkan data yang diperbarui ke *View* untuk ditampilkan kembali kepada pengguna.

**Perbedaan antara MVC, MVT dan MVVM:**
Ketiga pola arsitektur di atas memiliki komponen *Model* dan *View*, namun ketiganya memiliki tiga alur kerja yang berbeda. Perbedaan tersebut adalah sebagai berikut:
- Pada MVC, terdapat *Controller* yang berfungsi sebagai pengontrol interaksi atau media penghubung antara *Model* dan *View*.
- Pada MVT, ia serupa dengan MVC namun MVT memanfaatkan *Template* sebagai elemen terpisah yang mengatur tampilan antarmuka pengguna.
- Pada MVVM, terdapat *ViewModel* yang berperan sebagai mediator pengelola tampilan serta interaksi pengguna.