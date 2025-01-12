# Hosts File Website Blocker

This Python script allows you to block or unblock websites by modifying the `hosts` file on your system. It redirects specified websites to the localhost IP (`127.0.0.1`), effectively preventing access to them. The script supports importing and exporting blocked websites and provides a simple command-line interface for managing the block list.

## Features

- Block websites by adding entries to the `hosts` file.
- Unblock websites by removing their entries from the `hosts` file.
- Import a list of websites to block from a file.
- Export the current list of blocked websites to a file.
- View all currently blocked websites.
- User-friendly command-line interface with help commands.

## Requirements

- Python 3.x
- Administrator privileges (required to modify the `hosts` file).

## How It Works

1. **Blocking a Website**:
   - The script adds an entry to the `hosts` file in the format:
     ```
     127.0.0.1 <website>
     127.0.0.1 www.<website>
     ```
   - This redirects the domain to `127.0.0.1`, which is the localhost, effectively blocking access.

2. **Unblocking a Website**:
   - The script removes the corresponding entries from the `hosts` file.

3. **Attributes Management**:
   - On Windows systems, the script temporarily removes the `System`, `Read-only`, and `Hidden` attributes from the `hosts` file using the command:
     ```
     attrib -s -r -h <hosts_file_path>
     ```
   - After modifications, the attributes are restored.

4. **Importing and Exporting**:
   - Websites can be imported from a text file containing a list of URLs.
   - Blocked websites can be exported to a text file for backup.

## Usage

### Commands

- `help`: Display the help menu with available commands.
- `check`: List all blocked websites.
- `del`: Unblock a website (displays blocked websites for selection).
- `export`: Export the current list of blocked websites to a file.
- `import`: Import a list of websites to block from a file.
- `<website_url>`: Directly block the specified website.

### Example Workflow

1. **Run the Script**:
   ```
   python website_blocker.py
   ```

2. **Block a Website**:
   - Enter the URL of the website (e.g., `youtube.com`).
   - Confirm the action when prompted.

3. **View Blocked Websites**:
   - Type `check` to see a list of currently blocked websites.

4. **Unblock a Website**:
   - Type `del` and follow the prompts to select a website to unblock.

5. **Export Blocked Websites**:
   - Type `export` to save the block list to a file.

6. **Import Websites to Block**:
   - Type `import` and provide the file path containing the list of websites.

## File Paths

- **Hosts File**:
  - Windows: `C:\Windows\System32\drivers\etc\hosts`
  - Linux/Mac: `/etc/hosts`

- **Export Path**:
  - Windows: `M:\Downloads\BlockedWebsiteExports\hosts.txt`
  - Linux/Mac: `/home/ubuntu/Downloads/hosts.txt`

## Notes

- **Administrator Privileges**: The script requires elevated privileges to modify the `hosts` file.


