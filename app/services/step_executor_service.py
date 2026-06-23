from unittest import result

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
               Executes one step from a plan.

               Updates AgentState with
               observations and progress.
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
        elif step.upper() == "PDF":

            result = (
                PdfTool.execute(
                    state.question
                )
            )

            state.observation.extend(
                result
            )

        state.completed_steps.append(step)

        return state