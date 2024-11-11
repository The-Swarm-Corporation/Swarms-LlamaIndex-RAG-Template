from llamaindex_rag.agent import healthcare_summarizer

# Example usage
print(
    healthcare_summarizer.run(
        """
   Is the mental health condition for Courtney Johnson getting better. Give me a report
   """,
        all_cores=True,
    )
)
