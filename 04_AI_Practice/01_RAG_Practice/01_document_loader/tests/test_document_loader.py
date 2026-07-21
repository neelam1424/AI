from pathlib import Path

import pytest

from src.document_loader import (
    DocumentLoader,
    UnsupportedFileTypeError,
)


@pytest.fixture
def loader() -> DocumentLoader:
    return DocumentLoader()


def test_load_txt_file(
    loader: DocumentLoader,
    tmp_path: Path,
) -> None:
    file_path = tmp_path / "sample.txt"
    file_path.write_text(
        "RAG combines retrieval and generation.",
        encoding="utf-8",
    )

    documents = loader.load(file_path)

    assert len(documents) == 1
    assert "retrieval and generation" in (
        documents[0].page_content
    )
    assert documents[0].metadata["file_name"] == "sample.txt"
    assert documents[0].metadata["file_extension"] == ".txt"


def test_load_markdown_file(
    loader: DocumentLoader,
    tmp_path: Path,
) -> None:
    file_path = tmp_path / "notes.md"
    file_path.write_text(
        "# RAG\n\nRetrieval finds relevant context.",
        encoding="utf-8",
    )

    documents = loader.load(file_path)

    assert len(documents) == 1
    assert "# RAG" in documents[0].page_content
    assert documents[0].metadata["file_extension"] == ".md"


def test_load_csv_file(
    loader: DocumentLoader,
    tmp_path: Path,
) -> None:
    file_path = tmp_path / "employees.csv"
    file_path.write_text(
        "name,department\n"
        "Neelam,AI\n"
        "Alex,Backend\n",
        encoding="utf-8",
    )

    documents = loader.load(file_path)

    assert len(documents) == 2
    assert "Neelam" in documents[0].page_content
    assert "AI" in documents[0].page_content
    assert documents[0].metadata["file_extension"] == ".csv"


def test_missing_file_raises_error(
    loader: DocumentLoader,
    tmp_path: Path,
) -> None:
    missing_file = tmp_path / "missing.txt"

    with pytest.raises(FileNotFoundError):
        loader.load(missing_file)


def test_unsupported_file_raises_error(
    loader: DocumentLoader,
    tmp_path: Path,
) -> None:
    file_path = tmp_path / "image.png"
    file_path.write_bytes(b"fake image data")

    with pytest.raises(UnsupportedFileTypeError):
        loader.load(file_path)


def test_directory_raises_error(
    loader: DocumentLoader,
    tmp_path: Path,
) -> None:
    with pytest.raises(IsADirectoryError):
        loader.load(tmp_path)