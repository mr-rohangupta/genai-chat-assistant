from app.tools.memory_tool import MemoryTool
from app.tools.pdf_tool import PdfTool
from app.services.tool_selection_service import ToolSelectionService

class ToolRouter:

    @staticmethod
    def route(
            query: str
    ):

        selected_tool = (
            ToolSelectionService.select_tool(
                query
            )
        )

        print(
            f"\nTOOL SELECTED: {selected_tool.upper()}"
        )

        if selected_tool == "memory":
            return MemoryTool.execute(
                query
            )

        return PdfTool.execute(
            query
        )