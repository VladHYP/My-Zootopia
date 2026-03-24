import data_fetcher


def serialize_animal(animal_obj):
    """
    Convert a single animal dictionary into an HTML <li> element.
    Only include fields that actually exist.
    """
    name = animal_obj.get("name")
    characteristics = animal_obj.get("characteristics", {})
    locations = animal_obj.get("locations", [])

    output = '<li class="cards__item">\n'

    if name:
        output += f'  <div class="card__title">{name}</div>\n'

    output += '  <p class="card__text">\n'

    diet = characteristics.get("diet")
    if diet:
        output += f'    <strong>Diet:</strong> {diet}<br/>\n'

    location = locations[0] if locations else None
    if location:
        output += f'    <strong>Location:</strong> {location}<br/>\n'

    animal_type = characteristics.get("type")
    if animal_type:
        output += f'    <strong>Type:</strong> {animal_type}<br/>\n'

    output += '  </p>\n'
    output += '</li>\n'

    return output


def generate_animals_html(data, animal_name):
    """
    Generate HTML for all animals or an error message if none found.
    """
    if not data:
        return f'<h2>The animal "{animal_name}" doesn\'t exist.</h2>'

    return "".join(serialize_animal(animal) for animal in data)


def main():
    """
    Main entry point of the program.
    Prompts the user for an animal name, fetches data,
    and generates an HTML file based on a template.
    """
    animal_name = input("Enter a name of an animal: ").strip()

    animals_data = data_fetcher.fetch_data(animal_name)
    animals_html = generate_animals_html(animals_data, animal_name)

    with open("animals_template.html", "r", encoding="utf-8") as file:
        template = file.read()

    final_html = template.replace("__REPLACE_ANIMALS_INFO__", animals_html)

    with open("animals.html", "w", encoding="utf-8") as file:
        file.write(final_html)

    print("Website was successfully generated to the file animals.html.")


if __name__ == "__main__":
    main()
    