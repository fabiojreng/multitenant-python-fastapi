import re


class Document:
    def __init__(self, document: str) -> None:
        self.__document = self.__validate_document(document)

    def __validate_document(self, document: str) -> str:
        document = re.sub(r"\s|\D", "", document)
        if not document.isdigit():
            raise ValueError("Only numeric values can be entered")

        if len(document) == 11:
            document = re.sub(
                r"(\d{3})(\d{3})(\d{3})(\d{2})",
                r"\1.\2.\3-\4",
                document,
            )
        elif len(document) == 14:
            document = re.sub(
                r"(\d{2})(\d{3})(\d{3})(\d{4})(\d{2})",
                r"\1.\2.\3/\4-\5",
                document,
            )
        else:
            raise ValueError("Document is not valid")
        return document

    def get_value(self):
        return self.__document
