import json


def load_data(file_path):
    """Loads a JSON file."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)

def read_template(file_path):
    """Reads an HTML template file and returns it as a string."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return handle.read()


def write_html(file_path, content):
    """Writes the generated HTML content into a file."""
    with open(file_path, "w", encoding="utf-8") as handle:
        handle.write(content)

def build_animals_info(animals):
    """Build HTML list items for each animal."""
    output = ""

    for animal in animals:
        output += '<li class="cards__item">\n'

        # Name
        if "name" in animal:
            output += f"Name: {animal['name']}<br/>\n"

        characteristics = animal.get("characteristics", {})

        # Diet
        diet = characteristics.get("diet")
        if diet:
            output += f"Diet: {diet}<br/>\n"

        # First location
        locations = animal.get("locations")
        if isinstance(locations, list) and len(locations) > 0:
            output += f"Location: {locations[0]}<br/>\n"

        # Type
        animal_type = characteristics.get("type")
        if animal_type:
            output += f"Type: {animal_type}<br/>\n"

        output += "</li>\n"

    return output

if __name__ == "__main__":
    # load animal data
    animals_data = load_data("animals_data.json")

    # build animals info string
    animals_info = build_animals_info(animals_data)

    # read HTML template
    template = read_template("animals_template.html")

    # replace placeholder in template
    final_html = template.replace("__REPLACE_ANIMALS_INFO__", animals_info)

    # write new HTML file
    write_html("animals.html", final_html)

    print("animals.html generated successfully.")