# Directory Command Runner

A simple Python script to run commands in all subdirectories.

## Features

- **Default Command**: Runs `git pull` in all subdirectories.  
- **Custom Commands**: Specify any command with the `--command` option.  
- **Colored Output**: Highlights directory names for better readability.

EX.
```bash
gity --command "git pull"
```
## Usage

1. Install dependencies:
   ```bash
   pip install colorama
