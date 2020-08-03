# One Health Laboratory Network website project

Website yang di pakai untuk laboratorium membuat sejumlah laporan mengenai laboratorium mereka

## Getting Started

Instruksi dibawah ini akan menjelaskan bagaimana cara menjalankan website ini dalam lokal komputer


### Installing

Bagaimana cara menjalankan di local komputer masing-masing

Membuat Virtual Environment di dalam laptop kita (pastikan di dalam direktori dimana project kita berada)

```
python3 -m venv env
source ./env/bin/activate 
```

Setelah itu, kita menginstall segala dependency yang kita butuhkan (yang tertulis dalam `settings.py`)

```
pip3 install -r requirements.txt
```

Jika kita menambahkan dependency lagi, kita jangan lupa untuk memasukan ke dalam file `requirements.txt` (yang tertulis dalam `settings.py`). Setelah itu kita dapat menginstallnya kembali dengan petunjuk yang tepat berada diatas poin ini.

```
pip freeze > requirements.txt
```

Kita bisa run website ini dalam local komputer dengan alamat port http://127.0.0.1:8000/ atau localhost:8000

```
python3 manage.py runserver
```

Jangan lupa, jika ada perubahan di dalam file `models.py` untuk selalu melakukan migration setiap kalinya

```
python3 manage.py makemigrations
python3 manage.py migrate
```
Untuk menjalankan fitur Reset Password dengan settingan `settings.py` di baris paling bawah, gunakan perintah dibawah ini dan dijalankan pada tab terminal yang berbeda dari dijalankannya web django --> `python3 manage.py runserver`

```
python -m smtpd -n -c DebuggingServer localhost:1025
```