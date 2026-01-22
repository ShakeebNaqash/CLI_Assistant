# CLI Assistant

A feature-rich command-line assistant that provides productivity tools, system utilities, and persistent data management through an interactive terminal interface.

## 📋 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Available Commands](#available-commands)
- [Examples](#examples)
- [Data Storage](#data-storage)
- [Security](#security)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

- **Note Management**: Create, view, search, and delete notes
- **Todo List**: Manage tasks with completion tracking
- **Password Manager**: Securely store and retrieve passwords with encryption
- **Calculator**: Perform basic mathematical operations
- **File Operations**: Browse directories, check file sizes, and search files
- **Unit Converter**: Convert between different units (temperature, weight, length, distance)
- **System Information**: View system details and disk usage
- **Command History**: Keep track of your recent commands
- **Cross-platform**: Works on Windows, macOS, and Linux

## 🛠️ Tech Stack

- **Python 3.7+**
- **cryptography** - For password encryption (Fernet)
- **Standard Library Modules**:
  - `os`, `sys`, `json`, `datetime`
  - `pathlib`, `argparse`, `subprocess`, `shutil`
  - `getpass`, `secrets`, `hashlib`, `base64`

## 📦 Prerequisites

Before you begin, ensure you have the following installed:

1. **Python 3.7 or higher**
   - Check version: `python --version` or `python3 --version`
   - Download from: [python.org](https://www.python.org/downloads/)

2. **pip** (Python package installer)
   - Usually comes with Python
   - Check version: `pip --version` or `pip3 --version`

## 🚀 Installation

### Step 1: Clone or Download

Download the `cli_assistant.py` file to your local machine.

```bash
# If using git
git clone <repository-url>
cd cli-assistant

# Or simply download the cli_assistant.py file
```

### Step 2: Install Dependencies

Install the required Python package:

```bash
pip install cryptography
```

Or if you're using `pip3`:

```bash
pip3 install cryptography
```

### Step 3: Make Executable (Optional - Linux/macOS)

```bash
chmod +x cli_assistant.py
```

### Step 4: Verify Installation

Test that everything works:

```bash
python cli_assistant.py help
```

## 💻 Usage

### Interactive Mode (Recommended)

Launch the assistant in interactive mode:

```bash
python cli_assistant.py
```

You'll see:
```
Welcome to CLI Assistant!
Type 'help' for available commands or 'exit' to quit.

> 
```

Now you can type commands directly.

### Single Command Mode

Execute a single command and exit:

```bash
python cli_assistant.py <command> [arguments]
```

Example:
```bash
python cli_assistant.py calc 10 + 5
```

### Creating an Alias (Optional)

For easier access, create an alias:

**Linux/macOS** (add to `~/.bashrc` or `~/.zshrc`):
```bash
alias assistant='python3 /path/to/cli_assistant.py'
```

**Windows** (PowerShell profile):
```powershell
function assistant { python C:\path\to\cli_assistant.py $args }
```

Then use:
```bash
assistant
```

## 📚 Available Commands

### General Commands

| Command | Description |
|---------|-------------|
| `help` | Display all available commands |
| `time` | Show current time |
| `date` | Show current date |
| `clear` | Clear the terminal screen |
| `history` | Show command history (last 10) |
| `exit` / `quit` | Exit the assistant |

### Productivity Tools

#### Notes
- `note add <title> <content>` - Create a new note
- `note list` - List all notes
- `note delete <title>` - Delete a note
- `note search <keyword>` - Search notes by keyword

#### Todo List
- `todo add <task>` - Add a new task
- `todo list` - List all tasks
- `todo done <number>` - Mark task as complete
- `todo delete <number>` - Delete a task

#### Password Manager
- `password add <service> [username]` - Add a new password (secure prompt)
- `password get <service>` - Retrieve a password
- `password list` - List all stored services
- `password delete <service>` - Delete a password
- `password generate [length]` - Generate a strong random password

#### Calculator
- `calc <expression>` - Perform calculations

### System Utilities

#### File Operations
- `files ls [path]` - List directory contents
- `files size [path]` - Show file/directory size

#### Search
- `search <pattern> [directory]` - Search for files

#### System Info
- `system` - Display system information and disk usage

### Conversion Tools

- `convert <value> <from_unit> <to_unit>` - Convert between units

**Supported conversions:**
- Temperature: `celsius` ↔ `fahrenheit`
- Weight: `kg` ↔ `lbs`
- Length: `m` ↔ `ft`
- Distance: `km` ↔ `miles`

## 📖 Examples

### Note Management

```bash
> note add "Meeting" "Discussed Q1 goals and project timeline"
Note 'Meeting' added successfully

> note list

Meeting:
  Discussed Q1 goals and project timeline
  Created: 2026-01-22T10:30:00

> note search project

Meeting:
  Discussed Q1 goals and project timeline

> note delete "Meeting"
Note 'Meeting' deleted
```

### Todo List

```bash
> todo add Buy groceries
Todo added: Buy groceries

> todo add Complete project report
Todo added: Complete project report

> todo list
1. ○ Buy groceries
2. ○ Complete project report

> todo done 1
Todo marked as done: Buy groceries

> todo list
1. ✓ Buy groceries
2. ○ Complete project report

> todo delete 1
Todo deleted: Buy groceries
```

### Password Manager

```bash
> password add gmail john.doe@gmail.com
Enter password for gmail: ********
Confirm password: ********
Password for 'gmail' saved successfully

> password generate 20

Generated password (20 characters):
xK9$mN2@pL5#qR8&tY3%

Save this password? (yes/no): yes
Service name: github
Username (optional): johndoe
Password for 'github' saved successfully

> password list

Stored passwords:
  - gmail (john.doe@gmail.com)
  - github (johndoe)

> password get gmail

Service: gmail
Username: john.doe@gmail.com
Password: MySecurePass123!
Created: 2026-01-22T10:45:00
Modified: 2026-01-22T10:45:00

> password delete github
Delete password for 'github'? (yes/no): yes
Password for 'github' deleted
```

### Calculator

```bash
> calc 15 * 8
15 * 8 = 120

> calc (100 - 25) * 2 + 10
(100 - 25) * 2 + 10 = 160

> calc 3.14 * 5 * 5
3.14 * 5 * 5 = 78.5
```

### File Operations

```bash
> files ls
Documents/
Downloads/
Pictures/
cli_assistant.py
readme.md

> files size cli_assistant.py
cli_assistant.py: 15.2 KB

> search config .
Found 3 matches:
  ./config.json
  ./.config/settings
  ./backup/old_config.json

> files ls /home/user/Documents
project1/
project2/
notes.txt
```

### Unit Conversion

```bash
> convert 100 celsius fahrenheit
100.0°C = 212.00°F

> convert 75 kg lbs
75.0 kg = 165.35 lbs

> convert 10 km miles
10.0 km = 6.21 miles

> convert 6 ft m
6.0 ft = 1.83 m
```

### System Information

```bash
> system
Operating System: posix
Python Version: 3.11.5 (main, Sep 11 2023, 13:54:46)
Current Directory: /home/user/projects
Home Directory: /home/user
Disk Usage: 245.5 GB / 500.0 GB (49.1%)

> time
Current time: 14:32:15

> date
Current date: 2026-01-22 (Thursday)
```

### Command History

```bash
> history
Recent commands:
 1. note add "Meeting" "Project discussion" (2026-01-22T10:30:00)
 2. todo add Buy groceries (2026-01-22T10:31:00)
 3. calc 15 * 8 (2026-01-22T10:32:00)
 4. password list  (2026-01-22T10:33:00)
 5. system  (2026-01-22T10:34:00)
```

## 💾 Data Storage

All data is stored locally in your home directory:

```
~/.cli_assistant/
├── notes.json          # Your notes
├── todos.json          # Your todo list
├── history.json        # Command history
├── passwords.enc       # Encrypted passwords
└── .key                # Encryption key (keep secure!)
```

### Important Notes:

- **Backup**: Regularly backup the `~/.cli_assistant/` directory
- **Security**: The `.key` file is crucial for decrypting passwords. Keep it safe!
- **Permissions**: Password files have restricted permissions (600) for security
- **Privacy**: All data stays on your local machine

## 🔒 Security

### Password Manager Security Features:

1. **Encryption**: Uses Fernet (symmetric encryption) from the cryptography library
2. **Secure Input**: Passwords are never displayed while typing (uses `getpass`)
3. **File Permissions**: Automatically sets restrictive permissions (0o600)
4. **Strong Generation**: Uses `secrets` module for cryptographically secure random passwords
5. **Local Storage**: All data stored locally, never transmitted

### Best Practices:

- ✅ Keep your `~/.cli_assistant/.key` file secure
- ✅ Use strong passwords
- ✅ Regular backups of your data directory
- ✅ Don't share your encryption key
- ❌ Don't store the master key in version control
- ❌ Don't share passwords over unsecured channels

## 🐛 Troubleshooting

### "ModuleNotFoundError: No module named 'cryptography'"

**Solution**: Install the cryptography package
```bash
pip install cryptography
```

### "Permission denied" when accessing files

**Solution**: Check file permissions or run with appropriate user permissions
```bash
chmod 600 ~/.cli_assistant/.key
```

### Commands not working in interactive mode

**Solution**: Ensure you're typing commands correctly. Use `help` to see available commands.

### "python: command not found"

**Solution**: Try using `python3` instead, or ensure Python is in your PATH
```bash
python3 cli_assistant.py
```

### Encrypted passwords won't decrypt

**Solution**: Your `.key` file may be corrupted. If you have a backup, restore it. Otherwise, you'll need to delete the `.key` and `passwords.enc` files and start fresh (you'll lose saved passwords).

### Calculator showing incorrect results

**Solution**: Use spaces between operators and operands, and use parentheses for complex expressions
```bash
# Correct
> calc (10 + 5) * 2

# Incorrect
> calc 10+5*2
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Feature Ideas:

- Email integration
- Calendar events
- Habit tracking
- Budget tracker
- Contact manager
- Reminder system
- API integrations
- Export/import functionality

## 📄 License

This project is open source and available under the MIT License.

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Troubleshooting](#troubleshooting) section
2. Review the [Examples](#examples) for proper usage
3. Open an issue on the repository

## 🎉 Acknowledgments

Built with Python and the cryptography library. Special thanks to the open-source community.

---

**Made with ❤️ for productivity enthusiasts**

*Version 1.0.0 - Last updated: January 2026*