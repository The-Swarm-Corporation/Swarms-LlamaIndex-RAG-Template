from llamaindex_rag.memory import LlamaIndexDB

# Example usage
llama_index_db = LlamaIndexDB(
    data_dir="docs",
    filename_as_id=True,
    recursive=True,
    required_exts=[".txt", ".pdf", ".docx"],
    similarity_top_k=10
)

llama_index_db.query(
    "What is the medical history of patient 1?",
    streaming=True,
    response_mode="compact"
)
