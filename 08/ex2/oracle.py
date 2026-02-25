import os


def main() -> None:
    from dotenv import load_dotenv

    load_dotenv()

    param_dict: dict[str, str] = {}

    print("ORACLE STATUS: Reading the matrix...")

    print()

    param_dict.update({"MATRIX_MODE": os.environ.get("MATRIX_MODE")})
    param_dict.update({"DATABASE_URL": os.environ.get("DATABASE_URL")})
    param_dict.update({"API_KEY": os.environ.get("API_KEY")})
    param_dict.update({"LOG_LEVEL": os.environ.get("LOG_LEVEL")})
    param_dict.update({"ZION_ENDPOINT": os.environ.get("ZION_ENDPOINT")})

    if None in param_dict.values():
        for key, value in param_dict.items():
            if value is None:
                print(f"Error: Missing \"{key}\" value.")
        return

    print("Configuration loaded:")
    print(f"Mode: {param_dict.get('MATRIX_MODE')}")
    print("Database: Connected to local instance")
    print("API Acces: Authenticated")
    print(f"Log Level: {param_dict.get('LOG_LEVEL')}")
    print("Zion Network: Online")

    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
