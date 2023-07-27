import subprocess

def run_script(script_name):
    try:
        subprocess.run(["python", script_name], check=True)
    except subprocess.CalledProcessError:
        print(f"Error while running {script_name}")

if __name__ == "__main__":
    scripts_to_run = ["bot.py", "smile.py", "eye_blink.py"]

    # Use multiprocessing to run the scripts in parallel
    import multiprocessing
    processes = [multiprocessing.Process(target=run_script, args=(script,)) for script in scripts_to_run]

    # Start all processes
    for process in processes:
        process.start()

    # Wait for all processes to finish
    for process in processes:
        process.join()

        print("All done")




