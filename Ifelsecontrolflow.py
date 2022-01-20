#Control flow if, else and elif

if 1>2:
    print("Yep!")

if 1==2:
    print("Yep!")

username = "users"
Check = "Admin"
permission =True
if username == Check and permission:
    print("Access Granted")
elif username == "users":
     print("No admin access")
else:
    print("access denied")
