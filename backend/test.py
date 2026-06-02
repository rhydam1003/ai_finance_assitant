from dotenv import load_dotenv
import os

load_dotenv()

print("GEMINI:", os.getenv("GEMINI_API_KEY"))
print("GOOGLE:", os.getenv("GOOGLE_API_KEY"))