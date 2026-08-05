from unidecode import unidecode


class TextSanitizer:

    @staticmethod
    def to_latin(text: str) -> str:
     
        if not text:
            return ""

        if not text.isascii():
            return unidecode(text)

        return text