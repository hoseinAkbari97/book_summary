from ebooklib import epub
import ollama

def extract_text_from_epub(epub_file):
    book = epub.read_epub(epub_file)
    text = []
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            text.append(item.get_body_content().decode('utf-8'))
    return ' '.join(text)

# Load your EPUB file
epub_file = 'D:\drive d\python\myProjects\hamketabfilesextra\test.epub'
book_content = extract_text_from_epub(epub_file)

# Initialize Ollama client and use the model for summarization
client = ollama.Client()
response = client.run(model='llama3.2', prompt=f"Please summarize the following text: {book_content}")

# Display the summary
print(response)
