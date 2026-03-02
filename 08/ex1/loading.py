from importlib.metadata import version
import json


def generate_matrix_analysis() -> None:
    matplotlib = globals()["matplotlib"]
    pandas = globals()["pandas"]
    requests = globals()["requests"]

    BASE_URL = "https://data.economie.gouv.fr/api/explore/v2.1\
/catalog/datasets/prix-des-carburants-en-france-flux-instantane-v2/records"

    params = {
        "where": "ville='Lyon'",
        "limit": 100
    }

    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    data = response.json()

    records = []
    for record in data.get("results", []):
        price_list = record.get("prix", [])
        if isinstance(price_list, str):
            price_list = json.loads(price_list)
        for gaz in price_list:
            if gaz.get("@nom") == "Gazole":
                valeur = gaz.get("@valeur")
                maj = gaz.get("@maj")
                if valeur and maj:
                    records.append({
                        "prix": float(valeur),
                        "maj": pandas.to_datetime(maj)
                    })

    df = pandas.DataFrame(records)
    df = df.sort_values("maj").reset_index(drop=True)

    matplotlib.pyplot.style.use('dark_background')
    fig, ax = matplotlib.pyplot.subplots(figsize=(10, 6))

    ax.plot(
            df['maj'],
            df['prix'],
            c='#FFFFFF',
            linewidth=1,
            alpha=0.8,
            label='Gazole (€)'
        )
    ax.plot(
            df['maj'],
            df['prix'],
            c='white',
            linewidth=2,
            label='Trend (MA10)'
        )

    ax.set_title('Gazole price at Lyon', color='#FFFFFF', fontsize=16)
    ax.set_xlabel('Date')
    ax.set_ylabel('Price (€ / L)')
    ax.grid(True, linestyle='--', alpha=0.3)
    matplotlib.pyplot.xticks(rotation=45)
    matplotlib.pyplot.tight_layout()

    filename = "analysis.png"
    matplotlib.pyplot.savefig(filename, dpi=100)
    matplotlib.pyplot.close()

    print("Results saved to :", filename)


def main() -> None:
    all_modules_installed: bool = True

    required_modules: list[tuple[str, str]] = [
        ("pandas", "Data manipulation ready", []),
        ("requests", "Network access ready", []),
        ("matplotlib", "Visualization ready", ["pyplot"])
    ]
    for module, module_text, f_list in required_modules:
        try:
            globals()[module] = __import__(module, fromlist=f_list)
            print(f"[OK] {module} ({version(module)}) - {module_text}")
        except Exception:
            all_modules_installed = False
            print(f"[KO] {module} not installed")
            pass

    print()

    if not all_modules_installed:
        print("Please install all the modules:")
        print("\"pip install -r requirements.txt\"")
        print("-- or -- ")
        print("\"pip install poetry\"")
        print("\"poetry install\"")
        print("\"poetry run python loading.py\"")
        return

    print("Pip and Poetry differencies.")

    print("pip installs Python packages from PyPI\
 and usually works with a requirements.txt file.")
    print("Poetry manages the whole project: dependencies,\
 virtual environments, and version locking using pyproject.toml")

    generate_matrix_analysis()


if __name__ == "__main__":
    main()
