import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def print_animals():
    animals_data = load_data('animals_data.json')
    for animal in animals_data:
        if animal["name"]:
            print(f"Name: {animal["name"]}")
        if animal["characteristics"]["diet"]:
            print(f"Diet: {animal["characteristics"]["diet"]}")
        if animal["locations"][0]:
            print(f"Location: {animal["locations"][0]}")
        try:
            if animal["characteristics"]["type"]:
                print(f"Type: {animal["characteristics"]["type"]}")
        except KeyError:
            pass
        print()


def main():
    print_animals()


if __name__ == "__main__":
    main()
