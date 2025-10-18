# Gemini & Notion Destekli Akıllı Sözlük Otomasyonu

Bu proje, Notion'ı kişisel bir kelime öğrenme veritabanı olarak kullanarak, yeni eklenen her kelimenin anlamını ve örnek cümlesini Google Gemini API'si aracılığıyla otomatik olarak bulan ve ilgili Notion sayfasına ekleyen bir otomasyon sistemidir.

---

### 🌟 Projenin Amacı

Kişisel bir kelime öğrenme ve sözlük veritabanı oluşturma sürecini otomatize etmek. Manuel olarak anlam arama ve kopyala-yapıştır yapma ihtiyacını ortadan kaldırır.

### 🎥 Demo

<img width="1246" height="243" alt="image" src="https://github.com/user-attachments/assets/51d276bb-509c-4967-837d-7f97fa81df5b" />
<img width="542" height="207" alt="image" src="https://github.com/user-attachments/assets/19ad7cc9-549f-4f6f-aa6d-bcb5265d941a" />


---

### ⚙️ Sistemin İşleyişi

1.  **Girdi:** Notion'daki "Kelimeler" veritabanına yeni bir kelime eklenir.
2.  **Tetikleyici:** Notion'daki bu değişiklik, bir otomasyon aracı olan ActivePieces'i tetikler.
3.  **Backend Çağrısı:** ActivePieces, bu Python betiğini çalıştıran bir webhook'a isteği yönlendirir.
4.  **Yapay Zeka Sorgusu:** Python betiği, kelimeyi alarak Google Gemini API'sine gönderir ve JSON formatında anlam ve örnek cümle talep eder.
5.  **Veri İşleme:** Betik, Gemini'den gelen JSON yanıtını işler.
6.  **Güncelleme:** Son olarak, betik (veya ActivePieces) Notion API'sini kullanarak ilgili kelimenin sayfasını bulunan anlam ve örnek cümle ile günceller.

---

### 🔧 Teknik Yapı ve Kullanılan Teknolojiler

* **Arayüz & Veri Tabanı:** Notion
* **Backend & Mantık:** Python 3
* **Yapay Zeka Modeli:** Google Gemini (`gemini-1.5-flash`)
* **Entegrasyon & Otomasyon:** ActivePieces (Webhook ile)
* **Kütüphaneler:** `google-generativeai`, `requests`, `python-dotenv`, `notion-client` *(Eğer Notion'ı Python ile güncelliyorsan)*

---

### 🚀 Kurulum ve Çalıştırma

Projenin Python betiğini çalıştırmak için:

1.  **Depoyu klonlayın:**
    ```bash
    git clone [https://github.com/talhacaglar/gemini-notion-dictionary.git](https://github.com/senin-kullanici-adin/gemini-notion-dictionary.git)
    cd gemini-notion-dictionary
    ```
2.  **Gerekli kütüphaneleri yükleyin:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Ortam değişkenlerini ayarlayın:**
    * Proje ana dizininde `.env` adında bir dosya oluşturun.
    * `API_KEY` ve `WEBHOOK_URL` bilgilerinizi bu dosyaya aşağıdaki formatta ekleyin:
        ```
        API_KEY="SIZIN_GEMINI_API_ANAHTARINIZ"
        WEBHOOK_URL="SIZIN_WEBHOOK_URL"
        ```
4.  **Betiği çalıştırın:**
    ```bash
    python main.py
    ```
