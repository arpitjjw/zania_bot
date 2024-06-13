import PyPDF2

class DocumentProcessor:
    def __init__(self, file_path):
        self.file_path = file_path

    def extract_text(self):
        text = ""
        with open(self.file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text()
        return text