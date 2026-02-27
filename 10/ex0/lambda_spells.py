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
                max(mages, key=lambda mage: mage.get("power", float("-inf")))
            ).get("power")

    total_power: int = sum(mage.get("power", 0) for mage in mages)

    avg_power: float = round((total_power / len(mages)), 2)

    return {
        "max_power": max_power,
        "min_power": min_power,
        "avg_power": avg_power
    }


if __name__ == "__main__":
    a1 = {"power": 10, "name": "name"}
    a2 = {"power": 14, "name": "tets1"}
    a3 = {"power": -10, "name": "test"}
    a4 = {"power": 101, "name": "ahah"}
    a5 = {"name": "okok"}

    l = [a1, a2, a3, a4, a5]
    l2 = ["test", "*", "", "okok"]

    print(artifact_sorter(l))
    print(power_filter(l, 2))
    print(spell_transformer(l2))
    print(mage_stats(l))
