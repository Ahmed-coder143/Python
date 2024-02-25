def is_camel_case(s):
    
    if any(char.islower() for char in s) and any(char.isupper() for char in s):
       
        if ' ' not in s:
            
            if s[0].islower():
                return True
    return False
user_input = input()
if is_camel_case(user_input):
    print("yes")
else:
    print("no")