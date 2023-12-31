import subprocess


def run_file_in_new_process(file_path):
    try:
        print("Process Start")
        subprocess.run(['python', file_path], check=True)
        print("Process End")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")


file_path = 'demo_code.py'
run_file_in_new_process(file_path)
