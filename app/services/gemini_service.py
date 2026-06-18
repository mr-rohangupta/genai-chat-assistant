import google.generativeai as genai

from app.core.config import settings

from app.core.logger import get_logger

logger = get_logger(__name__)

genai.configure(
    api_key=settings.GOOGLE_API_KEY
)

class GeminiService:

    @staticmethod
    def generate(
            prompt: str
    ) -> str:

        logger.info(
            "Calling Gemini API"
        )

        model = genai.GenerativeModel(
            settings.MODEL_NAME
        )

        response = model.generate_content(
            prompt,
            generation_config={
                "temperature": settings.TEMPERATURE,
            }
        )

        return response.text.strip()

