import json

def push_password(pass_list):
    message = "OK"
    if len(pass_list) == 2:
        with open("data/passwords.json", "r+") as f:
            fdata = json.load(f)
            fdata["passwords"].update({pass_list[0] : pass_list[1]})
            f.seek(0)
            json.dump(fdata, f, ensure_ascii=False, sort_keys=True, indent=4)
    else: message = "Err"

    return message