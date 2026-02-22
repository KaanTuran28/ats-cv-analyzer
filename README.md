# ATS CV Analiz Sistemi

Bu proje, yüklenen bir PDF formatındaki özgeçmişi (CV) ve iş ilanı metnini kullanarak Applicant Tracking System (ATS) simülasyonu yapan web tabanlı bir uygulamadır. 

Yapay zeka desteğiyle anahtar kelime eşleşmesi, yetkinlik analizi ve puanlama yaparak kullanıcılara CV'lerini nasıl iyileştirebilecekleri konusunda detaylı geri bildirim sunar.

## Kullanılan Teknolojiler
* **Backend:** Python, FastAPI, Uvicorn
* **Frontend:** HTML, Tailwind CSS, JavaScript (Vanilla)
* **Yapay Zeka:** Google Gemini 2.5 Flash API
* **Veri İşleme:** PDFPlumber

## Kurulum (Yerel Ortam)
1. Gerekli kütüphaneleri kurun: `pip install -r requirements.txt`
2. `main.py` içine Gemini API anahtarınızı ekleyin.
3. Sunucuyu başlatın: `uvicorn main:app --reload`
4. `index.html` dosyasını tarayıcıda açın.  