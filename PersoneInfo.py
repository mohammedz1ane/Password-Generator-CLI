import csv
import os
from datetime import datetime
import Theme
import itertools


def save_to_csv(info):
    directory = './personInfo'
    os.makedirs(directory, exist_ok=True)
    
    base_filename = f"{info['first_name']}_{info['last_name']}.csv"
    filename = base_filename
    version = 1
    
    while os.path.exists(os.path.join(directory, filename)):
        version += 1
        filename = f"{info['first_name']}_{info['last_name']}V{version}.csv"
    
    filepath = os.path.join(directory, filename)
    
    with open(filepath, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for key, value in info.items():
            writer.writerow([key, value])
    
    print(f"Information saved to {filepath}")


def collect_information():
    print(f'{Theme.GREEN}{Theme.BOLD}Now we start Collecting info {Theme.RESET}')
    info = {}
    
    info['first_name'] = input('Enter first name: ')
    info['last_name'] = input('Enter last name: ')
    info['middle_name'] = input('Enter middle name: ')
    
    # Birth Date
    while True:
        birth_date = input('Enter birth date (YYYY-MM-DD): ')
        try:
            datetime.strptime(birth_date, '%Y-%m-%d')
            info['birth_date'] = birth_date
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
    
    info['partner_name'] = input('Enter partner name: ')
    info['company_name'] = input('Enter company name or work name: ')
    info['city_name'] = input('Enter city name: ')
    
    # Pets
    pets = []
    while True:
        pet = input('Enter pet name (or press Enter to finish): ')
        if pet == '':
            break
        pets.append(pet)
    if pets:
        info['pets'] = ', '.join(pets)
    
    children = []
    while True:
        child_name = input('Enter child name (or press Enter to finish): ')
        if child_name == '':
            break
        child_birth_date = input(f'Enter birth date for {child_name} (YYYY-MM-DD): ')
        children.append(f"{child_name} ({child_birth_date})")
    if children:
        info['children'] = '; '.join(children)
    
    while True:
        key = input('Enter additional info key (or press Enter to finish): ')
        if key == '':
            break
        value = input(f'Enter value for {key}: ')
        info[key] = value
    save_to_csv(info)
    return info




def generate_passwords(info, filepath):
    passwords = set()
    basic_info = [
        info.get('first_name', ''),
        info.get('last_name', ''),
        info.get('middle_name', ''),
        info.get('birth_date', '').replace('-', ''),
        info.get('partner_name', ''),
        info.get('company_name', ''),
        info.get('city_name', '')
    ]
    
    for r in range(1, 4):
        for combo in itertools.permutations(basic_info, r):
            passwords.add(''.join(combo))
    
    separators = ['', '_', '.', '-']
    suffixes = ['', '123', '!', '@', '#', '1234', '12345']
    
    temp_passwords = set(passwords)
    for password in temp_passwords:
        for sep in separators:
            for suffix in suffixes:
                passwords.add(f"{password}{sep}{suffix}")
    
    if 'pets' in info:
        pets = info['pets'].split(', ')
        passwords.update(pets)
    
    if 'children' in info:
        children = [child.split(' (')[0] for child in info['children'].split('; ')]
        passwords.update(children)
    
    for key, value in info.items():
        if key not in ['first_name', 'last_name', 'middle_name', 'birth_date', 'partner_name', 'company_name', 'city_name', 'pets', 'children']:
            passwords.add(value)
    
    with open(filepath, 'w') as f:
        for password in sorted(passwords):
            f.write(f"{password}\n")
    
    print(f"Generated {len(passwords)} potential passwords and saved them to {filepath}")

    return len(passwords)


def read_csv_info(csv_file_path):
    info = {}
    try:
        with open(csv_file_path, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) == 2:
                    key, value = row
                    info[key.strip()] = value.strip()
    except FileNotFoundError:
        print(f"{Theme.RED}CSV file not found. Please check the file path.{Theme.RESET}")
    except csv.Error as e:
        print(f"{Theme.RED}Error reading CSV file: {e}{Theme.RESET}")
    return info