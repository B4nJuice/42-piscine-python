from importlib.metadata import version, PackageNotFoundError
import sys


def check_imports() -> bool:
    required_modules: list[tuple[str, str]] = [
        ("pandas", "Data manipulation ready"),
        ("requests", "Network access ready"),
        ("matplotlib", "Visualization ready")
    ]

    all_modules_installed: bool = True
    for module, module_text in required_modules:
        try:
            print(f"[OK] {module} ({version(module)}) - {module_text}")
        except (PackageNotFoundError):
            all_modules_installed = False
            print(f"[KO] {module} not installed")
    print()
    return all_modules_installed


if __name__ == "__main__":
    modules: list[any] = ["pandas", "matplotlib", "requests"]
    for module in modules:
        try:
            globals()[module] = __import__(module)
        except Exception:
            pass

    if not check_imports():
        print("Not all module installed please install them:")
        print("\"pip install -r requirements.txt\"")
        print("-- or -- ")
        print("\"pip install poetry\"")
        print("\"poetry install\"")
        print("\"poetry run python loading.py\"")
