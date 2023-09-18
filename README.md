**Nama    : Cheeryl Aisyah Retnowibowo**

**NPM     : 2206813706**

**Kelas   : PBP C**

# [*Stock Els*](https://stock-els.adaptable.app/main)

## Link Adaptable: https://stock-els.adaptable.app

<details>
<summary><b>Tugas 2</b></summary>

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
    
- *Model*: Mengelola dan berhubungan langsung dengan *database*.
- *View*: Menyajikan tampilan informasi kepada pengguna
- *Controller*: Menghubungkan *Model* dan *Vview* dalam setiap proses *request* dari *user*. 

Alur kerja MVC yaitu *Controller* berinteraksi dengan *user*, lalu meneruskan perintah *user* ke *model* untuk menampilkan data yang diminta. Selanjutnya *model* akan memberikan data tersebut ke *Controller* agar ditampilkan oleh *View*. 

b. **MVT (Model-View-Template)**:
    MVT adalah sebuah konsep arsitektur yang digunakan dalam pengembangan web untuk memisahkan komponen-komponen utama dari sebuah aplikasi. Konsep ini memungkinkan pengembang web untuk mengorganisasi dan mengelola kode dengan lebih terstruktur.
    
- *Model*: Menyimpan data dan logika aplikasi.
- *View*: Menampilkan data dari *Model* dan menghubungkannya dengan *Template*.
- *Template*: Menentukan tampilan antarmuka pengguna.
    
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
</details>

<details>
<summary><b>Tugas 3</h1></b></summary>

### 1. Apa perbedaan antara form POST dan form GET dalam Django?
| POST  | GET |
| ------------- | ------------- |
| Mengirimkan data atau nilai langsung ke *action* untuk ditampung, tanpa menampilkan pada URL | Menampilkan data/nilai pada URL, kemudian akan ditampung oleh *action*  |
| Lebih aman | Kurang aman |
| Digunakan untuk mengirimkan data yang penting/kredensial.  | Digunakan untuk mengirimkan data dengan informasi umum yang dapat dilihat oleh *public* |
| Menampung data yang tidak terbatas | Hanya bisa menampung 2047 data |
| Pemanggilan method POST menggunakan $_POST | Pemanggilan method GET menggunakan $_GET |

### 2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
| Perbedaan | JSON | XML | HTML |
|--------------------------|---------------------------------------------|---------------------------------------------|---------------------------------------------|
| Pemahaman Data | Format data sering digunakan untuk pertukaran data terstruktur antara aplikasi | Format data yang sering digunakan untuk pertukaran data terstruktur, konfigurasi, dan penyimpanan dokumen | Digunakan untuk menggambarkan tampilan dan struktur halaman *web* |
| Struktur Data | Data dijelaskan dalam bentuk pasangan *key-value* (objek) atau array | Data dijelaskan dalam elemen yang dapat bersarang dan memiliki hierarki | Digunakan untuk membuat tampilan halaman *web* dengan elemen, atribut, dan teks |
| Tipe Data | Mendukung tipe data dasar seperti string, angka, boolean, objek, dan array | Mendukung berbagai jenis data dengan definisi khusus melalui DTD atau XML Schema | Mengandung teks, tautan, gambar, video, audio, dan elemen tampilan *web* lainnya |
| Validasi | Tidak memiliki mekanisme bawaan untuk validasi data | Dukungan untuk validasi data dengan XML Schema atau DTD | Tidak memiliki mekanisme bawaan untuk validasi data |
| Pembacaan | Penulisan dan pembacaan data relatif mudah, terutama dalam bahasa JavaScript | Pembacaan data memerlukan *parsing* XML, yang bisa jadi lebih kompleks | Penulisan dan pembacaan data mudah karena HTML didesain untuk ditampilkan di *browser* |
| Ukuran Data | Struktur data ringan dan biasanya lebih efisien dalam pengiriman dan penerimaan data | Lebih berat dan memerlukan lebih banyak karakter untuk menggambarkan data yang sama | Lebih berat dibandingkan JSON, tetapi biasanya lebih ringan daripada XML |
| Kelebihan | Mudah dibaca oleh manusia dan digunakan untuk pertukaran data antar aplikasi | Dukungan untuk validasi struktur data dan fleksibilitas dalam mendefinisikan tipe data | Digunakan untuk membuat tampilan halaman web yang interaktif |
| Kekurangan | Tidak memiliki mekanisme bawaan untuk validasi data dan kurang ekspresif dibandingkan XML | Memerlukan *parsing* yang lebih kompleks dan lebih berat daripada JSON | Tidak terstruktur secara formal dan memiliki keterbatasan dalam pengiriman data terstruktur |

