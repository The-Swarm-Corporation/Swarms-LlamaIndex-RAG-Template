from llamaindex_rag.agent import healthcare_summarizer

# Example usage
print(
    healthcare_summarizer.run(
        """
        What is the medical history of patient 1? Create a report with the following format:
        - Chief Complaint
        - Vitals
        - Assessment
        - Medications
        - Plan
        """,
        all_cores=True,
    )
)
