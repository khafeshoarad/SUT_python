current_menu = 'log in/sign up menu'
class User:
    def __init__(self, id, name, password, type) -> None:
        self.id = id
        self.name = name
        self.password = password
        self.type = type
    
class Course:
    def __init__(self, id, name, capacity) -> None:
        self.id = id
        self.name = name
        self.capacity = capacity
        self.students_numbers = []

def has_no_whitespace_in_middle(s):

    return not any(s[i].isspace() and s[i + 1].isspace() for i in range(len(s) - 1))

def sign_up(type, id, name, password):
    pass_cons = ['*', '.', '!', '@', '$', '%', '^', '&', '(', ')']
    
    if type == 'S' or type == 'P':
        if not id.isnumeric():
            return 'invalid id'
        for user in users:
            if user.id == id:
                return 'id already exists'
        if not has_no_whitespace_in_middle(name):
            return 'invalid name'
        if not any(char in pass_cons for char in password):
            return 'invalid password'
        
        users.append(User(id, name, password, type))
        
        return 'signed up successfully!'        
            
    else:
        return 'invalid type'
                
def log_in(id, password):
    
    uids = [user.id for user in users]
    passes = [user.password for user in users]
    
    if (id not in uids) or not id.isnumeric():
        print('incorrect id')
        return False
    
    if password not in passes:
        print('incorrect password')
        return False  
    
    for user in users:
        if int(user.id) == int(id) and user.password == password:
            print('logged in successfully!')
            global current_menu
        
            if user.type == 'S':
            
                current_menu = 'student menu'
                print('entered student menu')
                return True
            elif user.type == 'P':
                current_menu = 'professor menu'
                print('entered professor menu')
                return True 
    
        
    
def show_course():
    print("course list:")
    for course in courses:
        print(f"{course.id} {course.name} {len(course.students_numbers)}/{course.capacity}")

def add_course(id, name, capacity):
    if not id.isnumeric():
        return 'invalid course id'
    
    if not capacity.isnumeric():
        return 'invalid course capacity'
    
    if not has_no_whitespace_in_middle(name):
        return 'invalid course name'

    for course in courses:
        if course.id == id:
            return 'course id already exists'

    courses.append(Course(id, name, capacity))
    return 'course added successfully!'
    
    
        

def get_course(course_id, user_id):
    course_ids = [c.id for c in courses]
    
    if (not course_id.isnumeric()) or (course_id not in course_ids):
        return 'incorrect course id'
    
    for course in courses:
        if course.id == course_id:
            
            if user_id in course.students_numbers:
                return 'you already have this course'
            
            elif len(course.students_numbers) == int(course.capacity):
                return 'course is full'
            
            else:
                course.students_numbers.append(user_id)
                return 'course added successfully!'
      
users = []
courses = []
cmds = []
current_user = 0
sign_in_flag = False


while True:
    cmd = input().strip()
    if cmd == 'edu exit edu':
        break
    cmds.append(cmd)
    
for cmd in cmds:    
    
    if cmd.startswith('edu') and cmd.endswith('edu') and has_no_whitespace_in_middle(cmd):
        cmd_extract = cmd.split()
        # print(cmd_extract)
        #0    1    2  3  4    5    6   7   8  9     10
        #edu sign up -S -i 12345 -n parsa -p p123* edu
        #edu log in -i 54321 -p a123* edu
        #edu add course -c fop -i 1 -n 50 edu

        if cmd_extract[1] == 'sign' and cmd_extract[2] == 'up':
            print(sign_up(cmd_extract[3][-1] ,cmd_extract[5], cmd_extract[7], cmd_extract[9]))
        
        elif cmd_extract[1] == 'log' and cmd_extract[2] == 'in' and cmd_extract[3] == '-i' and cmd_extract[5] == '-p':
            if log_in(cmd_extract[4], cmd_extract[6]):
    
                current_user = cmd_extract[4]
                sign_in_flag=True
            
        elif cmd_extract[1] == 'add' and cmd_extract[2] == 'course':
            print(add_course(cmd_extract[6], cmd_extract[4], cmd_extract[8]))
        
        elif cmd_extract[1] == 'show' and cmd_extract[2] == 'course' and cmd_extract[3] == 'list':
            show_course()
        
        elif cmd_extract[1] == 'current' and cmd_extract[2] == 'menu':
            print(current_menu)
                
        elif cmd_extract[1] == 'log' and cmd_extract[2] == 'out':
            sign_in_flag = False
            current_menu = 'entered log in/sign up menu'
            print('logged out successfully!')
            print(current_menu)
            continue
        elif cmd_extract[1] == 'get' and cmd_extract[2] == 'course' and cmd_extract[3] == '-i':
            print(get_course(cmd_extract[4], current_user))
        else:
            print('invalid command')
        
    else:
        print('invalid command')

        
        