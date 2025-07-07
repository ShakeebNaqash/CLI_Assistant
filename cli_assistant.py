import os
import sys
import json
import datetime
import subprocess
import shutil
from pathlib import Path
import argparse

class CLIAssistant:
    def __init__(self):
        self.commands = {
            'help': self.show_help,
            'time': self.show_time,
            'date': self.show_date,
            'weather': self.get_weather,
            'calc': self.calculator,
            'note': self.note_manager,
            'todo': self.todo_manager,
            'files': self.file_operations,
            'system': self.system_info,
            'convert': self.unit_converter,
            'search': self.search_files,
            'history': self.show_history,
            'clear': self.clear_screen,
            'exit': self.exit_assistant,
            'quit': self.exit_assistant,
        }
        
        self.data_dir = Path.home() / '.cli_assistant'
        self.data_dir.mkdir(exist_ok=True)
        self.notes_file = self.data_dir / 'notes.json'
        self.todos_file = self.data_dir / 'todos.json'
        self.history_file = self.data_dir / 'history.json'
        
        self.load_data()
        
    def load_data(self):
        """Load persistent data from files"""
        self.notes = self.load_json(self.notes_file, {})
        self.todos = self.load_json(self.todos_file, [])
        self.history = self.load_json(self.history_file, [])
        
    def load_json(self, file_path, default):
        """Load JSON data from file with error handling"""
        try:
            if file_path.exists():
                with open(file_path, 'r') as f:
                    return json.load(f)
        except (json.JSONDecodeError, IOError):
            pass
        return default
        
    def save_json(self, file_path, data):
        """Save JSON data to file"""
        try:
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=2)
        except IOError as e:
            print(f"Error saving data: {e}")
            
    def add_to_history(self, command):
        """Add command to history"""
        timestamp = datetime.datetime.now().isoformat()
        self.history.append({'command': command, 'timestamp': timestamp})
        # Keep only last 100 commands
        self.history = self.history[-100:]
        self.save_json(self.history_file, self.history)
        
    def show_help(self, args=None):
        """Display help information"""
        help_text = """
CLI Assistant - Available Commands:

General:
  help          - Show this help message
  time          - Show current time
  date          - Show current date
  clear         - Clear screen
  exit/quit     - Exit the assistant

Productivity:
  note          - Note management (add, list, delete, search)
  todo          - Todo list management (add, list, done, delete)
  calc          - Calculator (basic math operations)
  
System:
  system        - Show system information
  files         - File operations (ls, find, size)
  search        - Search for files
  
Utilities:
  convert       - Unit conversions (length, weight, temperature)
  weather       - Simple weather info (placeholder)
  history       - Show command history

Usage Examples:
  note add "Meeting notes" "Discussed project timeline"
  todo add "Buy groceries"
  calc 15 * 8 + 32
  files ls /home/user
  convert 100 celsius fahrenheit
        """
        print(help_text)
        
    def show_time(self, args=None):
        """Show current time"""
        now = datetime.datetime.now()
        print(f"Current time: {now.strftime('%H:%M:%S')}")
        
    def show_date(self, args=None):
        """Show current date"""
        now = datetime.datetime.now()
        print(f"Current date: {now.strftime('%Y-%m-%d (%A)')}")
        
    def get_weather(self, args=None):
        """Placeholder weather function"""
        print("Weather service not implemented. Use 'curl wttr.in' for weather info.")
        
    def calculator(self, args):
        """Basic calculator"""
        if not args:
            print("Usage: calc <expression>")
            print("Example: calc 2 + 3 * 4")
            return
            
        expression = ' '.join(args)
        try:
            # Simple validation - only allow basic math operations
            allowed_chars = set('0123456789+-*/.() ')
            if not all(c in allowed_chars for c in expression):
                print("Error: Only basic math operations allowed")
                return
                
            result = eval(expression)
            print(f"{expression} = {result}")
        except Exception as e:
            print(f"Error calculating: {e}")
            
    def note_manager(self, args):
        """Note management system"""
        if not args:
            print("Usage: note <add|list|delete|search> [arguments]")
            return
            
        action = args[0].lower()
        
        if action == 'add':
            if len(args) < 3:
                print("Usage: note add <title> <content>")
                return
            title = args[1]
            content = ' '.join(args[2:])
            timestamp = datetime.datetime.now().isoformat()
            self.notes[title] = {'content': content, 'timestamp': timestamp}
            self.save_json(self.notes_file, self.notes)
            print(f"Note '{title}' added successfully")
            
        elif action == 'list':
            if not self.notes:
                print("No notes found")
                return
            for title, note in self.notes.items():
                print(f"\n{title}:")
                print(f"  {note['content']}")
                print(f"  Created: {note['timestamp'][:19]}")
                
        elif action == 'delete':
            if len(args) < 2:
                print("Usage: note delete <title>")
                return
            title = args[1]
            if title in self.notes:
                del self.notes[title]
                self.save_json(self.notes_file, self.notes)
                print(f"Note '{title}' deleted")
            else:
                print(f"Note '{title}' not found")
                
        elif action == 'search':
            if len(args) < 2:
                print("Usage: note search <keyword>")
                return
            keyword = args[1].lower()
            found = False
            for title, note in self.notes.items():
                if keyword in title.lower() or keyword in note['content'].lower():
                    print(f"\n{title}:")
                    print(f"  {note['content']}")
                    found = True
            if not found:
                print("No notes found matching the keyword")
                
    def todo_manager(self, args):
        """Todo list management"""
        if not args:
            print("Usage: todo <add|list|done|delete> [arguments]")
            return
            
        action = args[0].lower()
        
        if action == 'add':
            if len(args) < 2:
                print("Usage: todo add <task description>")
                return
            task = ' '.join(args[1:])
            todo_item = {
                'task': task,
                'done': False,
                'created': datetime.datetime.now().isoformat()
            }
            self.todos.append(todo_item)
            self.save_json(self.todos_file, self.todos)
            print(f"Todo added: {task}")
            
        elif action == 'list':
            if not self.todos:
                print("No todos found")
                return
            for i, todo in enumerate(self.todos, 1):
                status = "✓" if todo['done'] else "○"
                print(f"{i}. {status} {todo['task']}")
                
        elif action == 'done':
            if len(args) < 2:
                print("Usage: todo done <task_number>")
                return
            try:
                task_num = int(args[1]) - 1
                if 0 <= task_num < len(self.todos):
                    self.todos[task_num]['done'] = True
                    self.save_json(self.todos_file, self.todos)
                    print(f"Todo marked as done: {self.todos[task_num]['task']}")
                else:
                    print("Invalid task number")
            except ValueError:
                print("Task number must be a number")
                
        elif action == 'delete':
            if len(args) < 2:
                print("Usage: todo delete <task_number>")
                return
            try:
                task_num = int(args[1]) - 1
                if 0 <= task_num < len(self.todos):
                    deleted_task = self.todos.pop(task_num)
                    self.save_json(self.todos_file, self.todos)
                    print(f"Todo deleted: {deleted_task['task']}")
                else:
                    print("Invalid task number")
            except ValueError:
                print("Task number must be a number")
                
    def file_operations(self, args):
        """File operations"""
        if not args:
            print("Usage: files <ls|find|size> [path]")
            return
            
        action = args[0].lower()
        
        if action == 'ls':
            path = Path(args[1]) if len(args) > 1 else Path.cwd()
            try:
                if path.is_dir():
                    items = sorted(path.iterdir())
                    for item in items:
                        type_indicator = "/" if item.is_dir() else ""
                        print(f"{item.name}{type_indicator}")
                else:
                    print(f"{path} is not a directory")
            except PermissionError:
                print(f"Permission denied: {path}")
            except FileNotFoundError:
                print(f"Path not found: {path}")
                
        elif action == 'size':
            path = Path(args[1]) if len(args) > 1 else Path.cwd()
            try:
                if path.is_file():
                    size = path.stat().st_size
                    print(f"{path.name}: {self.format_bytes(size)}")
                elif path.is_dir():
                    total_size = sum(f.stat().st_size for f in path.rglob('*') if f.is_file())
                    print(f"{path.name}/: {self.format_bytes(total_size)}")
                else:
                    print(f"Path not found: {path}")
            except PermissionError:
                print(f"Permission denied: {path}")
                
    def format_bytes(self, bytes_size):
        """Format bytes in human readable format"""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if bytes_size < 1024.0:
                return f"{bytes_size:.1f} {unit}"
            bytes_size /= 1024.0
        return f"{bytes_size:.1f} TB"
        
    def system_info(self, args=None):
        """Display system information"""
        print(f"Operating System: {os.name}")
        print(f"Python Version: {sys.version}")
        print(f"Current Directory: {os.getcwd()}")
        print(f"Home Directory: {Path.home()}")
        
        # Disk usage
        try:
            disk_usage = shutil.disk_usage('/')
            total = disk_usage.total
            free = disk_usage.free
            used = total - free
            print(f"Disk Usage: {self.format_bytes(used)} / {self.format_bytes(total)} ({used/total*100:.1f}%)")
        except:
            print("Disk usage information not available")
            
    def unit_converter(self, args):
        """Unit conversion utility"""
        if len(args) < 3:
            print("Usage: convert <value> <from_unit> <to_unit>")
            print("Supported: celsius/fahrenheit, kg/lbs, m/ft, km/miles")
            return
            
        try:
            value = float(args[0])
            from_unit = args[1].lower()
            to_unit = args[2].lower()
            
            # Temperature conversions
            if from_unit == 'celsius' and to_unit == 'fahrenheit':
                result = (value * 9/5) + 32
                print(f"{value}°C = {result:.2f}°F")
            elif from_unit == 'fahrenheit' and to_unit == 'celsius':
                result = (value - 32) * 5/9
                print(f"{value}°F = {result:.2f}°C")
                
            # Weight conversions
            elif from_unit == 'kg' and to_unit == 'lbs':
                result = value * 2.20462
                print(f"{value} kg = {result:.2f} lbs")
            elif from_unit == 'lbs' and to_unit == 'kg':
                result = value / 2.20462
                print(f"{value} lbs = {result:.2f} kg")
                
            # Length conversions
            elif from_unit == 'm' and to_unit == 'ft':
                result = value * 3.28084
                print(f"{value} m = {result:.2f} ft")
            elif from_unit == 'ft' and to_unit == 'm':
                result = value / 3.28084
                print(f"{value} ft = {result:.2f} m")
                
            # Distance conversions
            elif from_unit == 'km' and to_unit == 'miles':
                result = value * 0.621371
                print(f"{value} km = {result:.2f} miles")
            elif from_unit == 'miles' and to_unit == 'km':
                result = value / 0.621371
                print(f"{value} miles = {result:.2f} km")
            else:
                print("Conversion not supported")
                
        except ValueError:
            print("Invalid value. Please enter a number.")
            
    def search_files(self, args):
        """Search for files"""
        if not args:
            print("Usage: search <filename_pattern> [directory]")
            return
            
        pattern = args[0]
        directory = Path(args[1]) if len(args) > 1 else Path.cwd()
        
        try:
            matches = list(directory.rglob(f"*{pattern}*"))
            if matches:
                print(f"Found {len(matches)} matches:")
                for match in matches[:20]:  # Limit to first 20 results
                    print(f"  {match}")
                if len(matches) > 20:
                    print(f"  ... and {len(matches) - 20} more")
            else:
                print("No matches found")
        except PermissionError:
            print(f"Permission denied: {directory}")
            
    def show_history(self, args=None):
        """Show command history"""
        if not self.history:
            print("No command history")
            return
            
        print("Recent commands:")
        for i, entry in enumerate(self.history[-10:], 1):
            timestamp = entry['timestamp'][:19]
            print(f"{i:2d}. {entry['command']} ({timestamp})")
            
    def clear_screen(self, args=None):
        """Clear the screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def exit_assistant(self, args=None):
        """Exit the assistant"""
        print("Goodbye!")
        sys.exit(0)
        
    def parse_command(self, command_line):
        """Parse command line into command and arguments"""
        parts = command_line.strip().split()
        if not parts:
            return None, []
        return parts[0].lower(), parts[1:]
        
    def execute_command(self, command, args):
        """Execute a command"""
        if command in self.commands:
            self.add_to_history(f"{command} {' '.join(args)}")
            self.commands[command](args)
        else:
            print(f"Unknown command: {command}")
            print("Type 'help' for available commands")
            
    def run(self):
        """Main interactive loop"""
        print("Welcome to CLI Assistant!")
        print("Type 'help' for available commands or 'exit' to quit.")
        
        while True:
            try:
                command_line = input("\n> ").strip()
                if not command_line:
                    continue
                    
                command, args = self.parse_command(command_line)
                if command:
                    self.execute_command(command, args)
                    
            except KeyboardInterrupt:
                print("\nExiting...")
                break
            except EOFError:
                print("\nExiting...")
                break

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description='CLI Assistant')
    parser.add_argument('command', nargs='*', help='Command to execute')
    
    args = parser.parse_args()
    
    assistant = CLIAssistant()
    
    # If command provided as arguments, execute it and exit
    if args.command:
        command = args.command[0].lower()
        command_args = args.command[1:]
        assistant.execute_command(command, command_args)
    else:
        # Interactive mode
        assistant.run()

if __name__ == "__main__":
    main()