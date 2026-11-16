# Latihan 5.1 - Calling an API, Processing JSON, Managing Keys

**Kasus:** TokoKu menerima turis asing. Kasir ingin tahu harga dalam USD, SGD, dan JPY.

1. Panggil `https://open.er-api.com/v6/latest/IDR` dengan `requests.get(url, timeout=10)`.
2. Cek `status_code` dan isi JSON (`response.json()`).
3. Ambil kurs USD, SGD, JPY dari key `rates`.
4. Konversikan harga menu ke mata uang tersebut.
5. Bila internet mati, pakai cadangan `kurs_cadangan.json`.

## Managing Keys
1. Salin `.env.example` menjadi `.env`, isi `TOKOKU_API_KEY=...`.
2. Baca dengan `os.getenv("TOKOKU_API_KEY")` setelah `load_dotenv()`.
3. **Jangan pernah** menulis key di kode atau meng-upload `.env` ke GitHub.
