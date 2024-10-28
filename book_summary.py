from ebooklib import epub
import ebooklib
import ollama
from ollama import Client

def extract_text_from_epub(epub_file):
    book = epub.read_epub(epub_file)
    text = []
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            text.append(item.get_body_content().decode('utf-8'))
    return ' '.join(text)

# Load your EPUB file
epub_file = 'C:/Users/Hossein/OneDrive/Desktop/test.epub'
book_content = extract_text_from_epub(epub_file)

# Initialize Ollama client and use the model for summarization
client = Client(host="http://localhost:11434")
# response = client.run(model='llama3.2', prompt=f"Please summarize the following text: {book_content}")
# client = Client(host='http://localhost:11434')
response = client.chat(model='llama3.2', messages=[
  {
    'role': 'user',
    'content': f"Please summarize the following text: {book_content}",
  },
])

# Display the summary
print(response)
