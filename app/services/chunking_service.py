from typing import List


class ChunkingService:

    @staticmethod
    def split_text(
            text: str,
            chunk_size: int = 200
    ) -> List[str]:

        words = text.split()

        chunks = []

        for i in range(
                0,
                len(words),
                chunk_size
        ):

            chunk = " ".join(
                words[i:i + chunk_size]
            )

            chunks.append(
                chunk
            )

        return chunks