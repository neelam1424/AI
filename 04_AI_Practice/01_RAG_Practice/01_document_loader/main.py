import argparse
import sys
from pathlib import Path

from src.document_loader import (
    DocumentLoader,
    UnsupportedFileTypeError,
)


def preview_documents(
    documents,
    preview_length: int = 300,
) -> None:
    """Print a readable preview of loaded documents."""

    print(f"\nLoaded {len(documents)} document object(s).\n")

    for index, document in enumerate(documents, start=1):
        preview = document.page_content[:preview_length]

        print("=" * 70)
        print(f"DOCUMENT {index}")
        print("=" * 70)

        print("\nContent preview:")
        print(preview or "[No text was extracted]")

        print("\nMetadata:")
        for key, value in document.metadata.items():
            print(f"- {key}: {value}")

        print()


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Load PDF, TXT, Markdown, or CSV files "
            "as LangChain documents."
        )
    )

    parser.add_argument(
        "file_path",
        type=Path,
        help="Path to the document to load.",
    )

    parser.add_argument(
        "--preview-length",
        type=int,
        default=300,
        help="Number of characters to preview per document.",
    )

    args = parser.parse_args()

    if args.preview_length < 0:
        print(
            "Error: --preview-length cannot be negative.",
            file=sys.stderr,
        )
        return 1

    loader = DocumentLoader()

    try:
        documents = loader.load(args.file_path)
    except (
        FileNotFoundError,
        IsADirectoryError,
        UnsupportedFileTypeError,
        RuntimeError,
    ) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    preview_documents(
        documents,
        preview_length=args.preview_length,
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())