import google.generativeai as genai

from app.core.config import settings

genai.configure(
    api_key=settings.GOOGLE_API_KEY
)

for model in genai.list_models():

    if "generateContent" in model.supported_generation_methods:
        print(model.name)