### 3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
JSON didukung oleh JavaScript, yaitu bahasa pemrograman yang paling banyak digunakan dalam pengembangan *web* sehingga JSON memudahkan para *developer* untuk *parsed* dan *manipulated* dalam aplikasi *front-end*. JSON memungkinkan *developer* untuk merepresentasikan struktur data yang kompleks dalam format yang ringkas dan mudah dibaca sehingga ideal untuk pertukaran data antar aplikasi *web*. 

*Main point* dari JSON adalah *simplicity and readibility*. JSON sangat mudah ditulis dan dipahami karena menggunakan format yang sangat *human-readable*. JSON juga mendukung tipe-tipe data umum, seperti string, angka, boolean, null, objek, dan array, yang dapat di-*nested* dan dikombinasikan dengan berbagai cara. Selain itu, JSON juga memiliki tingkat *compatibility* dan *interoperability* yang baik dengan berbagai *platform*, bahasa, dan *frameworks*. JSON juga umumnya lebih cepat dan ringan daripada XML karena ukurannya yang lebih kecil dan strukturnya lebih sederhana. Oleh karena itu, JSON sering digunakan karena memiliki banyak keuntungan yang memudahkan para *developer* untuk mengembangkan suatu aplikasi *web* modern. 

### 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist secara step-by-step (bukan hanya sekadar mengikuti tutorial).

