# Kampus Merdeka MSIB Hybrid Programs Scraper

Script sederhana untuk scraping data lowongan magang MSIB yang available untuk hybrid.

URL untuk ambil semua data: (https://api.kampusmerdeka.kemdikbud.go.id/magang/browse/position?offset=0&limit=20)[https://api.kampusmerdeka.kemdikbud.go.id/magang/browse/position]

URL untuk ambil data by ID: (https://api.kampusmerdeka.kemdikbud.go.id/magang/browse/position/id)[https://api.kampusmerdeka.kemdikbud.go.id/magang/browse/position/{id}]

Script ini akan mengambil data lowongan yang mempunyai `activity_type` berisi `BLENDED`.

## Installation/Running Locally
1. Clone repository ini.
2. Buat virtual environment (dengan Conda, virtualenv, venv, etc) pada directory clone tersebut. Kemudian activate virtual environment tersebut. (`./Scripts/activate` apabila menggunakan virtualenv, `conda activate [nama virtual env]` apabila menggunakan Conda)
3. Jalankan `pip install -r requirements.txt`
4. Langsung jalankan script `main.py`. Output hasil akan ada di file `result.txt`. Klik link yang dituliskan di sana untuk mengunjungi halaman lowongan magang tersebut.

Thankyou :)