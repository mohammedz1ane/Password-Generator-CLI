import os
import argparse
import Theme
import time
import random
import PersoneInfo


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def showAnimatedASCIILogo():
    fire_colors = [Theme.RED, Theme.YELLOW, Theme.RESET]
    base_art =f"""
    (                                                                                                
    )\ )                                  (      (                                       )           
    (()/(    )          (  (         (     )\ )   )\ )      (           (   (       )  ( /(      (    
    /(_))( /(  (   (   )\))(    (   )(   (()/(  (()/(     ))\  (      ))\  )(   ( /(  )\()) (   )(   
    (_))  )(_)) )\  )\ ((_)()\   )\ (()\   ((_))  /(_))_  /((_) )\ )  /((_)(()\  )(_))(_))/  )\ (()\  
    | _ \((_)_ ((_)((_)_(()((_) ((_) ((_)  _| |  (_)) __|(_))  _(_/( (_))   ((_)((_)_ | |_  ((_) ((_) 
    |  _// _` |(_-<(_-<\ V  V // _ \| '_|/ _` |    | (_ |/ -_)| ' \))/ -_) | '_|/ _` ||  _|/ _ \| '_| 
    |_|  \__,_|/__//__/ \_/\_/ \___/|_|  \__,_|     \___|\___||_||_| \___| |_|  \__,_| \__|\___/|_|                                                                                                

    """     
    
    for _ in range(10):  
        clear_console()
        animated_art = ""
        for line in base_art.splitlines():
            colored_line = ""
            for char in line:
                if char != ' ':
                    colored_line += random.choice(fire_colors) + char + Theme.RESET
                else:
                    colored_line += char
            animated_art += colored_line + "\n"
        print(animated_art)
        time.sleep(0.1)



def showMenu():
    print(f"""
    {Theme.BOLD}Select your choice:{Theme.RESET}

        1) Make a number worldlist.
        2) Make a character worldlist.
        3) Select existing file (csv) and make a worldlist.

        {Theme.RED}Press (Q) to quit{Theme.RESET}
        """)
    while True:
        choice = input(f'{Theme.GREEN}\tEnter: {Theme.RESET}')

        if choice.lower() == 'q':
            break
        elif choice =='1':
            print(f"{Theme.CYAN}You selected option {choice}{Theme.RESET}")
            MakeNumberWorldList()
            

        elif choice =='2':
            print(f"{Theme.CYAN}You selected option {choice}{Theme.RESET}")
            MakeCharacterWorldList()
            
        elif choice =='3':
            print(f"{Theme.CYAN}You selected option {choice}{Theme.RESET}")
            MakeWorldListWithExistingFile()
        else:
            print(f"{Theme.RED}{Theme.BOLD}Invalid input: {Theme.YELLOW}{choice}{Theme.RED}. Choose 1, 2, 3, or Q.{Theme.RESET}")


def setFileDir(path):
    if os.path.exists(path):
        if os.path.isdir(path):
            print('this path is exist ')
            return True
        else:
            print(f'{Theme.RED}is not directory{Theme.RESET} ')
            return False
    else:
        print(f"{Theme.RED}{Theme.BOLD}This path does not exist{Theme.RESET}")  
        return False  

def getExistFile(path):
    if os.path.exists(path):
        if os.path.isfile(path): 
            print("File is exists") 
            return True
        else:
            print(f'{Theme.RED}This is not a file ?{Theme.RESET}')
    else:
        print(f"{Theme.RED}Chek you file path !?{Theme.RESET}")
    

def MakeNumberWorldList():
    while(True):
        path=input("Enter path (e.g., C:\\Users\\User\\Desktop\\):")
        name=input("Enter you file name file.txt) : ") 
        if setFileDir(path)==False:
            continue
        start=input("number of start ")
        end=input("number of End ")
        file_path=os.path.join(path,name)
        if NumberWorldlistFile(file_path,start,end):
            break
           
def MakeCharacterWorldList(file_path=None):
    while(True):
        if file_path==None:
             path=input("Enter path (e.g., C:\\Users\\User\\Desktop\\):")
             name=input("Enter you file name file.txt) : ") 
             if setFileDir(path)==False:
                 continue
             file_path=os.path.join(path,name)
        Info=PersoneInfo.collect_information()
        num_passwords=PersoneInfo.generate_passwords(Info,file_path)
        print(f"{Theme.GREEN}Generated {num_passwords} passwords and saved them to {file_path}{Theme.RESET}")

        break
        
      
def NumberWorldlistFile(filepath, start, end):
    try:
        with open(filepath, 'w') as f:
            start_int = int(start)
            end_int = int(end)
            use_leading_zeros = len(start) > len(str(start_int))      
            if use_leading_zeros:
                num_digits = len(start)  
                for i in range(start_int, end_int + 1): 
                    f.write(f"{i:0{num_digits}d}\n")
            else:
                if start_int<=end_int:
                    for i in range(start_int, end_int + 1):
                        f.write(f"{i}\n")
                else:
                     for i in range(start_int, end_int - 1,-1):
                        f.write(f"{i}\n")   
        print(f"Numbers from {start} to {end} have been written to {filepath}.")
    except IOError as e:
        print(f"An error occurred: {e}")
    return True

def MakeWorldListWithExistingFile(file_path=None,csv_info_file=None):
    while True:
        if file_path == None:
            path = input("Enter path for saving wordlist (e.g., C:\\Users\\User\\Desktop\\): ")
            name = input("Enter your file name for wordlist (e.g., wordlist.txt): ")
            if not setFileDir(path):
                continue
            
            file_path = os.path.join(path, name)
            csv_info_file = input(f'{Theme.ITALIC}Enter your CSV file path (e.g., C:\\Users\\User\\Desktop\\Info.csv): {Theme.RESET}')
            
        info = PersoneInfo.read_csv_info(csv_info_file)
        if not info:
            print(f"{Theme.RED}Failed to read information from CSV. Please check the file and try again.{Theme.RESET}")
            continue
        
        num_passwords = PersoneInfo.generate_passwords(info, file_path)
        print(f"{Theme.GREEN}Generated {num_passwords} passwords and saved them to {file_path}{Theme.RESET}")
        break


def parse_arguments():
    parser = argparse.ArgumentParser(description="Password Generator CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Number worldlist parser
    number_parser = subparsers.add_parser("number", help="Generate number worldlist")
    number_parser.add_argument("-n", "--name", required=True, help="Output file path")
    number_parser.add_argument("-s", "--start", required=True, type=int, help="Start number")
    number_parser.add_argument("-e", "--end", required=True, type=int, help="End number")

    # Character worldlist parser
    char_parser = subparsers.add_parser("char", help="Generate character worldlist")
    char_parser.add_argument("-char", "--name", help="Output file path")
    char_parser.add_argument("--file", help="Input CSV file path")

    return parser.parse_args()

def main():
    args = parse_arguments()

    if args.command == "number":
        NumberWorldlistFile(args.name, str(args.start), str(args.end))
    elif args.command == "char":
        if args.file:
            print(args.name,'\n',args.file)
            MakeWorldListWithExistingFile(args.name, args.file)
        else:
            MakeCharacterWorldList(args.name)
    else:
        showAnimatedASCIILogo()
        showMenu()


if __name__ == "__main__":
    main()
    
    