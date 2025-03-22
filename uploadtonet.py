import paramiko
import os
import datetime
from dotenv import load_dotenv

load_dotenv()


def upload_file(local_file_path):
    host = "152.69.212.39"
    port = 22
    username = "czlucius"  # Change if needed
    password = os.getenv("MYPASS")
    remote_dir = "/tmp/a/"  # Updated remote directory
    
    # Extract file extension
    file_ext = os.path.splitext(local_file_path)[1]
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    new_filename = f"{timestamp}_upload{file_ext}"
    remote_path = os.path.join(remote_dir, new_filename)
    
    try:
        # Establish SSH and SFTP connection
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port, username, password)
        
        sftp = ssh.open_sftp()
        sftp.put(local_file_path, remote_path)
        sftp.close()
        ssh.close()
        
        return f"http://{host}:18398/{new_filename}"
    except Exception as e:
        return f"Error: {str(e)}"

# Example usage
if __name__ == "__main__":
    local_path = "stop.apk"  # Change to the file you want to upload
    print(upload_file(local_path))