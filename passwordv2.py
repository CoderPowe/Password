import os
from random import randint as Rand
from colorama import Fore,Style
from getpass import getpass
from pyfiglet import figlet_format as ff
RAW_PASSWORD = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!?@#$%&"
def genPassword(length_of_password):
    i=0
    password=""
    while i<length_of_password:
        password+=RAW_PASSWORD[Rand(0,len(RAW_PASSWORD)-1)]
        i+=1 
    return password
def getAdminPassword():
    with open("admin1.txt","r") as f:
        encrypted_password = f.readlines()
        res = Decrypt(encrypted_password[0][:len(encrypted_password[0])-1])
    return res
def hlp():
    print(Fore.GREEN)
    print("generate -- [Generate password]")
    print("exit -- [Exit the tool]")
    print("help -- [Get User help]")
    print("clear -- [Clear console]")
    print("save -- [Save password]")
    print("see -- [See password]")
    print("update -- [Update password]")
    print("delete -- [Delete a record]")
    print("check -- [Full data of all users (only for admin)]")
    print("change -- [Change the admin password]")
    print("reset -- [Reset all data of the tool]")
    print("list -- [Generate list of passwords]")
    print(Style.RESET_ALL)
def clr():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')
    cl = ["red","blue","green"][Rand(0,2)]
    Heading("Password v2.0",cl)
    print("\n\n\n")
def capitalize(data):
    res = ""
    pos = 0
    for i in data:
        if i != " ":
         if pos == 0:
            res += i.upper()
            pos = 1
         else:
            res += i
        else:
            pos = 0
    return res
def save(filename, name, password, app, login = ""):
    f=open(filename,"a")
    if login == "":
        msg_wrt = Encrypt(capitalize(name)+"-"+capitalize(app)+"-"+password+"-")+"\n"
    else:
        msg_wrt = Encrypt(capitalize(name)+"-"+capitalize(app)+"-"+password+"-"+capitalize(login)+"-")+"\n"
    f.write(msg_wrt)
    f.close()
def see(filename,name,app,login=""):
    found=False
    name=capitalize(name)
    app=capitalize(app)
    login=capitalize(login)
    try:
        f=open(filename,'r')
        lines=f.readlines()
        f.close()
        for each_line in lines:
            line=Decrypt(each_line[:len(each_line)-1])
            data=[]
            i=0
            datum=""
            lg=""
            while i<len(line):
                if line[i]!="-":
                    datum+=line[i]
                else:
                    data.append(datum)
                    datum=""
                i+=1
            nm=data[0]
            ap=data[1]
            ps=data[2]
            if len(data)>3: 
               lg=data[3]
            if name==nm and ap==app and lg==login:
                result=ps
                found=True
                break
        if not found:
            result=1    
        return result 
    except:
        print(Fore.BLUE+"No database exists !!"+Style.RESET_ALL)
        return 1
def delete(filename,name,app,login=""):
    name=capitalize(name)
    app=capitalize(app)
    login=capitalize(login)
    try:
        f=open(filename,"r")
        lines=f.readlines()
        f.close()
        index=0
        while index<len(lines):
            line=Decrypt(lines[index][:len(lines[index])-1])
            data=[]
            i=0
            datum=""
            lg=""
            while i<len(line):
                if line[i]!="-":
                    datum+=line[i]
                else:
                    data.append(datum)
                    datum=""
                i+=1
            nm=data[0]
            ap=data[1]
            ps=data[2]
            if len(data)>3: 
               lg=data[3]
            if name == nm and ap == app and lg == login:
                del lines[index]
                f=open(filename,"w")
                f.writelines(lines)
                f.close()
                return 0
            index+=1
        return 1
    except:
        print(Fore.BLUE+"No database exists !!"+Style.RESET_ALL)
        return 1
def update(filename,name,app,password,login=""):
    result=delete(filename,name,app,login)
    if result==1:
        print(Fore.BLUE+"No data found !!"+Style.RESET_ALL)
    else:
        save(filename,name,password,app,login)
        print("Updated successfully...")
def check(filename):
    try:
      f=open(filename,"r")
      Cipher_lines=f.readlines()
      f.close()
      normal_data=[]
      for text in Cipher_lines:
        normal_data.append(Decrypt(text[:len(text)-1]))
      return normal_data
    except:
        print(Fore.BLUE+"No database exists !!"+Style.RESET_ALL)
        return 1
def reset():
        if "user_data1.txt" in os.listdir():
            os.remove("user_data1.txt")
            print(Fore.BLUE+"All user data deleted successfully !!"+Style.RESET_ALL)
        else:
            print(Fore.BLUE+"No database exists !!"+Style.RESET_ALL)
def change_password(new_password):
        with open("admin1.txt","w") as f:
            f.write(Encrypt(new_password)+"\n")
        print(Fore.GREEN+"Password changed successfully !!"+Style.RESET_ALL)
def Heading(heading,color):
    if color=="red":
      print(Fore.RED)
    elif color=="blue":
        print(Fore.BLUE)
    elif color=="green":
        print(Fore.GREEN)
    print(ff(heading))
    print(Style.RESET_ALL)
def Encrypt(data):
    data = data[::-1]
    cisear = ""
    cipher = ""
    for i in data:
        cisear += chr(ord(i)+1)
    for i in cisear:
        if ord(i) >= 65 and ord(i) <= 90:
            cipher += chr(155-ord(i))
        elif ord(i) >= 97 and ord(i) <= 122:
            cipher += chr(219-ord(i))
        elif ord(i) >= 48 and ord(i) <= 57:
            cipher += chr(105-ord(i))
        else:
            cipher += i
    return cipher
