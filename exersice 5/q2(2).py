class User:
    def __init__(self, id, name, password, user_type) -> None:
        self.id = id
        self.name = name
        self.password = password
        self.user_type = user_type

class Course:
    def __init__(self, id, name, capacity) -> None:
        self.id = id
        self.name = name
        self.capacity = capacity
        self.students_numbers = []

def has_no_whitespace_in_middle(s):
    return not any(s[i].isspace() and s[i + 1].isspace() for i in range(len(s) - 1))

def sign_up(user_type, user_id, user_name, user_password):
    pass_cons = ['*', '.', '!', '@', '$', '%', '^', '&', '(', ')']

    if user_type in {'S', 'P'}:
        if not user_id.isnumeric():
            return 'invalid id'
        for user in users:
            if user.id == user_id:
                return 'id already exists'
        if not has_no_whitespace_in_middle(user_name):
            return 'invalid name'
        if not any(char in pass_cons for char in user_password):
            return 'invalid password'

        users.append(User(user_id, user_name, user_password, user_type))

        return 'signed up successfully!'

    else:
        return 'invalid type'

def log_in(user_id, user_password):
    uids = [user.id for user in users]
    passes = [user.password for user in users]

    if (user_id not in uids) or not user_id.isnumeric():
        print('incorrect id')
        return False

    if user_password not in passes:
        print('incorrect password')
        return False

    for user in users:
        if int(user.id) == int(user_id) and user.password == user_password:
            print('logged in successfully!')
            global current_menu

            if user.user_type == 'S':
                current_menu = 'student menu'
                print('entered student menu')
                return True
 
