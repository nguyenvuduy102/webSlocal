import os
import google.generativeai as genai
from dotenv import load_dotenv

# 1. Tải API Key từ file .env (giống như trong utils.py của bạn)
# load_dotenv()
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')

if not GEMINI_API_KEY:
    print("❌ Lỗi: Không tìm thấy GEMINI_API_KEY trong file .env!")
else:
    # 2. Cấu hình thư viện
    genai.configure(api_key=GEMINI_API_KEY)

    print("--- DANH SÁCH CÁC MODEL GEMINI BẠN CÓ THỂ DÙNG ---")
    try:
        # 3. Lấy danh sách các model hỗ trợ tạo nội dung (generateContent)
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                print(f"Model Name: {m.name}")
                print(f"Display Name: {m.display_name}")
                print(f"Description: {m.description}")
                print("-" * 30)
    except Exception as e:
        print(f"❌ Lỗi khi kết nối API: {e}")