import uuid

from app.services.memory_service import MemoryService


memories = [

    "User name is Rohan Gupta",

    "User's favorite language is Java",

    "User's favorite programming language is Java",

    "User's favorite database is PostgreSQL",

    "User is a Java Architect",

    "User is learning Generative AI",

    "User is building a ReAct Agent",

    "User is learning LangGraph concepts",

    "User works in Insurance Domain"

]


for memory in memories:

    MemoryService.save_memory(
        memory_id=str(
            uuid.uuid4()
        ),
        memory_text=memory
    )

    print(
        f"Saved: {memory}"
    )

print(
    "\nMemory seeding completed."
)