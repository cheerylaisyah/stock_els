**Nama    : Cheeryl Aisyah Retnowibowo**

**NPM     : 2206813706**

**Kelas   : PBP C**

# 💫👟[*Stock Els*](https://stock-els.adaptable.app/main)

## 💻Link Adaptable: https://stock-els.adaptable.app

<details>
<summary><b>📝Tugas 2</b></summary>

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
<summary><b>📝Tugas 3</h1></b></summary>

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
    from main.models import Item

    class ItemForm(ModelForm):
        class Meta:
            model = Item
            fields = ["name", "amount", "size", "qty", "description"]
    ```
    - *ketika data dari *form* disimpan, isi dari *form* akan disimpan menjadi objek `Item`*

- [x] **Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID**
    1. Untuk menampilkan objek dalam format HTML, pada `views.py` dalam folder `main`, tambahkan import baru dan fungsi baru `create_item` dengan parameter `request`, dan ubah fungsi `show_main`:
    ```
    from django.http import HttpResponseRedirect
    from main.forms import ItemForm
    from django.urls import reverse

    def show_main(request):
        items = Item.objects.all()

        context = {
           ...
        }

        return render(request, "main.html", context)

    def create_item(request):
        form = ItemForm(request.POST or None)

        if form.is_valid() and request.method == "POST":
            form.save()
            return HttpResponseRedirect(reverse('main:show_main'))

        context = {'form': form}
        return render(request, "create_item.html", context)
    ```
    - `form = ItemForm(request.POST or None)` --> membuat `ItemForm` baru dengan memasukkan QueryDict berdasarkan input *user* pada `request.POST`
    - `form.is_valid()` --> memvalidasi isi input dari *form*.
    - `form.save()` --> membuat dan menyimpan data dari *form*.
    - `return HttpResponseRedirect(reverse('main:show_main'))` --> melakukan *redirect* setelah data *form* berhasil disimpan.
    - `Item.objects.all()` --> mengambil seluruh object Item yang tersimpan pada *database*.
    2. Buat file `create_item.html` pada folder `main/templates` dan isi dengan kode berikut:
    ```
    {% extends 'base.html' %} 

    {% block content %}
    <h1>Add New Item</h1>

    <form method="POST">
        {% csrf_token %}
        <table>
            {{ form.as_table }}
            <tr>
                <td></td>
                <td>
                    <input type="submit" value="Add Item"/>
                </td>
            </tr>
        </table>
    </form>

    {% endblock %}
    ```
    - `<form method="POST">` --> menandakan *block* untuk *form* dengan metode POST.
    - `{% csrf_token %}` --> token yang berfungsi sebagai *security*
    - `{{ form.as_table }}` --> menampilkan *fields form* yang telah dibuat pada `forms.py` sebagai *table*
    - `<input type="submit" value="Add Item"/>` --> tombol *submit* untuk mengirimkan *request* ke *view* `create_item(request)`.
    3. Untuk menampilkan data produk dalam bentuk *table* serta tombol `Add New Item` yang akan *redirect* ke halaman *form* dengan menambahkan kode di bawah ini di antara `{% block content %}` dan `{% endblock content %}`:
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

    {% for item in items %}
        <tr>
            <td>{{item.name}}</td>
            <td>{{item.price}}</td>
            <td>{{item.size}}</td>
            <td>{{item.amount}}</td>
            <td>{{item.description}}</td>
            <td>{{item.date_added}}</td>
        </tr>
    {% endfor %}
    </table>

    <br />

    <a href="{% url 'main:create_item' %}">
        <button>
            Add New Item
        </button>
    </a>
    ```
    4. Untuk menampilkan objek dalam format XML, JSON, XML *by* ID, dan JSON *by* ID, buka kembali `views.py` dalam folder `main` lalu tambahkan import dan fungsi di bawah ini:
    ```
    from django.http import HttpResponse
    from django.core import serializers

    def show_xml(request):
        data = Item.objects.all()
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json(request):
        data = Item.objects.all()
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")

    def show_xml_by_id(request, id):
        data = Item.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json_by_id(request, id):
        data = Item.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```

- [x] **Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2**
    1. Pada `urls.py` dalam folder `main`, import fungsi yang telah ditambahkan sebelumnya dan tambahkan *path url* ke dalam `urlpatterns` untuk mengakses fungsi yang telah diimpor hingga kode menjadi seperti di bawah ini:
    ```
    ...
    from main.views import show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id
    ...
    urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    ]

    ```
### 5. Hasil akses URL pada Postman
- HTML
  <img width="960" alt="HTML" src="https://github.com/cheerylaisyah/stock_els/assets/113777425/e7467225-f05f-4682-941a-0f7bf3371cf4">

- XML
  <img width="960" alt="XML" src="https://github.com/cheerylaisyah/stock_els/assets/113777425/b7cf1e90-51cf-44a9-a4cc-81cf06ce946c">

- JSON
  <img width="960" alt="JSON" src="https://github.com/cheerylaisyah/stock_els/assets/113777425/b9397d92-7dfc-4921-aa19-ebefa6c0ffa3">

