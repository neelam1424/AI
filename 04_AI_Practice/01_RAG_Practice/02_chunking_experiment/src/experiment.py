from __future__ import annotations

from dataclasses import dataclass

from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import (
    RecursiveCharacterTextSplitter,
)


@dataclass
class RetrievalResult:
    chunk_size: int
    query: str
    retrieved_text: str
    hit: bool
    chunk_count: int


def contains_expected_terms(
    text: str,
    expected_terms: list[str],
) -> bool:
    normalized = text.lower()

    return all(
        term.lower() in normalized
        for term in expected_terms
    )


def run_chunk_size_experiment(
    document: Document,
    chunk_sizes: list[int],
    evaluation_cases: list[dict],
    top_k: int = 3,
) -> list[RetrievalResult]:
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    results: list[RetrievalResult] = []

    for chunk_size in chunk_sizes:
        overlap = max(10, int(chunk_size * 0.10))

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=overlap,
        )

        chunks = splitter.split_documents([document])

        vector_store = FAISS.from_documents(
            chunks,
            embeddings,
        )

        for case in evaluation_cases:
            retrieved = vector_store.similarity_search(
                case["query"],
                k=top_k,
            )

            combined_text = "\n\n".join(
                item.page_content
                for item in retrieved
            )

            hit = contains_expected_terms(
                combined_text,
                case["expected_terms"],
            )

            results.append(
                RetrievalResult(
                    chunk_size=chunk_size,
                    query=case["query"],
                    retrieved_text=combined_text,
                    hit=hit,
                    chunk_count=len(chunks),
                )
            )

    return results