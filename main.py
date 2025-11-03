import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.call_function import available_functions
from functions.call_function import call_function

system_prompt = """
    You are a helpful AI coding agent.

    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

    - List files and directories
    - Read file contents
    - Execute Python files with optional arguments
    - Write or overwrite files

    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """
MAX_ITERS = 20

def main():
    
    load_dotenv()
    apiKey = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=apiKey)
    verbose = "--verbose" in sys.argv

    args = []
    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I fix the calculator?"')
        sys.exit(1)

    user_prompt = " ".join(args)    
    if verbose:
        print(f"User prompt: {user_prompt}\n")   

    messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),]


    for i in range(MAX_ITERS + 1):
        if i == MAX_ITERS:         
            print(f"Maximum iterations ({MAX_ITERS}) reached.")
            sys.exit(1)

        try:   
            final_response = generate_content(client, messages, verbose)
            if final_response:
                print("Final response:")
                print(final_response)
                break

        except Exception as e:
            print(f"Error in generate_content: {e}")


    
    
def generate_content(client, messages, verbose):    
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents = messages,
        config=types.GenerateContentConfig( tools=[available_functions], system_instruction=system_prompt),
        )
    
    if verbose:
        usage_metadata = response.usage_metadata
        print(f"Prompt tokens: {usage_metadata.prompt_token_count}")
        print(f"Response tokens: {usage_metadata.candidates_token_count}")

    if response.candidates:
        for candidate in response.candidates:
            messages.append(candidate.content)

    if not response.function_calls:
        return response.text
    
    function_responses = []    
    for call in response.function_calls:
        function_call_result = call_function(call, verbose)
        if (not function_call_result.parts 
            or not function_call_result.parts[0].function_response):
            raise Exception("ERROR: Missing call_function response")
            
        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")
        function_responses.append(function_call_result.parts[0])

    if not function_responses:
        raise Exception("ERROR: no function responses generated, exiting.")

    messages.append(types.Content(role="user", parts=function_responses))



if __name__ == "__main__":
    main()
