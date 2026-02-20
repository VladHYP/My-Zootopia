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

def serialize_animal(animal):
    """Serialize a single animal into HTML card markup."""
    output = ""

    name = animal.get("name")

    characteristics = animal.get("characteristics", {})
    diet = characteristics.get("diet")
    animal_type = characteristics.get("type")

    locations = animal.get("locations")
    first_location = None
    if isinstance(locations, list) and len(locations) > 0:
        first_location = locations[0]

    output += '<li class="cards__item">\n'

    if name:
        output += f'  <div class="card__title">{name}</div>\n'

    output += '  <p class="card__text">\n'

    if diet:
        output += f'      <strong>Diet:</strong> {diet}<br/>\n'

    if first_location:
        output += f'      <strong>Location:</strong> {first_location}<br/>\n'

    if animal_type:
        output += f'      <strong>Type:</strong> {animal_type}<br/>\n'

    output += "  </p>\n"
    output += "</li>\n"

    return output

def build_animals_info(animals):
    """Build HTML for all animals."""
    output = ""

    for animal in animals:
        output += serialize_animal(animal)

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