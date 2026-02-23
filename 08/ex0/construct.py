import sys
import site


def check_venv() -> bool:
    return sys.prefix != sys.base_prefix


if __name__ == "__main__":
    in_venv: bool = check_venv()
    current_python: str = sys.executable

    matrix_status: str = ""
    venv: str = "None detected"

    if in_venv:
        matrix_status = "Welcome to the construct"
        venv = sys.prefix.split("/")[-1]
    else:
        matrix_status = "You're still plugged in"

    print(f"MATRIX STATUS: {matrix_status}")

    print()

    print(f"Current Python: {current_python}")
    print(f"Virtual Environment: {venv}")

    if in_venv:
        print(f"Environment Path: {sys.prefix}")

        print()

        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system.")

        print()

        print("Package installation path:", site.getsitepackages()[0])
    else:
        print()

        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")

        print()

        print("To enter the construct, run:")
        print("python3 -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print(".\\matrix_env\\Scripts\\activate # On Windows")

        print()

        print("Then run this program again.")
