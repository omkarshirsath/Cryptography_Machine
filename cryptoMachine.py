
def machine():
    keys = "abcdefghijklmnopqrstuvwxyz !@#$%^&*()?|][_-+*/-'.,;1234567890"
    Value = keys[-1] + keys[ 0: -1]
    
    encrypDict = dict(zip(keys, Value))
    decrypDict = dict(zip(Value, keys))
    
    message= input("Please enter your secret message : ")
    mode = input("Please enter the mode : Encode(E) OR Decode(D)")
    
    
    if mode.upper() == 'E':
        newMessage = ''.join([encrypDict[letter] for letter in message.lower()])
        
    elif mode.upper() == 'D':
        newMessage = ''.join([decrypDict[letter] for letter in message.lower()])
    else:
        print("Please enter a correct choise") 
    return newMessage.capitalize()
print(machine())   
    