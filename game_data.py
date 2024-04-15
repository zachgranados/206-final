# reads game data api key from extra file
def get_api_key(filename):
    with open(filename, 'r', encoding="utf-8-sig") as file:
            key = file.read()
            return key

    

    