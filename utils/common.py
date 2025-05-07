import random
import re
import string


def generate_random_password_for_register(length=14,use_lower_case=True,use_upper_case=True,use_numbers=True,use_special_character=True):

    # Required character sets
    upper = random.choice(string.ascii_uppercase) if use_upper_case else ""
    lower = random.choice(string.ascii_lowercase) if use_lower_case else ""
    digit = random.choice(string.digits) if use_numbers else ""
    symbol = random.choice('!"?$%^&)') if use_special_character else ""
    # Remaining characters
    all_chars = ""
    if use_upper_case:
        all_chars += string.ascii_uppercase
    if use_lower_case:
        all_chars+= string.ascii_lowercase
    if use_numbers:
        all_chars += string.digits
    if use_special_character:
        all_chars += '!"?$%^&)'
    remaining = ''.join(random.choices(all_chars, k=length - 4))

    # Combine and shuffle
    password = list(upper + lower + digit + symbol + remaining)
    random.shuffle(password)
    return ''.join(password)

# Example use
def get_username_if_email(text):
    # Simple email pattern
    email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    print(email_pattern)
    if re.match(email_pattern, text):
        return text.split('@')[0]
    else:
        return  text

def get_reason_and_ui_input_warningmessage_or_warning_message_flag(context):
    if "@" not in context.email_address:
        return "mising_domain_address_in_mail_id",True
    user_name,sep,domain=context.email_address.partition("@")
    if not user_name:
        return "missing_user_name_in_email_Address",True
    if not domain or domain.startswith("."):
        return "missing_domain_name_in_mail_id",True
    if ".." in domain:
        return "double_dot_in_mail_address_domain",True
    if " " in context.email_address:
        return "space_in_mail_address",True
    if "!" in domain:
        return "!symbol_in_mail_address_domain", True
    return "invalid_email_address",False




def get_login_failure_reason(context,reason,component="login"):
    print(component)
    if reason=="non_registered_username" and re.match(r"[^@]+@[^@]+\.[^@]+", context.username):
        reason="non_registered_mail_id"

    login_reason_dict={"non_registered_username":f"Error: The username {context.username} is not registered on this site. If you are unsure of your username, try your email address instead.",
                 "non_registered_mail_id":"Error: A user could not be found with this email address.",
                 "empty_username":"Error: Username is required.",
                 "empty_username_and_password":"Error: Username is required.",
                 "empty_password":"Error: Password is required.",
                 "wrong_password":f"Error: The password you entered for the username {context.username} is incorrect. Lost your password?",
                 "Case_sensitivity_password":f"Error: The password you entered for the username {context.username} is incorrect. Lost your password?",
                 "invalid-username_and_password":f"Error: The username {context.username} is not registered on this site. If you are unsure of your username, try your email address instead."
                 }
    register_reason_dict={"invalid_email_address":"Error: Please provide a valid email address.",
                         "mising_domain_address_in_mail_id":f"Please include an '@' in the email address. '{context.email_address}' is missing an '@'.",
                         "missing_domain_name_in_mail_id":f"'.' is used at a wrong position in '.com'.",
                          "missing_user_name_in_email_Address":f"Please enter a part followed by '@'. '{context.email_address}' is incomplete.",
                          "double_dot_in_mail_address_domain":f"'.' is used at a wrong position in '{context.email_address.split('@')[1] if '@' in context.email_address else context.email_address}'.",
                          "!symbol_in_mail_address_domain":"A part following '@' should not contain the symbol '!'.",
                          "space_in_mail_address":f"A part followed by '@' should not contain the symbol ' '.",
                          "empty_password":"Error: Please enter an account password.",
                         "empty_email_address_and_password":"Error: Please provide a valid email address.",
                         "empty_email_address":"Error: Please provide a valid email address."

    }
    if component!="login":
        print("register............")
        return register_reason_dict.get(reason,None)
    print("login_dict")
    return login_reason_dict.get(reason, None)

def convert_dictionary_values_to_string(address_dict):
    address = (
        f"{address_dict.get('c_name', '')}\n"
        f"{address_dict.get('f_name', '')} {address_dict.get('l_name', '')}\n"
        f"{address_dict.get('street_address', '')}\n"
        f"{address_dict.get('address_2', '')}\n"
        f"{address_dict.get('city_name', '')} - {address_dict.get('pincode', '')}\n"
        f"{address_dict.get('state', '')}"
    )
    return  address
