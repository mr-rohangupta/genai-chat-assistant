from app.tools.memory_tool import MemoryTool
from app.tools.pdf_tool import PdfTool

TOOL_REGISTRY = {
    "SEARCH MEMORY": MemoryTool,
    "SEARCH PDF": PdfTool,
}