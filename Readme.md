# Password Generator CLI

This project is a command-line interface (CLI) tool for generating password lists based on personal information or numerical ranges. It's designed to help create comprehensive wordlists for security testing and password strength analysis.

## Features

- Generate number-based wordlists
- Create character-based wordlists using personal information
- Import personal information from CSV files
- Interactive menu for ease of use


## Installation

1. Clone this repository:
   ```
   git clone https://github.com/mohammedz1ane/Password-Generator-CLI.git
   cd Password-Generator-CLI
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

You can run the tool in interactive mode or use command-line arguments for specific tasks.

### Interactive Mode

Run the script without any arguments to enter interactive mode:

```
python main.py
```

### Command-line Arguments

1. Generate a number-based wordlist:
   ```
   python main.py number -n output.txt -s 1 -e 1000
   ```

2. Generate a character-based wordlist:
   ```
   python main.py char --name output.txt
   ```

3. Generate a wordlist from a CSV file:
   ```
   python main.py char --name output.txt --file input.csv
   ```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Disclaimer

This tool is for educational purposes only. Do not use it to attempt unauthorized access to any systems or accounts.