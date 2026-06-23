from app.tools.memory_tool import MemoryTool


def main():

    print("=" * 60)
    print("MEMORY TOOL TEST")
    print("=" * 60)

    question = input(
        "\nEnter Question: "
    )

    print(
        f"\nQuestion: {question}"
    )

    print(
        "\nExecuting Memory Tool..."
    )

    result = (
        MemoryTool.execute(
            question
        )
    )

    print("\nRESULT TYPE")
    print(type(result))

    print(
        f"\nTotal Results: {len(result)}"
    )

    print("\nMEMORY RESULTS")
    print("-" * 60)

    if not result:

        print(
            "NO RESULTS FOUND"
        )

    else:

        for index, item in enumerate(
                result,
                start=1
        ):

            print(
                f"{index}. {item}"
            )

    print("\nDONE")


if __name__ == "__main__":
    main()