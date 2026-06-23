from app.models.agent_state import AgentState
from app.tools.memory_tool import MemoryTool
from app.tools.pdf_tool import PdfTool

class StepExecutorService:

    @staticmethod
    def execute_step(
            state: AgentState,
            step: str
    ):
        """
        Executes a single planner step.

        Responsibilities
        ----------------
        1. Identify the tool associated
           with the planner step.

        2. Execute the appropriate tool.

        3. Store tool output inside
           AgentState.observation.

        4. Track execution progress using:

           - current_step
           - completed_steps

        This service acts as the execution
        layer of the Planner-Executor pattern.
        """

        state.current_step = step

        print(
            f"\nEXECUTING STEP: {step}"
        )

        if step.upper() == "SEARCH MEMORY":

            result = (
                MemoryTool.execute(
                    state.question
                )
            )

            state.observation.extend(
                result
            )
        elif step.upper() == "SEARCH PDF":

            result = (
                PdfTool.execute(
                    state.question
                )
            )

            state.observation.extend(
                result
            )

        state.completed_steps.append(step)

        print(
            f"\nCOMPLETED STEPS: "
            f"{state.completed_steps}"
        )

        return state