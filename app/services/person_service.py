from app.services.json_manipulation import load_json_file

def check_email_exist(filepath: str, email: str) -> bool:
    person_list = load_json_file(filepath)

    for person in person_list:
        if person["email"]== email:
            return True
    
    return False