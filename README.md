# ATS CV Analyzer

![Python](https://img.shields.io/badge/python-3.x-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-009688)
![Gemini](https://img.shields.io/badge/AI-Gemini_2.5_Flash-8e75b2)
![License](https://img.shields.io/badge/license-MIT-green)

<p align="center"><b><a href="#english">English</a></b> · <b><a href="#türkçe">Türkçe</a></b></p>

**Live demo:** https://ats-cv-analyzer-five.vercel.app

---

## English

A web app that simulates an Applicant Tracking System (ATS): you upload a résumé (CV) as a PDF and paste a job posting, and it does keyword matching, competency analysis and scoring with AI, then gives detailed feedback on how to improve the CV.

### Features

- Upload a CV as PDF and paste the job-posting text.
- Keyword matching between the CV and the posting.
- Competency analysis and an ATS-style score.
- Actionable feedback on how to improve the CV.

### Tech stack

- **Backend:** Python, FastAPI, Uvicorn
- **Frontend:** HTML, Tailwind CSS, vanilla JavaScript
- **AI:** Google Gemini 2.5 Flash API
- **PDF parsing:** pdfplumber

### Setup (local)

```bash
pip install -r requirements.txt
```

Set your Gemini API key as an environment variable (the app reads `GEMINI_API_KEY`; do not hard-code it):

```bash
# Windows (PowerShell)
$env:GEMINI_API_KEY="your_key"
# macOS/Linux
export GEMINI_API_KEY="your_key"
```

Then start the server and open the front end:

```bash
uvicorn main:app --reload
# open index.html in a browser
```

### License

MIT — see [LICENSE](./LICENSE).

---

## Türkçe

Bir Başvuru Takip Sistemi (ATS) simülasyonu yapan web uygulaması: PDF formatında bir özgeçmiş (CV) yükler, iş ilanı metnini yapıştırırsınız; uygulama yapay zekâ ile anahtar kelime eşleşmesi, yetkinlik analizi ve puanlama yapıp CV'nizi nasıl iyileştirebileceğinize dair detaylı geri bildirim verir.

### Özellikler

- CV'yi PDF olarak yükleme ve iş ilanı metnini yapıştırma.
- CV ile ilan arasında anahtar kelime eşleşmesi.
- Yetkinlik analizi ve ATS tarzı puanlama.
- CV'yi iyileştirmek için uygulanabilir geri bildirim.

### Teknolojiler

- **Backend:** Python, FastAPI, Uvicorn
- **Frontend:** HTML, Tailwind CSS, vanilla JavaScript
- **Yapay zekâ:** Google Gemini 2.5 Flash API
- **PDF işleme:** pdfplumber

### Kurulum (yerel)

```bash
pip install -r requirements.txt
```

Gemini API anahtarınızı bir ortam değişkeni olarak verin (uygulama `GEMINI_API_KEY` okur; koda gömmeyin):

```bash
# Windows (PowerShell)
$env:GEMINI_API_KEY="anahtariniz"
# Mac/Linux
export GEMINI_API_KEY="anahtariniz"
```

Ardından sunucuyu başlatıp ön yüzü açın:

```bash
uvicorn main:app --reload
# index.html dosyasını tarayıcıda açın
```

### Lisans

MIT — bkz. [LICENSE](./LICENSE).
