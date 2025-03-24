import psutil

# Function to kill process forcefully if needed.
def kill_process(pid):
    try:
        process = psutil.Process(pid)
        process_name = process.name()

        # Attempt graceful termination first
        process.terminate()
        process.wait(3)  # Wait for 3 seconds to confirm termination

        if process.is_running():  # If still running, force kill
            process.kill()
            print(f"❌ Process {process_name} (PID: {pid}) forcefully killed.")
        else:
            print(f"✅ Process {process_name} (PID: {pid}) terminated successfully.")

    except psutil.NoSuchProcess:
        print(f"⚠️ No such process with PID: {pid}")
    except psutil.AccessDenied:
        print(f"⛔ Permission denied to terminate process {pid}")
    except Exception as e:
        print(f"❗ An error occurred: {e}")

# Example Usage
pid_to_kill = int(input("Enter PID to kill: "))
kill_process(pid_to_kill)
