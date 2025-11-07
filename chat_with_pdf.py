import os
import sys
import argparse
from dotenv import load_dotenv
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex

def setup_environment():
    """Loads environment variables and sets the OpenAI API key."""
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY not found in .env file.")
        sys.exit(1)
    os.environ["OPENAI_API_KEY"] = api_key
    print("✅ OpenAI API key loaded.")

def main():
    """Main function to run the Chat with PDF application."""
    parser = argparse.ArgumentParser(description="Chat with a PDF document using LlamaIndex.")
    parser.add_argument("--pdf", required=True, help="Path to the PDF file.")
    parser.add_argument("--query", required=True, help="The question to ask the document.")
    args = parser.parse_args()

    pdf_path = args.pdf
    user_query = args.query

    if not os.path.exists(pdf_path):
        print(f"Error: The file '{pdf_path}' was not found.")
        sys.exit(1)

    print(f"\nLoading document: {pdf_path}...")
    try:
        reader = SimpleDirectoryReader(input_files=[pdf_path])
        documents = reader.load_data()
        print(f"✅ Document loaded successfully. It was split into {len(documents)} chunks.")
    except Exception as e:
        print(f"Error loading PDF: {e}")
        sys.exit(1)

    print("\nIndexing the document... (This may take a moment)")
    try:
        index = VectorStoreIndex.from_documents(documents)
        print("✅ Index created successfully.")
    except Exception as e:
        print(f"Error creating index: {e}")
        sys.exit(1)

    print(f"\nQuerying the index with: '{user_query}'")
    try:
        query_engine = index.as_query_engine()
        response = query_engine.query(user_query)
        print("\n--- Answer ---")
        print(str(response))
        print("\n✅ Query complete.")
    except Exception as e:
        print(f"Error during query: {e}")
        sys.exit(1)

if __name__ == "__main__":
    setup_environment()
    main()