def Decrypt(cipher):
    data = ""  
    cisear = ""
    for i in cipher:
        if ord(i) >= 65 and ord(i) <= 90:
            cisear += chr(155-ord(i))
        elif ord(i) >= 97 and ord(i) <= 122:
            cisear += chr(219-ord(i))
        elif ord(i) >= 48 and ord(i) <= 57:
            cisear += chr(105-ord(i))
        else:
            cisear += i
    for i in cisear:
         data += chr(ord(i)-1)
    return  data[::-1]
if __name__=="__main__":
    Heading("Password","red")
    print("\n\n")
    database_name="user_data1.txt"
    admin="admin1.txt"
    if admin not in os.listdir():
        su_pass=getpass(Fore.RED+"Set admin password: "+Style.RESET_ALL)
        f=open(admin,"w")
        f.write(Encrypt(su_pass)+"\n")
        f.close()
        clr()
    su_pass=getpass(Fore.RED+"[+]Admin password: "+Style.RESET_ALL)
    if su_pass == getAdminPassword():
       clr()
       while True:
            command=input(Fore.GREEN+"command> "+Style.RESET_ALL)
            if command=="exit":
                exit()
            elif command=="generate":
                LEN_PASS=int(input("Password length: "))
                password = genPassword(LEN_PASS)
                print("Your password is: "+Fore.RED+password+Style.RESET_ALL+"\n")
            elif command=="clear":
                clr()
            elif command=="help":
                hlp()
            elif command=="save":
                usr_nm=input("User name: ")
                pass_of=input("Password of: ")
                login=input("Account logged in with(optional): ")
                new_p=input(Fore.GREEN+"Password: "+Style.RESET_ALL)
                if login=="\n":
                   save(database_name,usr_nm,new_p,pass_of)
                else:
                   save(database_name,usr_nm,new_p,pass_of,login)
                print("Password saved...")
            elif command=="see":
                usr_nm=input("User name: ")
                pass_of=input("Password of: ")
                login=input("Account logged in with(optional): ")
                if login=="\n":
                    result=see(database_name,usr_nm,pass_of)
                else:
                    result=see(database_name,usr_nm,pass_of,login)
                if result==1:
                    print(Fore.BLUE+"No password found!!"+Style.RESET_ALL)
                else:
                    print("Password: "+Fore.GREEN+result+Style.RESET_ALL)
            elif command=="delete":
                   usr_nm=input("User name: ")
                   pass_of=input("Password of: ")
                   login=input("Account logged in with(optional): ")
                   if login=="\n":
                       result=delete(database_name,usr_nm,pass_of)
                   else:
                       result=delete(database_name,usr_nm,pass_of,login)
                   if result==1:
                       print(Fore.BLUE+"No data found !!"+Style.RESET_ALL)
                   else:
                       print("Successfully deleted...")
            elif command=="update":
                usr_nm=input("User name: ")
                pass_of=input("Password of: ")
                login=input("Account logged in with(optional): ")
                pss=input("New password: ")
                if login=="\n":
                    update(database_name,usr_nm,pass_of,pss)
                else:
                    update(database_name,usr_nm,pass_of,pss,login)
            elif command=="check":
                su_pass=getpass(Fore.RED+"[+]Admin password: "+Style.RESET_ALL)
                if su_pass == getAdminPassword():
                    content=check(database_name)
                    if content!=1:
                        clr()
                        print(Fore.RED)
                        i=1
                        for text in content:
                            print(i,"> ",text)
                            i+=1
                        print(Style.RESET_ALL)
                        inp=input("\n\nEnter any key to continue...")
                        clr()
                else:
                    print(Fore.BLUE+"Cannot see sensitive data !!"+Style.RESET_ALL) 
            elif command=="reset":
                print(Fore.BLUE+"After reset the tool will be closed !!"+Style.RESET_ALL)
                ch=input(Fore.RED+"Reset all user data?(Y/any key): "+Style.RESET_ALL)
                if ch=="Y":
                    su_pass=getpass(Fore.RED+"\n[+]Admin password(required): "+Style.RESET_ALL)
                    if su_pass == getAdminPassword():
                        reset()
                        exit()
                    else:
                        print(Fore.BLUE+"Wrong admin password entered !!"+Style.RESET_ALL)
            elif command=="change":
                existing_password=getpass(Fore.RED+"\nOld password(required): "+Style.RESET_ALL)
                if existing_password==getAdminPassword():
                      new_password=getpass(Fore.GREEN+"\nNew password(required): "+Style.RESET_ALL)
                      change_password(new_password)
                else:
                    print(Fore.BLUE+"Wrong admin password entered !!"+Style.RESET_ALL)
            elif command == "list":
                LEN_PASS=int(input("Password length: "))
                numberOfPassword = int(input("List Length: "))
                print("List------------\n")
                i = 0
                while i < numberOfPassword:
                     password = genPassword(LEN_PASS)
                     print(f"{i+1}. "+Fore.RED + password+Style.RESET_ALL)
                     i += 1
            else:
                print(Fore.BLUE+"You entered wrong command !! Try again !!"+Style.RESET_ALL+"\n")
    else:
        exit()