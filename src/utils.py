import json
import hashlib
import random
import string


def parse_message(text: str, command: str) -> any:
    if command == "/push":
        formated_message = [s.strip() for s in text[len(command):].strip().split(':')]
        if len(formated_message) != 2 : formated_message = None
    elif command == "/pmake":
        formated_message = [s.strip() for s in text[len(command):].strip().split(' ')]
        if not formated_message[0].isdigit() : formated_message = None
        else : formated_message = int(formated_message[0])
    return formated_message


def push_password(service: str, password: str, filename: str):
    with open(f"../data/{filename}.json", "r+") as f:
        fdata = json.load(f)
        fdata["passwords"].update({service : password})
        f.seek(0)
        json.dump(fdata, f, ensure_ascii=False, sort_keys=True, indent=4)


def generate_random_string(length: int=100) -> str:
    letters = string.ascii_lowercase + string.ascii_uppercase
    random_string = ''.join(random.choice(letters) for i in range(length))

    return random_string


def encrypt_string(string: str) -> str:
    password = hashlib.md5(string.encode()).hexdigest()
    return password


def format_password(password: str, length: int=16) -> str:
    upper_case = length / 3
    password = password[:length]
    idx_choice = [i for i in range(length)]

    pass_with_upper = ''
    for i in range(len(password)):
        if i < upper_case:
            idx = int(random.choice(idx_choice))
            pass_with_upper += password[idx].upper()
        pass_with_upper += password[i]
    
    
    pass_with_sep = ''
    for i in range(len(pass_with_upper)):
        if i % 5 == 0 and i != 0:
            pass_with_sep += '-'
        pass_with_sep += pass_with_upper[i]

    return pass_with_sep


def get_passwords(filename: str) -> str:
    fdata = None
    with open(f"data/{filename}.json", "r+") as f:
        fdata = json.load(f)
    output = get_passwords_output(fdata["passwords"])
    return output


def get_passwords_output(pass_dict: dict) -> str:
    output = ''
    for key in pass_dict.keys():
        output += f"{key} : {pass_dict[key]}\n"
    return output