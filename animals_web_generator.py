import data_fetcher

def serialize_animal(animal_obj):
    """
    Convert a single animal dictionary into an HTML <li> element.
    """
    name = animal_obj.get("name", "Unknown")
    characteristics = animal_obj.get("characteristics", {})
    locations = animal_obj.get("locations", [])

    diet = characteristics.get("diet", "Unknown")
    animal_type = characteristics.get("type", "Unknown")
    location = locations[0] if locations else "Unknown"

    output = (
        '<li class="cards__item">\n'
        f'  <div class="card__title">{name}</div>\n'
        '  <p class="card__text">\n'
        f'    <strong>Diet:</strong> {diet}<br/>\n'
        f'    <strong>Location:</strong> {location}<br/>\n'
        f'    <strong>Type:</strong> {animal_type}<br/>\n'
        '  </p>\n'
        '</li>\n'
    )
    return output


def generate_animals_html(data):
    """
    Generate the HTML block for all returned animals.
    If no animals are found, return an error message block.
    """
    if not data:
        return '<h2>The animal "{animal_name}" doesn\'t exist.</h2>'

    output = ""
    for animal in data:
        output += serialize_animal(animal)

    return output


def main():
    animal_name = input("Enter a name of an animal: ").strip()
    animals_data = data_fetcher.fetch_data(animal_name)
    animals_html = generate_animals_html(animals_data)

    with open("animals_template.html", "r", encoding="utf-8") as file:
        template = file.read()

    if not animals_data:
        animals_html = f'<h2>The animal "{animal_name}" doesn\'t exist.</h2>'

    final_html = template.replace("__REPLACE_ANIMALS_INFO__", animals_html)

    with open("animals.html", "w", encoding="utf-8") as file:
        file.write(final_html)

    print("Website was successfully generated to the file animals.html.")


if __name__ == "__main__":
    main()