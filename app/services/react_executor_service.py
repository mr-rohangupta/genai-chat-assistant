from app.services.react_agent_service import ReActAgentService
from app.services.react_parser_service import ReActParserService
from app.tools.memory_tool import MemoryTool
from app.tools.pdf_tool import PdfTool
from app.services.react_answer_service import ReActAnswerService

class ReActExecutorService:

    @staticmethod
    def execute(
            question: str
    ):

        react_response = (
            ReActAgentService.think(question)
        )

        print("\nTHOUGHT + ACTION")
        print(react_response)

        action = (
            ReActParserService.extract_action(
                react_response
            )
        )
        print(
            f"\nACTION SELECTED: {action}"
        )
        if action == "memory":
            observation = (
                MemoryTool.execute(
                    question
                )
            )

        else:
            observation = (
                PdfTool.execute(
                    question
                )
            )

        print("\nOBSERVATION")

        for item in observation:
            print(item)

        answer = (
            ReActAnswerService.generate_answer(
                question=question,
                observation=observation
            )
        )

        print("\nFINAL ANSWER")
        print(answer)

        return {
            "thought": react_response,
            "action": action,
            "observation": observation,
            "answer": answer
        }