import os
import shutil
import tempfile
from pathlib import Path
from ask import generate_android_app

def transform_android_app(user_intent, template_path="./template/MyApp", output_dir=None):
    """
    Transform an Android app template based on user intent.

    Args:
        user_intent (str): User's description of what they want to build
        template_path (str): Path to the template directory
        output_dir (str): Optional custom output directory path

    Returns:
        str: Path to the transformed directory
    """
    # Ensure the template directory exists
    if not os.path.exists(template_path):
        raise FileNotFoundError(f"Template directory not found at {template_path}")

    # Create a temporary directory if output_dir is not specified
    if output_dir is None:
        tmp_dir = tempfile.mkdtemp(prefix="android_app_")
        output_app_path = os.path.join(tmp_dir, "MyApp")
    else:
        # Make sure the directory exists
        os.makedirs(output_dir, exist_ok=True)
        output_app_path = os.path.join(output_dir, "MyApp")

    # Copy the template to the new directory
    shutil.copytree(template_path, output_app_path)

    # Generate the Android app based on user intent
    generated_files = generate_android_app(user_intent).files

    # Transform the copied directory with the generated files
    for file_obj in generated_files:
        # Get the full path of the file
        file_path = os.path.join(output_app_path, file_obj.relative_path)

        # Ensure the directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # Write the content to the file
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(file_obj.content)

    print(f"Android app transformed successfully. Output directory: {output_app_path}")
    return output_app_path

if __name__ == "__main__":
    user_intent = """
    Build me a calculator app android

    """

    transformed_path = transform_android_app(user_intent)
    print(f"Transformed app is available at: {transformed_path}")
