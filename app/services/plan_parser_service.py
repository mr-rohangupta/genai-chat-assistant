class PlanParserService:

    @staticmethod
    def parse(
            plan: str
    ):

        """
        Converts planner output into
        executable steps.

        Example:

        Input:
        ------
        1. Search Memory
        2. Search PDF
        3. Generate Answer

        Output:
        -------
        [
            "Search Memory",
            "Search PDF",
            "Generate Answer"
        ]
        """

        steps = []

        for line in plan.splitlines():

            line = line.strip()

            if not line:
                continue

            if "." in line:

                step = (
                    line.split(
                        ".",
                        1
                    )[1].strip()
                )

                steps.append(step)

        return steps