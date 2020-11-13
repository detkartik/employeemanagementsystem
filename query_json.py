import re 
import json

regex = '^[A-Za-z_][A-Za-z0-9_]*'

def check(string):  
  
     # pass the regualar expression 
     # and the string in search() method 
    if(re.search(regex, string)):  
        print("Valid Identifier")  
        string = {"name": "John","age": 30,"city": "New York"}
        d = json.loads(string)
        print("%d",d)
          
    else:  
        print("Invalid Identifier") 
