from pathlib import Path

from langchain_community.document_loaders import (
    CSVLoader,
    PyPDFLoader,
    TextLoader,
)
from langchain_core.documents import Document


class UnsupportedFileTypeError(ValueError):
    """Raised when no loader is available for a file type."""


class DocumentLoader:
    """Load PDF, TXT, Markdown, and CSV files as LangChain documents."""

    SUPPORTED_EXTENSIONS = {".pdf", ".txt", ".md", ".csv"}

    def load(self, file_path: str | Path) -> list[Document]:
        """
        Load a file and return LangChain Document objects.

        Args:
            file_path:
                Path to a supported local document.

        Returns:
            A list of LangChain Document objects.

        Raises:
            FileNotFoundError:
                If the path does not exist.

            IsADirectoryError:
                If the path refers to a directory.

            UnsupportedFileTypeError:
                If the extension is unsupported.

            RuntimeError:
                If the selected loader cannot parse the file.
        """
        path = Path(file_path).expanduser().resolve()

        self._validate_path(path)

        loader = self._create_loader(path)

        try:
            documents = loader.load()
        except Exception as exc:
            raise RuntimeError(
                f"Failed to load '{path.name}': {exc}"
            ) from exc

        return self._normalize_metadata(
            documents=documents,
            path=path,
        )

    def _validate_path(self, path: Path) -> None:
        """Validate that the path is a supported file."""

        if not path.exists():
            raise FileNotFoundError(
                f"File does not exist: {path}"
            )

        if not path.is_file():
            raise IsADirectoryError(
                f"Expected a file but received: {path}"
            )

        if path.suffix.lower() not in self.SUPPORTED_EXTENSIONS:
            supported = ", ".join(
                sorted(self.SUPPORTED_EXTENSIONS)
            )

            raise UnsupportedFileTypeError(
                f"Unsupported file type '{path.suffix}'. "
                f"Supported extensions: {supported}"
            )

    def _create_loader(
        self,
        path: Path,
    ) -> PyPDFLoader | TextLoader | CSVLoader:
        """Create the correct LangChain loader."""

        extension = path.suffix.lower()

        if extension == ".pdf":
            return PyPDFLoader(str(path))

        if extension in {".txt", ".md"}:
            return TextLoader(
                str(path),
                encoding="utf-8",
                autodetect_encoding=True,
            )

        if extension == ".csv":
            return CSVLoader(
                file_path=str(path),
                encoding="utf-8",
                autodetect_encoding=True,
            )

        # This is defensive because _validate_path already checks it.
        raise UnsupportedFileTypeError(
            f"No loader configured for '{extension}'."
        )

    def _normalize_metadata(
        self,
        documents: list[Document],
        path: Path,
    ) -> list[Document]:
        """Add consistent metadata to every loaded document."""

        for index, document in enumerate(documents):
            document.metadata.update(
                {
                    "source": str(path),
                    "file_name": path.name,
                    "file_extension": path.suffix.lower(),
                    "document_index": index,
                }
            )

        return documents