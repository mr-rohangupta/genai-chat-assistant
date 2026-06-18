from app.services.vector_db_service import VectorDBService

class KnowledgeBaseService:

    @staticmethod
    def load_sample_data():

        VectorDBService.collection.add(
            ids = [
                "doc1",
                "doc2",
                "doc3"
            ],
            documents=[
                "Rohan Gupta is a Technical Architect with 11 years of experience in Java, Spring Boot, Kafka, AWS and Kubernetes.",
                "Kafka is a distributed event streaming platform used for real-time data pipelines and event-driven architectures.",
                "Spring Boot is a Java framework used for building microservices and enterprise applications."
            ]
        )

        return "Knowledge Base Loaded"