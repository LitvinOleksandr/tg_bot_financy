__token_address = "token.txt"
__access_tist_address = "access_list.txt"
__file_with_names = "file_with_names.txt"

def load_token():
    with open(__token_address, "r") as file:
        return file.read().strip()

def load_access_list() -> list[int]:
    with open(__access_tist_address, "r") as file:
        return [int(line.strip()) for line in file if line.strip().isdigit()]

def load_names(ids_number) -> str:
    return read_numbers_to_dict(__file_with_names).get(ids_number, "Unknown name")


def read_numbers_to_dict(filename):
    numbers_dict = {}

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split(maxsplit=1)
            if len(parts) == 2:
                number, owner = parts
                numbers_dict[int(number)] = owner

    return numbers_dict

TOKEN = load_token()
ACCESS_LIST = load_access_list()
