import os
import streamlit as st
import pathlib
import time
import shutil
from build import build_gradle_project

st.set_page_config(
    page_title="Code",
    page_icon="💡",
)

if "path" not in st.session_state:
    st.warning("Code not generated yet. You will be redirected back in 3 seconds...")
    time.sleep(3)
    st.switch_page("pages/chat.py")

# Set this to the directory you want to browse
folder = st.session_state.path if "path" in st.session_state else "."
FILE_PATH = os.path.expanduser(folder)  # Default to home directory, change as needed

def get_language_from_filename(filename):
    # Extract the file extension
    ext = pathlib.Path(filename).suffix.lower()

    # Map common extensions to Streamlit-supported languages
    extension_map = {
        ".py": "python",
        ".js": "javascript",
        ".ts": "typescript",
        ".java": "java",
        ".c": "c",
        ".cpp": "cpp",
        ".cs": "csharp",
        ".html": "html",
        ".css": "css",
        ".json": "json",
        ".yaml": "yaml",
        ".yml": "yaml",
        ".xml": "xml",
        ".sql": "sql",
        ".sh": "bash",
        ".r": "r",
        ".go": "go",
        ".php": "php",
        ".swift": "swift",
        ".rb": "ruby",
    }

    # Return mapped language or default to "plaintext"
    return extension_map.get(ext, "plaintext")
def main():
    st.title("Results")

    # Layout with columns for file browser and content
    col1, col2 = st.columns([1, 3])

    # File browser in the left pane
    with col1:
        st.header("File Browser")
        selected_file = file_browser(FILE_PATH)

    # File content and buttons in the right pane
    with col2:
        # Create a row for the header and buttons

        # Add Accept/Reject buttons to the top
        cols = st.columns([3, 1, 1])
        with cols[1]:
            accept_button = st.button("Accept", type="primary")
        with cols[2]:
            reject_button = st.button("Reject", type="secondary")

        if accept_button:
            if selected_file and os.path.isfile(selected_file):
                st.write("Building Gradle project...")
                logs = build_gradle_project(os.path.dirname(selected_file))  # Call the build function
                st.text_area("Build Logs", logs, height=300)  # Display logs in a text box
            else:
                st.warning("File is invalid.")

        if reject_button:
            try:
                shutil.rmtree(st.session_state.path)
                st.session_state.clear()
                st.switch_page("pages/chat.py")
            except Exception as e:
                st.error(f"Error deleting temp folder: {e}")
                
        # Show file contents if a file is selected
        if selected_file and os.path.isfile(selected_file):
            try:
                with open(selected_file, 'r') as file:
                    content = file.read()

                st.code(content, )
            except Exception as e:
                st.error(f"Error reading file: {e}")
        elif selected_file:
            st.info("Please select a file to view its contents.")

def file_browser(path):
    """Recursive file browser that returns the selected file path."""
    selected_file = None
    current_path = st.session_state.get('current_path', path)

    # Button to go up one directory
    if st.button("⬆️ Up one level"):
        current_path = str(pathlib.Path(current_path).parent)
        st.session_state.current_path = current_path

    # Show current directory
    st.caption(f"Current directory: {current_path}")

    try:
        # List directories first, then files
        items = os.listdir(current_path)
        directories = [d for d in items if os.path.isdir(os.path.join(current_path, d))]
        files = [f for f in items if os.path.isfile(os.path.join(current_path, f))]

        # Show directories with folder icons
        for directory in sorted(directories):
            if st.button(f"📁 {directory}"):
                new_path = os.path.join(current_path, directory)
                st.session_state.current_path = new_path
                st.rerun()

        # Show files with file icons
        for file in sorted(files):
            if st.button(f"📄 {file}"):
                selected_file = os.path.join(current_path, file)
                st.session_state.selected_file = selected_file

        # Get the selected file from session state if it exists
        selected_file = st.session_state.get('selected_file', None)
    except Exception as e:
        st.error(f"Error accessing directory: {e}")

    return selected_file

if __name__ == "__main__":
    main()
