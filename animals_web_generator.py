import data_fetcher


def serialize_animal(animal_obj):
    """
    Convert a single animal dictionary into an HTML <li> element.
    Only include fields that actually exist.
    """
    output = '<li class="cards__item">\n'

    name = animal_obj.get("name")
    if name:
        output += f'  <div class="card__title">{name}</div>\n'

    output += '  <p class="card__text">\n'

    characteristics = animal_obj.get("characteristics", {})
    locations = animal_obj.get("locations", [])

    diet = characteristics.get("diet")
    if diet:
        output += f'    <strong>Diet:</strong> {diet}<br/>\n'

    if locations:
        output += f'    <strong>Location:</strong> {locations[0]}<br/>\n'

    animal_type = characteristics.get("type")
    if animal_type:
        output += f'    <strong>Type:</strong> {animal_type}<br/>\n'

    output += '  </p>\n'
    output += '</li>\n'

    return output


def generate_animals_html(data):
    """
    Generate the HTML block for all returned animals.
    """
    output = ""
    for animal in data:
        output += serialize_animal(animal)

    return output


def main():
    """
    Ask the user for an animal name, fetch matching animal data,
    and generate the animals.html file.
    """
    animal_name = input("Enter a name of an animal: ").strip()
    animals_data = data_fetcher.fetch_data(animal_name)

    if not animals_data:
        animals_html = f'<h2>The animal "{animal_name}" doesn\'t exist.</h2>'
    else:
        animals_html = generate_animals_html(animals_data)

    with open("animals_template.html", "r", encoding="utf-8") as file:
        template = file.read()

    final_html = template.replace("__REPLACE_ANIMALS_INFO__", animals_html)

    with open("animals.html", "w", encoding="utf-8") as file:
        file.write(final_html)

    print("Website was successfully generated to the file animals.html.")


if __name__ == "__main__":
    main()