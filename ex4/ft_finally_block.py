#! /usr/bin/env python3
class PlantError(Exception):
    pass


def check_water() -> None:
    raise PlantError("Not enough water in the tank!")


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system(plants: list[str]) -> None:
    print("Opening watering system...")
    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as e:
        print(f"Cought PlantError : {e}")
        print("...ending tests and returning to main")
        return
    finally:
        print("Closing watering system")


def main() -> None:
    print("=== Garden Watery System")
    print("")
    print("Testing valid plants...")
    test_watering_system(["Tomato", "Lettuce", "Carrots"])
    print("")
    print("Testing invalid plants...")
    test_watering_system(["Tomato", "lettuce"])
    print("")
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    main()
