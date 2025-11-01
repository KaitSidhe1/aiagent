import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from sys import argv
from sys import exit
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file

load_dotenv()
apiKey = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=apiKey)
system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""
available_functions = types.Tool(function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
    ])

def main():
    if len(argv) < 2:
        print('Usage: uv run main.py "<question?>"')
        exit(1)
    user_prompt = argv[1]

    messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),]

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents = messages,
        config=types.GenerateContentConfig( tools=[available_functions], system_instruction=system_prompt),
        )
   
    if response.function_calls:
        for call in response.function_calls:
            print (f"Calling function: {call.name}({call.args})")

    if response.text:
        print (response.text)


    if "--verbose" in argv:
        usage_metadata = response.usage_metadata
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {usage_metadata.prompt_token_count}")
        print(f"Response tokens: {usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
