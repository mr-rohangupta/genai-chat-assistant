class ReActParserService:

    @staticmethod
    def extract_action(
            react_response: str
    ):

        lines = react_response.splitlines()

        for line in lines:

            if line.startswith(
                    "ACTION:"
            ):

                return (
                    line.replace(
                        "ACTION:",
                        ""
                    )
                    .strip()
                    .lower()
                )

        return None