- XML *by* ID
  <img width="960" alt="XML by ID" src="https://github.com/cheerylaisyah/stock_els/assets/113777425/73b26d67-adb9-4213-a289-d8e4f84c132f">

- JSON *by* ID
  <img width="960" alt="JSON by ID" src="https://github.com/cheerylaisyah/stock_els/assets/113777425/b9d30b18-c314-4343-8023-19fdcf99171c">

### 6. Melakukan add-commit-push ke GitHub.
Pada *root folder*, lakukan add-commit-push ke dalam repository GitHub yang telah ditetapkan di awal.

========
### Referensi
Dimas, S. (2019, September 17). Perbedaan Method GET dan POST! Kapan sebaiknya digunakan ? Kelas Programmer. Retrieved September 18, 2023, from https://kelasprogrammer.com/perbedaan-method-get-dan-post-kapan-digunakan/

JSON for Web Applications: Benefits and Drawbacks. (2023, August 25). LinkedIn. Retrieved September 18, 2023, from https://www.linkedin.com/advice/3/what-benefits-drawbacks-using-json-data

JSON vs XML. (2022, November 11). AppMaster. Retrieved September 18, 2023, from https://appmaster.io/id/blog/json-vs-xml-id

JSON vs XML - Perbedaan Antara Berbagai Representasi Data - AWS. (n.d.). Amazon AWS. Retrieved September 18, 2023, from https://aws.amazon.com/id/compare/the-difference-between-json-xml/

Panduan Perbedaan XML dan HTML yang Wajib Kamu Ketahui. (2021, December 23). Exabytes. Retrieved September 18, 2023, from https://www.exabytes.co.id/blog/perbedaan-xml-dan-html/

Perbedaan Method POST dan GET Beserta Fungsinya. (2016, November 6). Makinrajin. Retrieved September 18, 2023, from https://makinrajin.com/blog/perbedaan-post-dan-get/

Unlocking the Power of JSON Data Type in Web Development. (2023, April 22). LinkedIn. Retrieved September 18, 2023, from https://www.linkedin.com/pulse/unlocking-power-json-data-type-web-development-elvin-shahsuvarli
</details>

<details>
<summary><b>📝Tugas 4</h1></b></summary>

### 1. Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
Django UserCreationForm adalah impor *form* bawaan dari Django yang memudahkan pembuatan *form* pendaftaran *user* dalam aplikasi *web*. UserCreationForm memiliki tiga *fields* yaitu `username`, `password`, `confirmation password`. Dengan *form* ini, *user* baru dapat mendaftar dengan mudah di situs *web* tanpa harus menulis kode dari awal. 

- **Kelebihan**

    1. *Built-In Authentication*

        Karena merupakan bagian dari *framework* Django, UserCreationForm mudah diimplementasikan dan memiliki fungsionalitas yang tinggi di mana developer tidak perlu membuat *code* dari *strach*. Bahkan, *form* yang disediakan juga sudah terdapat validasi otomatisnya.

    2. *Security*

        *Form* telah meng-*handle* masalah kemanan seperti validasi kata sandi dan *password hashing* di mana melindungi data *user*.

    3. *Customization*

        Kita dapat dengan mudah mengkustomisasi *form* tersebut, contohnya menambahkan *fields* tambahan sebagai syarat registrasi.

    4. *Compatibility*

        Karena merupakan bagian dari *framework* Django, *form* ini akan selalu *update* mengikuti *update* dari Django sehingga bersifat *well-maintained* dan memastikan *security & compability* yang ada sudah *up-to-date*.

- **Kekurangan**
    1. *Basic Features*

        UserCreationForm menyediakan fungsi pendaftaran yang sangat *basic* sehingga jika kita memerlukan fitur-fitur tambahan ataupun menyesuaikan dengan desain aplikasi kita, diperlukan kustomisasi kembali di mana dapat menjadi kompleks dan memakan waktu.

    2. *Internationalization* (i18n)

        Perlu dipastikan kembali apakah label-label form dan pesan yang ditampilkan sesuai dengan bahasa yang diinginkan.

    3. *Dependency on Django*

        UserCreationForm merupakan *framework* bawaan dari Django sehingga jika suatu saat aplikasi/web beralih ke sistem otentikasi atau kerangka kerja yang berbeda, perlu disesuaikan kembali fungsionalitas form pendaftaran user.

### 2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
| Autentikasi  | Otorisasi |
| ------------- | ------------- |
| Identitas pengguna diperiksa untuk memberikan akses ke sistem | Otoritas pengguna diperiksa untuk mengakses *resources* pada sistem |
| Pengguna diverifikasi melalui nama pengguna, *password*, *face recognition*, *retina scan*, *fingerprint*, dll. | Pengguna divalidasi berdasarkan hak ases terhadap *resources* dengan menggunakan *role* yang telah ditentukan sebelumnya |
| Memerlukan detail login pengguna | Memerlukan *user's privilege* atau *security levels* |
| Menentukan apakah orang tersebut adalah pengguna atau bukan | Menentukan apakah izin yang dimiliki pengguna tersebut |
| Terlihat pada *end user* | Tidak terlihat oleh *end user* |

