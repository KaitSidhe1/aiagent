# Warning: It does not have all the security and safety features that a production AI agent would have. The LLM can run arbitrary code that you (or it) places in the working directory... so be careful. It is for learning purposes only. 

What Does the Agent Do?

It's a CLI tool that:

Accepts a coding task (e.g., "strings aren't splitting in my app, please fix")
Chooses from a set of predefined functions to work on the task, for example:
    Scan the files in a directory
    Read a file's contents
    Overwrite a file's contents
    Execute the python interpreter on a file
Repeats step 2 until the task is complete (or it fails miserably, which is possible)

For example, I have a buggy calculator app:
~~~
> uv run main.py "fix my calculator app, its not starting correctly"
# Calling function: get_files_info
# Calling function: get_file_content
# Calling function: write_file
# Calling function: run_python_file
# Calling function: write_file
# Calling function: run_python_file
# Final response:
# Great! The calculator app now seems to be working correctly. The output shows the expression and the result in a formatted way.
~~~
