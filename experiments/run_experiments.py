import subprocess
import sys


def run_script(script_path):

    print("\n===================================")
    print(f"Running experiment: {script_path}")
    print("===================================\n")

    result = subprocess.run(
        [sys.executable, script_path],
        capture_output=True,
        text=True
    )

    print(result.stdout)

    if result.stderr:
        print("\nErrors:")
        print(result.stderr)


if __name__ == "__main__":

    experiments = [

        "experiments/momentum_experiments.py",
        "experiments/parameter_sweep.py"

    ]

    for exp in experiments:
        run_script(exp)

    print("\nAll experiments completed.")
