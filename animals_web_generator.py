import json

HTML_TEMPLATE = "animals_template.html"
ANIMALS_DATA = "animals_data.json"

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)
    

def save_html(html_string, file_name):
    with open(file_name, "w") as fileobj:
        fileobj.write(html_string)



def print_animals():
    animals_data = load_data(ANIMALS_DATA)
    for animal in animals_data:
        try:
            print(f"Name: {animal["name"]}")
        except KeyError:
            pass   
        try:
            print(f"Diet: {animal["characteristics"]["diet"]}")
        except KeyError:
            pass        
        try:
            print(f"Location: {animal["locations"][0]}")
        except KeyError:
            pass
        try:
            print(f"Type: {animal["characteristics"]["type"]}")
        except KeyError:
            pass
        print()


def serialize_animal(animal):
    output = ""
    output += '<li class="cards__item">\n'
    output += f'<div class="card__title">{animal["name"]}</div>\n'
    output += '<p class="card__text">\n'
    try:
        output += f"<strong>Diet:</strong> {animal["characteristics"]["diet"]}<br/>\n"
    except KeyError:
        pass
    try:
        output += f"<strong>Location:</strong> {animal["locations"][0]}<br/>\n"
    except KeyError:
        pass
    try:
        output += f"<strong>Type:</strong> {animal["characteristics"]["type"]}<br/>\n"
    except KeyError:
        pass
    output += '</p>\n'
    output += '</li>\n'
    return output

def get_string():
    animals_data = load_data(ANIMALS_DATA)
    output = ""
    for animal in animals_data:
        output += serialize_animal(animal)
    return output


def get_html():
    with open(HTML_TEMPLATE, "r") as fileobj:
        return fileobj.read()


def main():
    animals = get_string()
    html_template = get_html()
    # print(html_template)
    html_output = html_template.replace("__REPLACE_ANIMALS_INFO__", animals)
    save_html(html_output, "animals.html")


if __name__ == "__main__":
    main()
