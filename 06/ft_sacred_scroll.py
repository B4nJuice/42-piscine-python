#!/usr/bin/env python3

import alchemy
import alchemy.elements as direct


if __name__ == "__main__":
    print("=== Sacred Scroll Mastery ===\n")
    print("Testing direct module access:")
    print("alchemy.elements.create_fire(): " + direct.create_fire())
    print("alchemy.elements.create_water(): " + direct.create_water())
    print("alchemy.elements.create_earth():" + direct.create_earth())
    print("alchemy.elements.create_air():" + direct.create_air())

    print()

    print("Testing package-level access (controlled by __init__.py):")
    for function in [
                "create_fire",
                "create_water",
                "create_earth",
                "create_air",
            ]:
        try:
            print(f"alchemy.{function}(): ", end="")
            real_function = getattr(alchemy, function)
            print(real_function())
        except AttributeError:
            print("AttributeError - not exposed")

    print()

    print("Package metadata:")
    print("Version: " + alchemy.__version__)
    print("Author: " + alchemy.__author__)
