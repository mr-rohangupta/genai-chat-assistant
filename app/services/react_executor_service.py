from app.services.react_agent_service import ReActAgentService
from app.services.react_answer_service import ReActAnswerService
from app.services.react_parser_service import ReActParserService
from app.services.reflection_service import ReflectionService
from app.services.retry_prompt_service import RetryPromptService
from app.tools.memory_tool import MemoryTool
from app.tools.pdf_tool import PdfTool
from app.models.agent_state import AgentState
from app.services.planner_service import PlannerService
from app.services.plan_parser_service import PlanParserService
from app.services.step_executor_service import StepExecutorService

class ReActExecutorService:

    @staticmethod
    def execute(
            question: str
    ):

        """
        Main agent execution engine.

        Responsibilities
        ----------------
        1. Create execution plan.
        2. Ask the agent to think.
        3. Select a tool.
        4. Execute the tool.
        5. Evaluate the observation.
        6. Retry if information is insufficient.
        7. Generate final answer.

        This service acts as the orchestrator
        for the complete Planner + ReAct workflow.
        """

        # Maximum retries allowed.
        max_retries = 1

        # Agent state stores all runtime data
        # for the current execution.
        state = AgentState(
            question=question
        )

        # ==================================================
        # PLANNER
        #
        # Planner creates a high-level execution strategy
        # before the agent starts reasoning.
        #
        # Example:
        #
        # 1. Search Memory
        # 2. Search PDF
        # 3. Generate Answer
        # ==================================================

        state.plan = (
            PlannerService.create_plan(
                state.question
            )
        )

        print("\nPLAN")
        print(state.plan)

        plan_steps = (
            PlanParserService.parse(
                state.plan
            )
        )

        print("\nPLAN STEPS")

        for step in plan_steps:
            print(step)

        for step in plan_steps:

            if (
                    step.upper()
                    ==
                    "GENERATE ANSWER"
            ):
                continue

            state = (
                StepExecutorService.execute_step(
                    state,
                    step
                )
            )

        # ==================================================
        # AGENT LOOP
        #
        # Continue until:
        # 1. Answer is generated
        # 2. Retry limit is reached
        # ==================================================

        while state.retry_count <= max_retries:

            print(
                f"\nRETRY COUNT: {state.retry_count}"
            )

            # ==================================================
            # BUILD QUESTION
            #
            # First attempt uses original question.
            #
            # Retry attempts use a richer prompt
            # containing previous failures.
            # ==================================================

            if state.retry_count == 0:

                question_to_use = state.question

            else:

                question_to_use = (
                    RetryPromptService.build(
                        question=state.question,
                        action=state.action,
                        observation=state.observation,
                        reflection=state.reflection
                    )
                )

            # ==================================================
            # THINK
            #
            # Agent decides which tool should be used.
            # ==================================================

            state.thought = (
                ReActAgentService.think(
                    question_to_use
                )
            )

            print("\nTHOUGHT + ACTION")
            print(state.thought)

            # ==================================================
            # ACTION EXTRACTION
            #
            # Parse selected tool from agent output.
            # ==================================================

            state.action = (
                ReActParserService.extract_action(
                    state.thought
                )
            )

            print(
                f"\nACTION SELECTED: {state.action}"
            )

            # ==================================================
            # TOOL EXECUTION
            #
            # Execute the selected tool.
            # ==================================================

            if state.action == "memory":

                state.observation = (
                    MemoryTool.execute(
                        state.question
                    )
                )

            elif state.action == "pdf":

                state.observation = (
                    PdfTool.execute(
                        state.question
                    )
                )

            else:

                state.observation = []

            # ==================================================
            # OBSERVATION
            #
            # Tool output becomes observation.
            # ==================================================

            print("\nOBSERVATION")

            for item in state.observation:
                print(item)

            # ==================================================
            # REFLECTION
            #
            # Evaluate whether the observation
            # contains enough information.
            # ==================================================

            state.reflection = (
                ReflectionService.evaluate(
                    question=state.question,
                    observation=state.observation
                )
            )

            print("\nREFLECTION")
            print(state.reflection)

            # ==================================================
            # SUCCESS PATH
            #
            # Generate answer if evaluator
            # says enough information exists.
            # ==================================================

            if (
                    state.reflection
                    and
                    state.reflection.strip().upper() == "ENOUGH"
            ):
                state.answer = (
                    ReActAnswerService.generate_answer(
                        question=state.question,
                        observation=state.observation
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

            state.retry_count += 1

        # ==================================================
        # FALLBACK RESPONSE
        #
        # Executed when all retries fail.
        # ==================================================

        if not state.answer:
            state.answer = (
                "I could not find enough information "
                "after retrying."
            )

        print("\nFINAL ANSWER")
        print(state.answer)

        #The Below Block can be returned with single line return state

        return {
            "plan": state.plan,
            "thought": state.thought,
            "action": state.action,
            "observation": state.observation,
            "reflection": state.reflection,
            "answer": state.answer
        }