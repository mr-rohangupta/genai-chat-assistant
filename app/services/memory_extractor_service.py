from app.services.gemini_service import GeminiService

class MemoryExtractorService:

    @staticmethod
    def extract_memory(
            message: str
    ):
        prompt = f"""
        You are a memory extraction assistant.

        Your job is to determine whether the user's message
        contains information worth remembering.

        Examples:

        User:
        My name is Rohan Gupta

        Output:
        STORE: User name is Rohan Gupta


        User:
        I work as a Java Architect

        Output:
        STORE: User works as a Java Architect


        User:
        I live in Pune

        Output:
        STORE: User lives in Pune


        User:
        What is Kafka?

        Output:
        NO_MEMORY


        User:
        Explain Spring Boot

        Output:
        NO_MEMORY


        Current User Message:

        {message}

        Return ONLY one of the following:

        STORE: <memory>

        OR

        NO_MEMORY
        """

        response = (
            GeminiService.generate(
                prompt
            )
        )

        return response.strip()