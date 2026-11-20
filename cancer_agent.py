from rag_pipeline import ask_medical_ai


def cancer_ai_agent(patient_question):
    """
    Cancer RAG assistant.

    Uses the cancer PDF knowledge base through the RAG pipeline.
    This provides educational information and does not confirm
    a medical diagnosis.
    """

    if not patient_question or not patient_question.strip():
        return "Please enter your symptoms or medical question."

    response = ask_medical_ai(patient_question)

    return response 