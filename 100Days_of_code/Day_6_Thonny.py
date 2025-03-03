print ("Welcome to the secret vault")
print ("Please confirm your idenity")
username = input ("Username > " )
password = input ("Whats your password?")

if username == "Kamal" and password == "1234":
    print ("Hello Kamal welcome to the vault")
elif username == "Mr.Linowski" and password =="ABCD":
    print("Hello Mr.Linowksi Welcome the the vault")
    
    
else:
    print("\033[31m ACCESS DENIED AUTHORITY HAVE BEEN CALLED\033[m")