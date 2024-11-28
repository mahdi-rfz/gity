import os
from colorama import Fore
import argparse

dirList = os.listdir()

parser = argparse.ArgumentParser(description='notmot')
parser.add_argument("--command" , type = str , help = "run command for all dir")
args = parser.parse_args()


if args.command == None : 
    print(f"Command : git pull\n")
    for dir in dirList : 
        try : 
            print(Fore.GREEN + f"{dir} :" , Fore.RESET)
            os.system(f"cd {dir} && git pull")
        except : 
            pass
    
else : 
    print(f"Command : {args.command}\n")
    for dir in dirList : 
        try : 
            print(Fore.GREEN + f"{dir} :" , Fore.RESET)
            os.system(f"cd {dir} && {args.command}")
        except : 
            pass