- [x] **Membuat input form untuk menambahkan objek model pada app sebelumnya**
    1. Membuat folder `templates` pada *root folder* bernama `base.html` sebagai *template* dasar yang digunakan untuk kerangka umum halaman *web* lainnya dalam proyek dengan kode:

        ```
        {% load static %}
        <!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="UTF-8" />
                <meta
                    name="viewport"
                    content="width=device-width, initial-scale=1.0"
                />
                {% block meta %}
                {% endblock meta %}
            </head>

            <body>
                {% block content %}
                {% endblock content %}
            </body>
        </html>
        ```

    2. Menambahkan kode `'DIRS': [BASE_DIR / 'templates'],` dalam `TEMPLATES` pada `settings.py` yang berada di subdirektori `stock_els`. Hal ini dilakukan agar `base.html` terbaca sebagai berkas *template*.
    3. Ubah kode yang pernah dibuat pada `main.html` dengan menambahkan:
    ```
    {% extends 'base.html' %}

    {% block content %}
        *kode yang pernah dibuat*
    {% endblock content %}
    ```
    4. Untuk membuat struktur *form* yang dapat menerima data produk baru, buat *file* baru dalam *folder* `main` dengan nama `forms.py` dengan kode:
    ```
    from django.forms import ModelForm
    from main.models import Product

    class ProductForm(ModelForm):
        class Meta:
            model = Product 
            fields = ["name", "amount", "size", "qty", "description"]
    ```
    - *ketika data dari *form* disimpan, isi dari *form* akan disimpan menjadi objek `Product`*
    5. Dalam `views.py` dalam folder `main`, tambahakan import baru dan fungsi baru `create_product` dengan parameter `request`, dan ubah fungsi `show_main`:
    ```
    from django.http import HttpResponseRedirect
    from main.forms import ProductForm
    from django.urls import reverse

    def show_main(request):
        products = Product.objects.all()

        context = {
           ...
        }

        return render(request, "main.html", context)

    def create_product(request):
        form = ProductForm(request.POST or None)

        if form.is_valid() and request.method == "POST":
            form.save()
            return HttpResponseRedirect(reverse('main:show_main'))

        context = {'form': form}
        return render(request, "create_product.html", context)
    ```
    - `form = ProductForm(request.POST or None)` --> membuat `ProductForm` baru dengan memasukkan QueryDict berdasarkan input *user* pada `request.POST`
    - `form.is_valid()` --> memvalidasi isi input dari *form*.
    - `form.save()` --> membuat dan menyimpan data dari *form*.
    - `return HttpResponseRedirect(reverse('main:show_main'))` --> melakukan *redirect* setelah data *form* berhasil disimpan.
    - `Product.objects.all()` --> mengambil seluruh object Product yang tersimpan pada *database*.
    6. Pada `urls.py` yang ada dalam *folder* `main`, lalu *import* fungsi `create_product` dan tambahkan *path url* ke dalam `urlpatterns`.
    7. Buat file `create_product.html` pada folder `main/templates` dan isi dengan kode berikut:
    ```
    {% extends 'base.html' %} 

    {% block content %}
    <h1>Add New Product</h1>

    <form method="POST">
        {% csrf_token %}
        <table>
            {{ form.as_table }}
            <tr>
                <td></td>
                <td>
                    <input type="submit" value="Add Product"/>
                </td>
            </tr>
        </table>
    </form>

    {% endblock %}
    ```
    - `<form method="POST">` --> menandakan *block* untuk *form* dengan metode POST.
    - `{% csrf_token %}` --> token yang berfungsi sebagai *security*
    - `{{ form.as_table }}` --> menampilkan *fields form* yang telah dibuat pada `forms.py` sebagai *table*
    - `<input type="submit" value="Add Product"/>` --> tombol *submit* untuk mengirimkan *request* ke *view* `create_product(request)`.
    8. Untuk menampilkan data produk dalam bentuk *table* serta tombol `Add New Product` yang akan *redirect* ke halaman *form* dengan menambahkan kode di bawah ini di antara `{% block content %}` dan `{% endblock content %}`:
    ```
    ...
    <table>
    <tr>
        <th>Name</th>
        <th>Amount</th>
        <th>Size</th>
        <th>Qty</th>
        <th>Description</th>
        <th>Date Added</th>
    </tr>

    {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini {% endcomment %}

    {% for product in products %}
        <tr>
            <td>{{product.name}}</td>
            <td>{{product.amount}}</td>
            <td>{{product.size}}</td>
            <td>{{product.qty}}</td>
            <td>{{product.description}}</td>
            <td>{{product.date_added}}</td>
        </tr>
    {% endfor %}
    </table>

    <br />

    <a href="{% url 'main:create_product' %}">
        <button>
            Add New Product
        </button>
    </a>
    ```


- [x] **Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID**
    1. Pada `views.py` dalam folder `main` tambahkan import dan fungsi di bawah ini:
    ```
    from django.http import HttpResponse
    from django.core import serializers

    def show_xml(request):
        data = Product.objects.all()
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json(request):
        data = Product.objects.all()
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")

    def show_xml_by_id(request, id):
        data = Product.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json_by_id(request, id):
        data = Product.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```

- [x] **Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2**
    1. Pada `urls.py` dalam folder `main`, import fungsi yang telah ditambahkan sebelumnya dan tambahkan *path url* ke dalam `urlpatterns` untuk mengakses fungsi yang telah diimpor hingga kode menjadi seperti di bawah ini:
    ```
    ...
    from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id
    ...
    urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    ]

    ```
</details>

### 5. Hasil akses URL pada Postman
- HTML

- XML

- JSON

- XML *by* ID

- JSON *by* ID

### 6. Melakukan add-commit-push ke GitHub.
Pada *root folder*, lakukan add-commit-push ke dalam repository GitHub yang telah ditetapkan di awal.