EVALUATION_CASES = [
    {
        "query": "What does a document loader do?",
        "expected_terms": [
            "files",
            "Document objects",
            "metadata",
        ],
    },
    {
        "query": "Why is chunk overlap useful?",
        "expected_terms": [
            "neighboring chunks",
            "chunk boundary",
        ],
    },
    {
        "query": "What happens during vector search?",
        "expected_terms": [
            "query vector",
            "stored chunk vectors",
            "most similar",
        ],
    },
    {
        "query": "What is the disadvantage of very small chunks?",
        "expected_terms": [
            "lose context",
        ],
    },
]