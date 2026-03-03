import functools
import re
import time


def spell_timer(func: callable) -> callable:
    functools.wraps(func)

    def wrapper(*args: tuple[any], **kwds: dict[str, any]) -> any:
        print(f'Casting {func.__name__}...')

        timestamp: float = time.time()

        result: any = func(*args, **kwds)

        time_taken: float = time.time() - timestamp

        print(f"Spell completed in {time_taken} seconds")
        return result

    return wrapper


def power_validator(min_power: int) -> callable:

    def decorator(func: callable) -> callable:

        @functools.wraps(func)
        def wrapper(*args: tuple, **kwds: dict[str, any]) -> any:
            power: int = args[2]
            if power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwds)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> callable:

    def decorator(func: callable) -> callable:

        @functools.wraps(func)
        def wrapper(*args: tuple, **kwds: dict[str, any]) -> any:
            try:
                exception_occurred: bool = False
                result: any = func(*args, **kwds)
            except Exception:
                exception_occurred = True

            if exception_occurred:
                for i in range(max_attempts):
                    print(f"Spell failed, retrying... ({i+1}/{max_attempts})")
                    try:
                        exception_occurred: bool = False
                        result: any = func(*args, **kwds)
                    except Exception:
                        exception_occurred = True

                    if not exception_occurred:
                        return result

            if exception_occurred:
                return f"Spell casting failed after {max_attempts} attempts"

            return result
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return re.search(r"^[A-Za-zÀ-ÖØ-öø-ÿ\s]{3,}$", name) is not None

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    @spell_timer
    def fireball():
        return "Fireball cast!"

    print("Testing spell timer...")
    result: str = fireball()
    print(f"Result: {result}")

    print()

    from random import random

    @retry_spell(10)
    def min_random(min: float) -> bool:
        if random() > min:
            return True
        raise Exception("Random < min")

    print("Testing retry spell...")
    print(f"Result: {min_random(0.9)}")

    print()

    mage: MageGuild = MageGuild()

    print("Testing MageGuid...")
    print(f"Correct name: {mage.validate_mage_name('Perfect Mage')}")
    print(f"Incorrect name: {mage.validate_mage_name('mage42')}")
    print(f"Sufficient power: {mage.cast_spell('Lightning', 15)}")
    print(f"Insufficient power: {mage.cast_spell('Fireball', 3)}")
