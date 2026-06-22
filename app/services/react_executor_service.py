from app.services.react_agent_service import ReActAgentService
from app.services.react_answer_service import ReActAnswerService
from app.services.react_parser_service import ReActParserService
from app.services.reflection_service import ReflectionService
from app.services.retry_prompt_service import RetryPromptService
from app.tools.memory_tool import MemoryTool
from app.tools.pdf_tool import PdfTool


class ReActExecutorService:

    @staticmethod
    def execute(
            question: str
    ):

        """
        Main agent execution engine.

        Responsibilities
        ----------------
        1. Ask the agent to think.
        2. Select a tool.
        3. Execute the tool.
        4. Evaluate the observation.
        5. Retry if information is insufficient.
        6. Generate final answer.

        This service acts as the orchestrator
        for the complete ReAct workflow.
        """

        # Maximum number of retries.
        # Retry 0 = First attempt
        # Retry 1 = Second attempt
        max_retries = 1

        # Tracks current attempt.
        retry_count = 0

        # Final answer returned to UI.
        answer = None

        # Initialize variables outside loop
        # so they remain available after execution.
        react_response = None
        action = None
        observation = []
        reflection_result = None

        # ==================================================
        # AGENT LOOP
        #
        # Continue until:
        # 1. Answer is generated
        # 2. Retry limit is reached
        # ==================================================

        while retry_count <= max_retries:

            print(
                f"\nRETRY COUNT: {retry_count}"
            )

            # ==================================================
            # BUILD QUESTION
            #
            # First attempt uses original question.
            #
            # Retry attempts use a richer prompt
            # containing previous failures.
            # ==================================================

            if retry_count == 0:

                question_to_use = question

            else:

                question_to_use = (
                    RetryPromptService.build(
                        question=question,
                        action=action,
                        observation=observation,
                        reflection=reflection_result
                    )
                )

            # ==================================================
            # THINK
            #
            # Agent decides which tool should be used.
            # ==================================================

            react_response = (
                ReActAgentService.think(
                    question_to_use
                )
            )

            print("\nTHOUGHT + ACTION")
            print(react_response)

            # ==================================================
            # ACTION EXTRACTION
            #
            # Parse selected tool from agent output.
            # ==================================================

            action = (
                ReActParserService.extract_action(
                    react_response
                )
            )

            print(
                f"\nACTION SELECTED: {action}"
            )

            # ==================================================
            # TOOL EXECUTION
            #
            # Execute the selected tool.
            # ==================================================

            if action == "memory":

                observation = (
                    MemoryTool.execute(
                        question
                    )
                )

            elif action == "pdf":

                observation = (
                    PdfTool.execute(
                        question
                    )
                )

            else:

                observation = []

            # ==================================================
            # OBSERVATION
            #
            # Tool output becomes observation.
            # ==================================================

            print("\nOBSERVATION")

            for item in observation:
                print(item)

            # ==================================================
            # REFLECTION
            #
            # Evaluate whether the observation
            # contains enough information.
            # ==================================================

            reflection_result = (
                ReflectionService.evaluate(
                    question=question,
                    observation=observation
                )
            )

            print("\nREFLECTION")
            print(reflection_result)

            # ==================================================
            # SUCCESS PATH
            #
            # Generate answer if evaluator
            # says enough information exists.
            # ==================================================

            if (
                    reflection_result
                    and
                    reflection_result.strip().upper() == "ENOUGH"
            ):
                answer = (
                    ReActAnswerService.generate_answer(
                        question=question,
                        observation=observation
                    )
                )

                break

            # ==================================================
            # RETRY PATH
            #
            # Reflection determined that
            # information is insufficient.
            #
            # Allow the agent another attempt.
            # ==================================================

            print(
                "\nINSUFFICIENT INFORMATION. RETRYING..."
            )

            retry_count += 1

        # ==================================================
        # FALLBACK RESPONSE
        #
        # Executed when all retries fail.
        # ==================================================

        if not answer:
            answer = (
                "I could not find enough information "
                "after retrying."
            )

        print("\nFINAL ANSWER")
        print(answer)

        return {
            "thought": react_response,
            "action": action,
            "observation": observation,
            "reflection": reflection_result,
            "answer": answer
        }