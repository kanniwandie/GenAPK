import subprocess
import os

def build_gradle_project(project_dir):
    """
 Returns True if the build succeeds, False otherwise.
    """
    try:
        # Navigate to the project directory
        os.chdir(project_dir)

        print("Cleaning project...")
        clean_process = subprocess.Popen(
            ["./gradlew", "clean"],
            stdout=subprocess.PIPE, #Logs
            stderr=subprocess.PIPE, #Error Logs
            universal_newlines=True
        )

        # Display logs
        for line in clean_process.stdout:
            print(line, end="")
        for line in clean_process.stderr:
            print(line, end="")

        # Wait for the clean process to complete
        clean_process.wait()

        # Build the debug APK
        print("Building APK...")
        build_process = subprocess.Popen(
            ["./gradlew", "assembleDebug"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )

        # Display logs in real-time
        for line in build_process.stdout:
            print(line, end="")
        for line in build_process.stderr:
            print(line, end="")

        # Wait for the build process to complete
        build_process.wait()

        # Check if the build succeeded
        if build_process.returncode == 0:
            # Locate the APK file
            apk_path = os.path.join("app", "build", "outputs", "apk", "debug", "app-debug.apk")
            if os.path.exists(apk_path):
                print(f"APK successfully built at: {apk_path}")
                return True
            else:
                print("APK build failed. Check the logs for errors.")
                return False
        else:
            print("Gradle build failed. Check the logs for errors.")
            return False

    except FileNotFoundError:
        print("Gradle wrapper (gradlew) not found. Ensure you're in the correct project directory.")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False
if __name__ == "__main__":
    project_dir = input("Enter the project directory: ")
    build_gradle_project(project_dir)
