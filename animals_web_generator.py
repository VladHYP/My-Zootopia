import json


def load_data(file_path):
    """Loads a JSON file."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)

def print_animals(animals):
    """Print name, diet, first location, type (if present) for each animal."""
    for animal in animals:
        if "name" in animal:
            print(f"Name: {animal['name']}")

        characteristics = animal.get("characteristics", {})

        diet = characteristics.get("diet")
        if diet:
            print(f"Diet: {diet}")

        locations = animal.get("locations")
        if isinstance(locations, list) and len(locations) > 0:
            print(f"Location: {locations[0]}")

        animal_type = characteristics.get("type")
        if animal_type:
            print(f"Type: {animal_type}")

        print()  # blank line between animals

if __name__ == "__main__":
    animals_data = load_data("animals_data.json")
    print_animals(animals_data)