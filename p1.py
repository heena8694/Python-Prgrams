#palidrome
def is_palidrome(s):
    s.replace(" ","").lower()
    return s[::-1]
 
input_string = " PythonProgramminP"
if is_palidrome(input_string):
    print("It's Palidrome")
else:
    print("It's not palidrome")
          
    
