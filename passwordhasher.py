import hashlib
import getpass

def validatepsswd(password):
    upp = False
    low = False
    num = False
    spc = False
    cnt = False
    space = True
    norpt = True

    pwlen = len(password)
    pos = 0
    for eachchar in password:
        if pos < pwlen-2:
            if eachchar==password[pos+1] and eachchar==password[pos+2]:
                norpt = False                
        else:
            pos += 1

    if pwlen >= 8:
        cnt = True

    for eachchar in password:
        if eachchar in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            upp = True
        elif eachchar in "abcdcdefghijklmnopqrstuvwxyz":
            low = True
        elif eachchar in "0123456789":
            num = True
        elif eachchar in "!@#$%^&*()_+-=<>?,./;'\":[]":
            spc = True
        elif eachchar in " ":
            space = False
        else:
            continue
    
    if upp and low and num and spc and cnt and norpt and space:
        confirm_password(password)
        return True
    else:
        print('Enter a stronger password.')
        return False
    
def confirm_password(password):
    passwd2 = getpass.getpass(prompt='Confirm your password:', stream=None)
    if password == passwd2:
        hashing(passwd2)
    else:
        print("Passwords does not match.")
        
def hashing(password):
    h =  hashlib.pbkdf2_hmac('sha512', password.encode('ascii'), b'salt', 100000)
    hash = h.hex()
    b = open('hashedpass.txt', "a")
    b.write(hash + "\n")
    print('Password hashed successfully.')    

print("$>Your password should be:\n\t1.atleast eight characters.\n\t2.atleast one uppercase,lowercase,symbol,number with no space.")
print("$>The password you enter will be hidden.")
passwd = getpass.getpass(prompt='Enter the password:', stream=None)
validatepsswd(passwd)