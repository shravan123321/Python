'''  you're building a simple app that registers users.
     you want to separate concerns: getting input,validating it, and saving it
     taxk:
      -Write register_user() that calls:
        -get_input()
        -validate_input()
        -save_to_db()
'''

def get_input() :
    print("geting the input: ")

def validate_input() :
    print("validate the input: ")

def save_to_db() :
    print("saving to database: ")

def register_user() :
    get_input()
    validate_input()
    save_to_db()
    print("Registation is sucessfully completed: ")

register_user()