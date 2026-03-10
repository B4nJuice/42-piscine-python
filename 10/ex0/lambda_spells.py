def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(
        artifacts, key=lambda artifact: -artifact.get("power", float("-inf"))
        )


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(
        lambda mage: mage.get("power", float("-inf")) >= min_power, mages
        ))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    max_power: int = dict(
                max(mages, key=lambda mage: mage.get("power", float("-inf")))
            ).get("power")

    min_power: int = dict(
                min(mages, key=lambda mage: mage.get("power", float("-inf")))
            ).get("power")

    total_power: int = sum(mage.get("power", 0) for mage in mages)

    avg_power: float = round((total_power / len(mages)), 2)

    return {
        "max_power": max_power,
        "min_power": min_power,
        "avg_power": avg_power
    }


if __name__ == "__main__":
    try:
        artifacts: list[dict[str, str | int]] = [
            {
                "name": "Fire Staff",
                "power": 92
            },
            {
                "name": "Crystal orb",
                "power": 80
            },
            {
                "name": "Magic Shield",
                "power": 85
            }
        ]

        spells: list[str] = ["fireball", "heal", "shield"]

        print("Testing artifact sorter...")

        sorted_artifacts: list[dict[str, str | int]] = (
            artifact_sorter(artifacts))

        for i, artifact in enumerate(sorted_artifacts):
            print(
                f"{i+1} {artifact.get('name')} ({artifact.get('power')} power)"
                )

        print()

        print("Filtering artifacts with power > 80...")

        filter_artifacts: list[dict[str, str | int]] = (
            power_filter(artifacts, 81))

        for artifact in filter_artifacts:
            print(f"{artifact.get('name')} ({artifact.get('power')} power)")

        print()

        print("Testing spell transformer...")
        print(" ".join(spell_transformer(spells)))

        print()

        print("Getting mage statistics...")
        mage_stats: dict[str, int] = mage_stats(artifacts)
        print(f"Max power :{mage_stats.get('max_power')}")
        print(f"Min power :{mage_stats.get('min_power')}")
        print(f"Avg power :{mage_stats.get('avg_power')}")
    except Exception as e:
        print(e)