Contoh dari perbedaan keduanya adalah, saat mahasiswa melakukan login pada SCELE. Mahasiswa diharuskan login terlebih dahulu sebagai bentuk autentikasi untuk menenetukan apakah terdaftar sebagai mahasiswa UI atau bukan sebelum mengakses laman SCELE. Setelah mahasiswa berhasil melakukan autentikasi, sistem menentukan informasi apa yang boleh diakses oleh mahasiswa tersebut berdasarkan *role* yang telah ditentukan dalam sistem.

Autentikasi dan otorisasi sangat penting untuk menjaga keamanan, privasi data, dan integritas sistem komputer dan aplikasi. Keduanya bekerja sama untuk memastikan bahwa hanya pengguna yang berwenang yang dapat mengakses data dan sumber daya yang sesuai, serta melindungi informasi pengguna dari akses yang tidak sah.

### 3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
Cookies dalam konteks aplikasi web adalah potongan data kecil yang disimpan di browser client. Cookies digunakan untuk menyimpan data pengguna dalam file secara permanen (atau untuk waktu tertentu) dan mengelola sesi pengguna dengan efektif dan aman. 

Ketika seorang pengguna pertama kali mengakses situs web Django, cookie session yang unik dibuat dan disimpan di perangkat mereka. Cookie ini berisi sebuah pengenal yaitu session ID sebagai suatu token (barisan karakter) untuk mengenali session yang unik pada aplikasi web tertentu. Session ID memungkinkan Django untuk mengenali dan mengaitkan interaksi pengguna selanjutnya dengan sesi khusus mereka di server. Session ID ini kemudian dapat dipetakan ke suatu struktur data pada sisi web server di mana memudahkan pengambilan dan pembaruan informasi session dengan lancar.

### 4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Penggunaan cookies dalam pengembangan web relatif aman. Namun, jika data cookie jatuh ke tangan yang salah maka dapat disalahgunakan untuk mengakses sesi penelusuran, mencuri informasi pribadi, dsb. Beberapa serangan yang bisa terjadi berkaitan dengan cookies ini adalah:

a. *Cross-Site Scripting* (XSS)

Eksploitasi keamanan di mana penyerang menempatkan malicious client-end code ke laman web dengan tujuan untuk mengambil data penting, mengambil cookie dari user atau mengirimkan suatu program yang dapat merusak user namun membuatnya terlihat disebabkan oleh web itu sendiri. Untuk mencegahnya, gunakan metode keamanan seperti HTTP Only untuk melindungi cookies dari serangan ini.

b. *Cross-Site Request Forgery* (CSRF)

Serangan CSRF dapat memanipulasi cookies untuk melakukan tindakan tidak diinginkan pada nama pengguna yang terotentikasi. Token CSRF dapat diimplementasikan untuk mencegah serangan ini.

Oleh karena itu, walaupun penggunaan cookies aman, namun kita perlu melakukan langkah-langkah pencegahan untuk menghindari hal-hal yang tidak diinginkan, seperti mematuhi praktik keamanan yang baik, mengenkripsi data sensitif yang disimpan dalam cookies, dan melakukan validasi data yang masuk ke dalam cookies.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- [x] **Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.**
1. Registrasi

    a. Pada `main/views.py`:
    - Tambahkan import berikut:
        ```
        from django.shortcuts import redirect
        from django.contrib.auth.forms import UserCreationForm
        from django.contrib import messages  
        ```
        Notes:
        - UserCreationForm --> impor form bawaan Django yang memudahkan pembuatan form pendaftaran user dalam aplikasi web tanpa harus menulis kode dari awal.
    - Untuk menghasilkan form registrasi secara otomatis dan membuat akun user ketika data dari form di-submit, buat fungsi `register` dengan parameter `request` dan isi dengan kode berikut:
        ```
        def register(request):
            form = UserCreationForm()

            if request.method == "POST":
                form = UserCreationForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Your account has been successfully created!')
                    return redirect('main:login')
            
            context = {'form':form}

            return render(request, 'register.html', context)
        ```
        Notes:
        - `form = UserCreationForm(request.POST)` --> membuat `UserCreationForm` baru dari yang telah diimpor sebelumnya dengan memasukkan QueryDict berdasarkan input dari user pada `request.POST`.
        - `form.is_valid` --> memvalidasi data dari form tersebut.
        - `form.save` --> membuat dan menyimpan data dari form tersebut.
        - `messages.success(request, 'Your account has been successfully created!')` --> menampilkan pesan kepada pengguna setelah berhasil membuat akun.
        - `return redirect('main:show_main')` --> melakukan redirect setelah data form berhasil disimpan.

    b. Pada folder `main/templates`, buat file HTML dengan nama `register.html` dan isi dengan kode berikut:
    ```
    {% extends 'base.html' %}

    {% block meta %}
        <title>Register</title>
    {% endblock meta %}

    {% block content %}  

    <div class = "login">
        
        <h1>Register</h1>  

            <form method="POST" >  
                {% csrf_token %}  
                <table>  
                    {{ form.as_table }}  
                    <tr>  
                        <td></td>
                        <td><input type="submit" name="submit" value="Register"/></td>  
                    </tr>  
                </table>  
            </form>

        {% if messages %}  
            <ul>   
                {% for message in messages %}  
                    <li>{{ message }}</li>  
                    {% endfor %}  
            </ul>   
        {% endif %}

    </div>  

    {% endblock content %}
    ```

