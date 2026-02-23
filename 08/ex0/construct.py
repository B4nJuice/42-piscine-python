import sys


def check_venv() -> bool:
    return sys.prefix != sys.base_prefix


if __name__ == "__main__":
    in_venv: bool = check_venv()
    current_python: str = sys.executable

    matrix_status: str = ""
    venv: str = "None detected"

    if in_venv:
        matrix_status = "Welcome to the construct"
    else:
        matrix_status = "You're still plugged in"

    print(current_python)
