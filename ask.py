import openai
import yaml
import os
from schema import Project
from dotenv import load_dotenv

load_dotenv()


base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
client = openai.Client(api_key=os.getenv("LLM_API_KEY"), base_url=base_url)

def generate_android_app(user_intent):
    global client
    """
    Generate Android app code based on the user's intent.

    Args:
        user_intent (str): The user's description of what they want to build

    Returns:
        structured_out: The parsed response containing the generated files
    """
    # Configure API key

    system = ("""
You are an AI assistant specializing in Android app development. Your task is to generate and improve an Android app's UI and functionality based on the provided .java and .xml files above. The modifications should align with the user's needs while ensuring a visually appealing and well-structured design.

Requirements:

Refer to the original .java and .xml code above to make precise and context-aware modifications.

Ensure an aesthetically pleasing UI with proper spacing, alignment, and readability. No elements should overlap.

Follow Android best practices, maintaining modularity, efficiency, and proper resource management.

Comment on significant changes to improve code readability and maintainability.

Use Material Design components where applicable to enhance the user experience.

Do not remove existing functionalities unless explicitly requested.

Generate only the modified .java and .xml sections, ensuring they integrate seamlessly with the existing code.

User Input Format:
Existing .java file(s) (code provided before the prompt)
Existing .xml layout file(s) (code provided before the prompt)
Existing .xml theme file(s) (if applicable)

Modification requirements (clear instructions on changes needed)

Expected Output:
Updated .java code with modifications based on the request.

Updated .xml code reflecting UI changes.

Brief explanation of the changes made and how they improve the app.
    """)

    template_structure= {}
    with open("template/template.yaml", "r") as stream:
        try:
            template_structure = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

    if "files" not in template_structure:
        raise Exception("Invalid template structure. 'files' key is missing.")
    files = template_structure["files"]
    app = files["app"]

    gradle = files["gradle"]
    logic = app["logic"]
    manifest = app["manifest"]
    layout = app["layout"]
    themes = app["themes"]

    user_msg = f"""
I want to perform these:
{user_intent}

Here are important files in my project:
    """

    def put_files_in_prompt(listing: list):
        nonlocal user_msg
        for fn in listing:
            file = os.path.join("template", "MyApp", fn)
            with open(file, "r") as f:
                contents = f.read()
            user_msg += f"""
    - {fn}:
    ```
    {contents}
    ```
    """

    user_msg += """
Java logic files:
    """
    put_files_in_prompt(logic)

    user_msg += """
XML layout files:
    """
    put_files_in_prompt(layout)

    user_msg += """
XML theme files:
    """
    put_files_in_prompt(themes)

    user_msg += """
Manifest file:
"""
    put_files_in_prompt(manifest)

    response = client.beta.chat.completions.parse(
        model="gemini-2.0-flash",
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user_msg},
        ],
        response_format=Project,
    )

    structured_out = response.choices[0].message.parsed
    return structured_out

# Example usage:
if __name__ == "__main__":
    user_intent = """
I want to create a new Android timer app that allows users to set timers. The app should have a simple and intuitive interface with the following features:
- Users can start, pause, and reset timers, and can set it to a custom duration of their choosing.
- The app should provide visual and audio notifications when a timer expires.
- Users can save and load timer configurations.
    """

    result = generate_android_app(user_intent)

    # Display the results
    s_files = result.files
    for file in s_files:
        print(file.relative_path)
        print(file.content)
        # If you want to write the files:
        # with open(file.relative_path, "w") as f:
        #     f.write(file.content)
