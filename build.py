import subprocess
import os

def build_gradle_project(project_dir):
    """
 Returns True if the build succeeds, False otherwise.
    """
    logs = []
    try:
        # Navigate to the project directory
        os.chdir(project_dir)

        logs.append("Cleaning project...")
        clean_process = subprocess.Popen(
            ["./gradlew", "clean"],
            stdout=subprocess.PIPE,  # Logs
            stderr=subprocess.PIPE,  # Error Logs
            universal_newlines=True
        )

        # Capture logs
        for line in clean_process.stdout:
            logs.append(line.strip())
        for line in clean_process.stderr:
            logs.append(line.strip())

        # Wait for the clean process to complete
        clean_process.wait()

        logs.append("Building APK...")
        build_process = subprocess.Popen(
            ["./gradlew", "assembleDebug"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )

        # Capture logs
        for line in build_process.stdout:
            logs.append(line.strip())
        for line in build_process.stderr:
            logs.append(line.strip())

        # Wait for the build process to complete
        build_process.wait()

        # Check if the build succeeded
        if build_process.returncode == 0:
            logs.append("Build succeeded!")
        else:
            logs.append("Build failed. Check the logs for errors.")
    except FileNotFoundError:
        logs.append("Gradle wrapper (gradlew) not found. Ensure you're in the correct project directory.")
    except Exception as e:
        logs.append(f"An unexpected error occurred: {e}")

    # Return logs as a single string
    return "\n".join(logs)

if __name__ == "__main__":
    project_dir = input("Enter the project directory: ")
    logs = build_gradle_project(project_dir)
    print(logs)