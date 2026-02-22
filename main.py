from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from google import genai
from google.genai import types # YENİ EKLENEN SATIR
import pdfplumber
import json
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Şimdilik herkese açık, Vercel linkini alınca burayı güncelleyeceğiz.
    allow_methods=["*"],
    allow_headers=["*"],
)
# API Anahtarını güvenli ortam değişkeninden alıyoruz
API_KEY = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)

def extract_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

@app.post("/analyze")
async def analyze_cv(
    job_description: str = Form(...),
    cv_file: UploadFile = File(...)
):
    temp_file_path = f"temp_{cv_file.filename}"
    with open(temp_file_path, "wb") as buffer:
        buffer.write(await cv_file.read())
    
    cv_text = extract_text_from_pdf(temp_file_path)
    os.remove(temp_file_path)

    prompt = f"""
    Sen bir ATS simülasyon motorusun. Aşağıdaki CV'yi, verilen İş İlanına göre analiz et.
    Çıktıyı SADECE geçerli bir JSON formatında ver. Başka hiçbir açıklama yazma.
    
    JSON Formatı:
    {{
        "skor": "X/100",
        "guc_alanlar": ["Madde 1", "Madde 2"],
        "kritik_eksikler": ["Madde 1", "Madde 2"],
        "eksik_anahtar_kelimeler": ["Kelime 1", "Kelime 2"],
        "ats_gecme_olasiligi": "Düşük/Orta/Yüksek",
        "optimize_ornekler": [
            {{"orijinal": "zayıf cümle", "optimize": "ölçülebilir cümle"}}
        ]
    }}

    İş İlanı: {job_description}
    CV Metni: {cv_text}
    """

    try:
        # JSON formatını API seviyesinde zorunlu kılıyoruz
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
            ),
        )
        
        # Artık replace veya strip yapmamıza gerek yok, doğrudan JSON geliyor
        result_json = json.loads(response.text)
        return result_json
        
    except Exception as e:
        # Hatayı konsola da yazdır ki terminalden görelim
        print(f"YAPAY ZEKA HATASI: {str(e)}")
        return {"error": "Analiz hatası", "details": str(e)}