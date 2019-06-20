#!/usr/bin/python
from hashlib import *
from termcolor import *
def exiting():
              _hash = input("[+hash+]==================>>>")
              file1 = input("[+path+]==================>>>")
              with open(file1,mode="r") as f:
                                             for l in f:
                                                        line=l.strip()
                                                        if md5(line.encode()).hexdigest()==_hash:
                                                                                                 print("[+]password cracked")
                                                                                                 co = colored(line,"green")
                                                                                                 print("[+]password is:",co)
                                                                                                 break;
                                                        else:
                                                             o = "[+]password not found"
                                                             error = colored(o,"red")
                                                             print(error)
              
_hash = input("[+hash+]==================>>>")
file1 = input("[+path+]==================>>>")
try:
    with open(file1,mode="r") as f:
                                   for l in f:
                                              line=l.strip()
                                              if md5(line.encode()).hexdigest()==_hash:
                                                                                       print("[+]password cracked")
                                                                                       co = colored(line,"green")
                                                                                       print("[+]password is:",co)
                                                                                       break;
                                              else:
                                                   o = "[+]password not found"
                                                   error = colored(o,"red")
                                                   print(error)
except FileNotFoundError as e1:
                               co2 = colored("[+]please enter right path and try again","red")                                                
                               print(co2)
except KeyboardInterrupt as e2:
                               m = colored("are you sure to exit[y/n]","yellow")
                               print(m)
                               choice1 = input("=========>")
                               if choice == "y":
                                                exiting()
                               elif choice == "Y":
                                                  exiting()
                               elif choice == "n":
                                                  print("exited successfully!!!")
                               elif choice == "N":
                                                  print("exited successfully!!!")
                               else:
                                    print("invalid choice")
                                                                                             