2. Login

    a. Pada `main/views.py`:
    - Tambahkan impor berikut:

        ```
        from django.contrib.auth import authenticate, login
        ```

        Notes:
        - fungsi `authenticate` dan `login` --> melakukan autentikasi dan login jika autentikasi berhasil
    - Untuk membuat form login, buat fungsi `login_user` dengan parameter `request` dan isi dengan kode berikut:
        ```
        def login_user(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main:show_main')
            else:
                messages.info(request, 'Sorry, incorrect username or password. Please try again.')
        context = {}
        return render(request, 'login.html', context)
        ```
        Notes:
        - `authenticate(request, username=username, password=password` --> melakukan autentikasi user berdasarkan username & password yang diterima dari request yang dikirim oleh user saat login.

    b. Pada folder `main/templates`, buat file HTML dengan nama `login.html` dan isi dengan kode berikut:
    ```
    {% extends 'base.html' %}

    {% block meta %}
        <title>Login</title>
    {% endblock meta %}

    {% block content %}

    <div style="display: flex; justify-content: center; align-items: center; min-height: 90vh;">
        <div class="login">

            <h1>Login</h1>

            <form method="POST" action="">
                {% csrf_token %}
                <table>
                    <tr>
                        <td>Username: </td>
                        <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
                    </tr>

                    <tr>
                        <td>Password: </td>
                        <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
                    </tr>

                    <tr>
                        <td></td>
                        <td><input class="btn login_btn" type="submit" value="Login"></td>
                    </tr>
                </table>
            </form>

            {% if messages %}
                <ul>
                    {% for message in messages %}
                        <li>{{ message }}</li>
                    {% endfor %}
                </ul>
            {% endif %}

            Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>
            
        </div>
    </div>

    {% endblock content %}
    ``````

3. Logout

    a. Pada `main/views.py`:
    - Tambahkan impor berikut::
        ```
        from django.contrib.auth import logout
        ```
    - Buat fungsi `logout_user` dengan parameter `request` dan isi dengan kode berikut:
        ```
        def logout_user(request):
            logout(request)
            return redirect('main:login')
        ```
        Notes:
        - `logout(request)` --> menghapus sesi pengguna yang saat ini masuk.
        - `return redirect('main:login')` --> mengarahkan pengguna ke halaman login dalam aplikasi Django.

    b. Pada `main/templates/main.html`:
    Setelah *hyperlink tag* untuk `Add New Item`, tambahkan kode berikut:
    ```
    ...
    <a href="{% url 'main:logout' %}">
        <button>
            Logout
        </button>
    </a>
    ...
    ```
 - Untuk menampilkan ketiga fungsi tersebut ke aplikasi, buka `main/urls.py`, import fungsi yang telah dibuat dan tambahkan path url dalam `urlpatterns` untuk mengakses fungsi yang di-import:
    ```
    from main.views import register, login_user, logout_user
    ...
    urlpatterns = [
        ...
        path('register/', register, name='register'), 
        path('login/', login_user, name='login'),
        path('logout/', logout_user, name='logout'),
    ]
    ```
- Untuk memastikan hanya user yang memiliki akun pada aplikasi yang dapat mengakses halaman main, lakukan hal berikut:

    a. Pada `main/views.py`:
    
    - Tambahkan import:
        ```
        from django.contrib.auth.decorators import login_required
        ```
        Notes:
        - `from django.contrib.auth.decorators import login_required` --> mengharuskan pengguna untuk login sebelum dapat mengakses suatu halaman web
        
    b. Di atas fungsi `show_main`, tambahkan kode:
    ```
    ...
    @login_required(login_url='/login')
    def show_main(request):
    ...
    ```
- [x] **Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.**
- Flow pembuatan akun dan menambahkan tiga dummy data:
    <img width="1887" alt="Flow Add Item" src="https://github.com/cheerylaisyah/stock_els/assets/113777425/a20bf1a7-7c82-41ea-86b0-5d692c7324ad">

- Akun Pertama
    <img width="960" alt="Akun 1" src="https://github.com/cheerylaisyah/stock_els/assets/113777425/cec0f584-de61-42a2-875a-9df897136754">

- Akun Kedua
    <img width="960" alt="Akun 2" src="https://github.com/cheerylaisyah/stock_els/assets/113777425/3f1a2768-9452-43a4-94b6-8dd61239a368">

- [x] **Menghubungkan model Item dengan User.**

a. Pada `main/models.py`

- Tambahkan impor:
    ```
    from django.contrib.auth.models import User
    ```
- Dengan *relationship*, kita dapat menghubungkan suatu item dengan satu user tertentu, yaitu dengan menambahkan kode berikut pada model `Item`:
    ```
    class Item(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        ...
    ```

b. Pada `main/views.py`
    
- Pada fungsi `create_item` ubah potongan kodenya menjadi seperti di bawah ini:
    ```
    def create_item(request):
        form = ItemForm(request.POST or None)

        if form.is_valid() and request.method == "POST":
            # Tugas 4
            item = form.save(commit=False)
            item.user = request.user
            item.save()    
            return HttpResponseRedirect(reverse('main:show_main'))
    ...
    ```
    Notes:
    - Parameter `commit=False` --> untuk memastikan objek yang dibuat tidak langsung di-save oleh Django sehingga memungkinkan kita untuk melakukan modifikasi jika diperlukan.
    - `item.user = request.user` --> menandakan bahwa item yang dibuat dimiliki oleh user yang sedang login.
- Untuk memastikan objek `Item` yang ditampilkan hanya milik user yang sedang login, ubah kode pada fungsi `show_main` menjadi seperti berikut:
    ```
    def show_main(request):
        items = Item.objects.filter(user=request.user)
        ...
    ...
    ```

Dengan melakukan perubahan pada model, maka kita perlu melakukan migrasi model pada aplikasi yaitu dengan `python manage.py makemigrations` dan `python manage.py migrate`.

- [x] **Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.**

a. Menampilkan detail informasi pengguna yang sedang logged in.

- Pada `main/views.py` ubah kode pada fungsi `show_main` menjadi seperti berikut:
    ```
    def show_main(request):
        ...
        context = {
            'name': request.user.username,
        ...
    ...
    ```
    Notes:
    - `request.user.username` --> menampilkan username pengguna yang login pada halaman main.

b. Menerapkan cookies seperti last login pada halaman utama aplikasi.

Pada `main/views.py`:
- Tambahkan import:
    ```
    import datetime
    from django.http import HttpResponseRedirect
    from django.urls import reverse
    ```
- Tambahkan cookie bernama `last_login` di dalam fungsi `login_user` sehingga kita dapat melihat kapan terakhir kali pengguna melakukan login dengan mengganti kode pada blok `if user is not None`:
    ```
    ...
    if user is not None:
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main")) 
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
    ...
    ```
    Notes:
    - `login(request, user)` --> meminta user melakukan login
    - `response = HttpResponseRedirect(reverse("main:show_main"))` --> membuat response agar redirect ke halaman utama
    - `response.set_cookie('last_login', str(datetime.datetime.now()))` --> membuat cookie last_login dan menambahkannya ke dalam response

- Untuk menambahkan informasi cookie last_login di halaman web, tambahkan potongan kode `'last_login': request.COOKIES['last_login'],` ke dalam variabel `context`.
- Untuk menghapus cookie `last_login` saat pengguna melakukan `logout`, ubah fungsi `logout_user` menjadi di bawah ini:
    ```
    def logout_user(request):
        logout(request)
        response = HttpResponseRedirect(reverse('main:login'))
        response.delete_cookie('last_login')
        return response
    ```
Pada `main/templates/main.html`:
- Untuk menampilkan data last login, tambahkan kode berikut di antara tabel dan button logout:
    ```
    ...
    <h5>Sesi terakhir login: {{ last_login }}</h5>
    ...
    ```

### 6. Bonus
- [x] **Tambahkan tombol dan fungsi untuk menambahkan amount suatu objek sebanyak satu, mengurangi jumlah stok suatu objek sebanyak satu, dan menghapus suatu objek dari inventori .**
- Pada `main/views.py`, buat fungsi untuk ketiga action tersebut:
    ```
    # Menambahkan satu item
    def decrement_item(request, id):
        item = Item.objects.get(id=id)

        if (item.amount > 0):
            item.amount -= 1
            item.save()
            if item.amount <= 0:
            Item.objects.filter(pk=id).delete()

        return HttpResponseRedirect(reverse("main:show_main"))

    # Mengurangi satu item
    def increment_item(request, id):
        item = Item.objects.get(id=id)

        item.amount += 1
        item.save()
        
        return HttpResponseRedirect(reverse("main:show_main"))

    # Menghapus item
    def remove_item(request, id):
        Item.objects.filter(pk=id).delete()

        return HttpResponseRedirect(reverse("main:show_main"))
    ```
- Lakukan routing untuk ketiga fungsi dalam `main/urls.py`:
    ```
    from main.views import decrement_item, increment_item, remove_item

    urlpatterns = [
        ...
        path('decrement-item/<int:id>', decrement_item, name='decrement_item'),
        path('increment-item/<int:id>', increment_item, name='increment_item'),
        path('remove-item/<int:id>', remove_item, name='remove_item')
    ]
    ```
- Tampilkan ketiga action tersebut pada halaman aplikasi dengan menambahkan kode berikut pada `main/templates/main.html`:
    ```
    <!-- menambahkan button tentang amount item sebagai bonus -->
                <td style="text-align: center;">
                    <form action="{% url 'main:increment_item' item.id %}" method="post" style="display: inline;">
                        {% csrf_token %}
                        <button type="submit" name="increment">
                            +
                        </button>
                    </form>
                    <form action="{% url 'main:decrement_item' item.id %}" method="post" style="display: inline;">
                        {% csrf_token %}
                        <button type="submit" name="decrement">
                            -
                        </button>
                    </form>
                    <form action="{% url 'main:remove_item' item.id %}" method="post" style="display: inline;">
                        {% csrf_token %}
                        <button type="submit" name="remove">
                            Remove
                        </button>
                    </form>
                </td>
    ```

### 7. Melakukan add-commit-push ke GitHub.
Pada *root folder*, lakukan add-commit-push ke dalam repository GitHub yang telah ditetapkan di awal.
</details>

<details>
<summary><b>📝Tugas 5</b></summary>

### 1. Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.
| Nama Selektor | Manfaat | Waktu Penggunaan | Contoh Penggunaan |
|-|-|-|-|
| Selektor Elemen (Tag) | Memilih semua elemen HTML dengan jenis tag tertentu. | Cocok digunakan ketika ingin menerapkan gaya yang sama pada semua elemen dengan jenis tag yang sama. Misalnya, untuk mengatur gaya default untuk semua paragraf (<p>) di halaman web. | `p`|
| Selektor Universal (*) | Memilih semua elemen dalam dokumen HTML. | Harus digunakan dengan hati-hati karena dapat memengaruhi semua elemen dalam halaman. Sebaiknya digunakan untuk mengatur reset CSS atau gaya default di tingkat tinggi. | `*` |
| Selektor ID (#id) | Memilih elemen berdasarkan atribut id yang unik. | Digunakan ketika ingin mengatur gaya untuk elemen tunggal yang memiliki atribut id unik. Juga berguna dalam konteks JavaScript ketika perlu merujuk ke elemen tertentu. | `#header` |
| Selektor Kelas (.class) | Memilih elemen berdasarkan atribut class. | Ketika ingin menerapkan gaya yang sama pada beberapa elemen dengan atribut class yang sama atau ketika ingin menambahkan perilaku JavaScript ke elemen-elemen serupa. | `.btn-primary` |
| Selektor Atribut ([attribute]) | Memilih elemen berdasarkan atribut HTML mereka. | Saat ingin memilih elemen berdasarkan atribut tertentu, misalnya, ketika ingin mengatur gaya untuk semua tautan eksternal (<a>) dengan href eksternal. | `[href]` |
| Selektor Pseudo-class (:pseudo-class) | Memilih elemen dalam keadaan tertentu atau berdasarkan interaksi pengguna. | Saat ingin mengubah gaya elemen saat interaksi pengguna, seperti mengubah warna tautan saat diklik (:hover) atau mengatur ulang inputan saat difokuskan (:focus). | `a:hover` |
| Selektor Pseudo-element (::pseudo-element) | Memilih bagian dari elemen yang mungkin tidak ada dalam markup HTML. | Digunakan saat ingin mengatur gaya bagian-bagian tertentu dari elemen, seperti menambahkan konten sebelum atau sesudah elemen (::before dan ::after) atau memformat teks yang dipilih (::selection). | `::before` |

### 2. Jelaskan HTML5 Tag yang kamu ketahui.
| Tag HTML   | Penjelasan                                               |
|------------|---------------------------------------------------------|
| `<a>`      | Menentukan tautan atau hyperlink ke halaman web atau berkas lain. |
| `<b>`      | Menampilkan teks dalam gaya tebal (bold).                   |
| `<body>`   | Menentukan badan atau konten utama dokumen HTML.           |
| `<br>`     | Menghasilkan satu baris pemisah.                           |
| `<button>` | Membuat tombol yang dapat diklik.                          |
| `<col>`    | Menentukan nilai atribut untuk satu atau lebih kolom dalam tabel. |
| `<div>`    | Mengelompokkan dan mengatur konten dalam blok yang dapat diubah tampilannya menggunakan CSS. |
| `<form>`   | Menentukan formulir HTML untuk input pengguna.               |
| `<head>`   | Menentukan bagian kepala dokumen yang berisi informasi tentang dokumen, seperti judul. |
| `<h1>` - `<h6>` | Menentukan tingkat kepentingan berbagai judul atau heading dalam halaman web. |
| `<html>`   | Menentukan elemen root dari dokumen HTML.                    |
| `<i>`      | Menampilkan teks dalam gaya miring (italic).                 |
| `<img>`    | Menampilkan gambar di halaman web.                           |
| `<input>`  | Menentukan kontrol input, seperti kotak input teks.          |
| `<label>`  | Menentukan label untuk kontrol input seperti `<input>`.     |
| `<li>`     | Menentukan item dalam daftar, seperti daftar tak terurut (unordered list). |
| `<meta>`   | Menyediakan informasi meta tentang dokumen, seperti karakter encoding dan deskripsi halaman. |
| `<nav>`    | Menentukan bagian dari navigasi atau tautan-tautan menu dalam halaman web. |
| `<p>`      | Menampilkan paragraf teks.                                   |
| `<small>`  | Menampilkan teks dalam ukuran kecil.                        |
| `<style>`  | Menyisipkan informasi gaya, seperti CSS, ke dalam dokumen.     |
| `<table>`  | Menentukan tabel untuk menampilkan data tabular.            |
| `<tbody>`  | Mengelompokkan baris-baris yang mendefinisikan isi utama dari tabel. |
| `<td>`     | Menentukan sel dalam tabel.                                  |
| `<textarea>` | Menentukan kontrol input teks multi-baris (text area).     |
| `<th>`     | Menentukan sel header dalam tabel.                           |
| `<thead>`  | Mengelompokkan baris-baris yang mendefinisikan label kolom dalam tabel. |
| `<tr>`     | Menentukan baris dalam tabel.                               |
| `<ul>`     | Menentukan daftar tak terurut (unordered list).              |

### 3. Jelaskan perbedaan antara margin dan padding.
<img width=400px alt="Margin vs Padding" src="https://images.ctfassets.net/pdf29us7flmy/6FMwLUnze6f6SQjjxpB5lq/4da8905078cce5668a00b488f913340d/-IND-004-082-_When_and_How_To_Use_Margin_vs._Padding_in_CSS_-_Final.png">

| Fitur | Margin | Padding |
| - | - | - |
| Definisi | Jarak di luar batas elemen. | Jarak di dalam batas elemen.|
| Penggunaan| Mengatur jarak antara elemen dan elemen-elemen lain. | Mengatur jarak antara konten elemen dan batas elemen itu sendiri. |
| Latar Belakang | Tidak memiliki latar belakang atau warna sendiri. | Memiliki latar belakang atau warna yang sama dengan elemen tersebut. |
| Mempengaruhi  | Mempengaruhi tata letak elemen itu sendiri dan elemen-elemen lain di sekitarnya. | Mempengaruhi tampilan elemen itu sendiri dan jarak antara konten dan batasnya. |
| Penyajian Visual | Menciptakan ruang di sekitar elemen. | Menciptakan ruang di dalam elemen sekitar kontennya. |
| Penggunaan Umum | Mengatur jarak antara elemen-elemen yang berdekatan atau elemen dengan elemen tetangganya. | Mengatur jarak antara konten elemen dan elemen itu sendiri. |
| Nilai Numerik  | Bilangan bulat. | Bilangan real positif. |

### 4. Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
| Tailwind CSS | Bootstrap |
|-|-|
| Framework CSS berbasis utilitas (utility-first). Membangun tampilan dengan menggabungkan kelas-kelas utilitas yang telah didefinisikan sebelumnya. | Framework berbasis komponen dengan class utilitas. Menggunakan gaya dan komponen yang telah didefinisikan, yang memiliki tampilan yang sudah jadi dan dapat digunakan secara langsung. |
| Memberikan fleksibilitas dan adaptabilitas tinggi terhadap proyek. | Sering kali menghasilkan tampilan yang lebih konsisten di seluruh proyek karena menggunakan komponen yang telah didefinisikan. |
| Tema yang dapat disesuaikan menggunakan berkas konfigurasi. | Menawarkan tema dan template yang telah didesain sebelumnya. |
| Tersedia perpustakaan komponen berpendapat, seperti Tailwind UI (produk komersial). | Dilengkapi dengan perpustakaan komponen yang luas. |
| Kurva belajar yang lebih curam karena karena perlu memahami kelas-kelas utilitas. | Lebih mudah bagi pemula yang sudah akrab dengan CSS. |
| Komunitas yang lebih kecil namun sumber daya yang sangat membantu karena popularitas yang meningkat. | Komunitas besar dengan sumber daya yang sangat banyak. |

Maka, untuk memilih di antara kedua framework ini, bergantung kepada kebutuhan dan kemampuan kita. Jika kita ingin tingkat kontrol yang tinggi atau kemampuan CSS yang tinggi maka gunakan Tailwind, namun jika kita ingin membuat website dengan cepat menggunakan komponen yang sudah ada atau kemampuan CSS yang masih pemula maka gunakan Bootstrap.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Kustomisasi desain pada templat HTML yang telah dibuat pada Tugas 4 dengan menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma) dengan ketentuan sebagai berikut
- [x] **Kustomisasi halaman login, register, dan tambah inventori semenarik mungkin.**
Semua menggunakan `base.html` sebagai template sehingga untuk mempermudah proses kustomisasi, saya melakukan hal-hal berikut pada `base.html`: 
1. Menambahkan tag `<meta name="viewport">` agar halaman web dapat menyesuaikan ukuran dan perilaku perangkat mobile atau responsive.
    ```
    {% block meta %}
        <meta charset="UTF-8" />
        <meta
            name="viewport"
            content="width=device-width, initial-scale=1.0"
        />
    {% endblock meta %}
    ```
2. Menambahkan framework Bootstrap CSS dan JS untuk mempermudah dalam kustomisasi halaman:
    ```
    <head>
        {% block meta %}
            ...
        {% endblock meta %}
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
        <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha384-KyZXEAg3QhqLMpG8r+J4jsl5c9zdLKaUk5Ae5f5b1bw6AUn5f5v8FZJoMxm6f5cH1" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.min.js" integrity="sha384-BBtl+eGJRgqQAUMxJ7pMwbEyER4l1g+O15P+16Ep7Q9Q+zqX6gSbd85u4mG4QzX+" crossorigin="anonymous"></script>
    ```
3. Untuk menggunakan font dan icon dari luar, saya menambahkan code berikut:
    ```
    <head>
        ...
        <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    </head>
    ```
4. Untuk mengganti background dan font pada semua halaman, saya menambahkan code berikut:
    ```
    <style>
        body{
        background-image: url('https://media4.giphy.com/media/J3BlD4W2r1mcK1vMWW/giphy.webp'); 
        font-family: 'Poppins', sans-serif;
        }
    </style>
    ```
Notes: Menggunakan inline dan internal CSS.

1. 👤Login & Register
    Pada `login.html` dan `register.html`, saya memanfaatkan `container` untuk mengatur penempatan masing-masing form. Selain itu, saya juga mengatur `display`, `align`, `margin`, `background image`, `border`, `radius`, `button`, dan lain-lain agar form yang ditampilkan pada halaman HTML terlihat rapi dan menarik. Saya juga menambahkan icon dari Font Awesome untuk field username dan password. Walaupun pada `base.html` sudah terdapat background-image, saya ingin membuat pada kedua halaman ini memiliki background-image yang berbeda sehingga saya menambahkan kode berikut tepat di bawah `{% block content %}`:
    ```
    <div style="display: flex; justify-content: center; align-items: center; min-height: 100vh; background-image: url(https://images7.alphacoders.com/115/1153599.jpg); background-size: cover; background-position: center; background-repeat: no-repeat; background-attachment: fixed;">
    ```

2. 📦Tambah Inventori
    Pada `create_item.html`, saya memanfaatkan card, card-title, dan card-header yang berasal dari Bootstrap untuk memberikan tampilan yang menarik untuk input new item. Selain itu, saya juga mengubah style beberapa teks untuk menonjolkan elemen penting, seperti mengatur ketebalan `<b>` dan ukuran teks `text-size`. Sama seperti halaman `login` dan `register`, saya juga mengatur `align`, `margin`, `background image`, `border`, `radius`, `button` untuk memperindah tampilan.
   

- [x] **Kustomisasi halaman daftar inventori menjadi lebih berwarna maupun menggunakan apporach lain seperti menggunakan Card.**

    Daftar inventori ditampilkan pada `main.html`, sehingga saya menambahkan styling CSS pada file tersebut. Selain mengubah tata letak tabel, saya juga menambahkan navbar `(<nav>)`. Pada navbar terdapat Nama Website "Stock El's" yang ditautkan ke halaman `main`. Selain itu, navbar juga memiliki menu `Home` dan `Inventory`. Terdapat pula dropdown yang memiliki greeting message kepada pengguna dan menampilkan beberapa informasi akun, waktu terakhir login (last login), dan opsi `Logout`

    Halaman ini menampilkan daftar invetori dalam bentuk tabel dengan kolom-kolom seperti "Name", "Price", "Size", "Amount", "Description", "Date Added", dan "Actions". Kolom "Amount" memiliki tombol plus dan minus untuk mengubah jumlah item. Terdapat pula tombol "Edit" dan tombol dengan ikon "Trash" untuk menghapus item.

    Saya juga melakukan styling CSS seperti mengatur `background-color`, `font-size`, `border`, `margin`, `color`, `display`, dll untuk menghasilkan tampilan yang lebih menarik dan terstruktur.

- [x] **Melakukan add-commit-push ke GitHub.**

Pada *root folder*, lakukan add-commit-push ke dalam repository GitHub yang telah ditetapkan di awal.

### 6. Bonus
Memberikan warna yang berbeda (teks atau background) pada baris terakhir dari item pada inventori anda menggunakan CSS.
Tabel daftar inventori terdapat pada halaman main, sehingga saya menambahkan code berikut pada main.html:
```
table tr:last-child td {
        background-color: #daf8ff;  
    }
```
- Notes: `table tr:last-child td` adalah selector CSS yang digunakan untuk menargetkan elemen-elemen <td> (sel) dalam baris terakhir (<tr>) dari sebuah tabel (<table>). Sehingga, code tersebut akan mengubah warna background dari baris terakhir tabel (dalam hal ini berisi daftar inventori).

</detail>
