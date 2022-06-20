
from docarray import Document, DocumentArray

d = Document(uri='https://www.gutenberg.org/files/1342/1342-0.txt').load_uri_to_text()
da = DocumentArray(
    Document(text=s.strip()) for s in d.text.replace('\r\n', '').split('.') if s.strip()
)

da.summary()