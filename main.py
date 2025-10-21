import os
from dotenv import load_dotenv
from google import genai
from sys import argv
from sys import exit

load_dotenv()
apiKey = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=apiKey)

def main():
    if len(argv) < 2:
        print('Usage: uv run main.py "<question?>"')
        exit(1)
    content = argv[1]

    response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents = content,
    )

    print(response.text)
    usage_metadata = response.usage_metadata
    print(f"Prompt tokens: {usage_metadata.prompt_token_count}")
    print(f"Response tokens: {usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
