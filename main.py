import os
import requests
import json
import google.generativeai as genai

from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
webhook_url = os.getenv("WEBHOOK_URL")

if not api_key or not webhook_url:
    print("HATA: Lütfen proje klasöründe .env adında bir dosya oluşturup içine API_KEY ve WEBHOOK_URL bilgilerinizi ekleyin.")
    exit()

try:
    genai.configure(api_key=api_key)
except Exception as e:
    print(f"Hata: API anahtarı yapılandırılamadı. {e}")
    exit()

def yapay_zekadan_bilgi_al(kelime: str) -> tuple[str, str]:
    print(f"'{kelime}' kelimesi için Gemini'den bilgi alınıyor...")
    model = genai.GenerativeModel('gemini-2.5-flash') # Model adını güncel tutmak iyi bir pratiktir
    prompt = f"""
    Sen bir sözlük asistanısın. Sana verilen kelimenin anlamını ve o kelimeyle ilgili bir örnek cümleyi içeren bir JSON nesnesi oluştur.
    Kelime: '{kelime}'
    JSON Formatı: {{"anlam": "kelimenin anlamı", "cumle": "örnek cümle"}}
    """
    try:
        generation_config = genai.GenerationConfig(response_mime_type="application/json")
        response = model.generate_content(prompt, generation_config=generation_config)
        data = json.loads(response.text)
        anlam = data.get("anlam", "Anlam bulunamadı.")
        cumle = data.get("cumle", "Örnek cümle bulunamadı.")
        return anlam, cumle
    except Exception as e:
        print(f"Google Gemini API Hatası: {e}")
        return "Hata", "API ile iletişim kurulamadı veya yanıt ayrıştırılamadı."

def webhook_gonder(kelime: str, anlam: str, cumle: str):
    """
    Alınan bilgileri ActivePieces Webhook'una gönderir.
    """
    print("Bilgiler ActivePieces'e gönderiliyor...")

    payload = {
        "kelime": kelime,
        "anlam": anlam,
        "cumle": cumle
    }
    
    try:
        response = requests.post(webhook_url, json=payload, timeout=10)
        response.raise_for_status()  
        print("✅ Başarılı: Bilgiler ActivePieces webhook'una gönderildi!")
    except requests.exceptions.RequestException as e:
        print(f"❌ Hata: Webhook'a gönderim başarısız oldu. Hata: {e}")

# --- 3️⃣ ANA PROGRAM AKIŞI --- (DEĞİŞİKLİKLER BURADA)
def main():
    """
    Kullanıcıdan sürekli olarak kelime alır ve çıkış komutu girilene kadar çalışır.
    """
    while True:
        # Kullanıcıya çıkış seçeneğini de belirterek kelime sor
        kelime = input("Anlamını öğrenmek istediğiniz kelimeyi girin (Çıkmak için 'çık', 'q' veya 'exit' yazın): ").strip()

        # Kullanıcı çıkmak isterse döngüyü sonlandır
        if kelime.lower() in ['çık', 'q', 'exit']:
            print("Programdan çıkılıyor. Hoşça kalın!")
            break

        # Eğer kullanıcı bir şey girmeden Enter'a basarsa uyar ve döngüye devam et
        if not kelime:
            print("Lütfen geçerli bir kelime girin.")
            continue # Döngünün başına dön

        anlam, cumle = yapay_zekadan_bilgi_al(kelime)
        
        if anlam != "Hata":
            webhook_gonder(kelime, anlam, cumle)
            # Çıktıyı daha düzenli hale getir
            print("\n--- SONUÇ ---")
            print(f"Kelime       : {kelime}")
            print(f"Bulunan Anlam: {anlam}")
            print(f"Örnek Cümle  : {cumle}")
            print("-------------\n")

if __name__ == "__main__":
    main()
