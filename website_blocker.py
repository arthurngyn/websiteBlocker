import os 
import platform 

# Check if the OS is Windows
is_windows_os = platform.system() == 'Windows'

# Change to adjust for your own path 
if is_windows_os:
    hosts_path = "C:\\Windows\\System32\\drivers\\etc\\hosts"
    export_path = "M:\\Downloads\\BlockedWebsiteExports"
else:
    hosts_path = "/etc/hosts"
    export_path = '/home/ubuntu/Downloads/'

# Localhost IP
redirect = "127.0.0.1"

# Write website to hosts file 
def write(hosts_path, website_list, flag, redirect, is_windows_os) -> None:
    if is_windows_os:
        os.system(f'attrib -s -r -h "{hosts_path}"') 
    with open(hosts_path, "r+", encoding="UTF-8") as host:
        file_data = host.readlines()
        for website in website_list:
            if any(redirect in line and website in line for line in file_data):
                print(f'\n\tWebsite "{website}" already exists in the block list.')
            else:
                if flag in ('yes', 'y'):
                    host.write(redirect + " " + website + "\n")
                    print(f'\n\tWebsite "{website}" has been added to the block list.')

    # Flush DNS cache
    if is_windows_os:
        os.system('ipconfig /flushdns')
    else:
        os.system('sudo systemctl restart nscd')

    print("\nDNS cache flushed!")


def delete() -> None:
    if is_windows_os:
        os.system('attrib -s -r -h %s' % hosts_path)
    try:
        # Display blocked websites
        print('\nBlocked websites:')
        with open(hosts_path, 'r', encoding='UTF-8') as fp:
            file_data = fp.readlines()
            blocked_websites = [line.strip().split()[1] for line in file_data if redirect in line]
            for website in blocked_websites:
                print(f" - {website}")

        string = input('\nEnter the website you want to unblock: ')
        if string in blocked_websites:
            with open(hosts_path, 'r+', encoding='UTF-8') as fp:
                file_data = fp.readlines()
                file_data.sort()
                content = (line for line in file_data if string not in line)
            with open(hosts_path, 'w+', encoding='UTF-8') as fpp:
                for i in content:
                    if i == '#':
                        fpp.write('\n')
                    fpp.write(i)
            print(f'\n"{string}" has been unblocked.')
        else:
            print(f'\n"{string}" is not in the block list.')

        if is_windows_os:
            os.system('attrib +s +r +h %s' % hosts_path)
    except PermissionError as error:
        print(error)

def check_file() -> None:
    try: 
        if is_windows_os:
            os.system('attrib -s -r -h %s' % hosts_path)
        with open(hosts_path, 'r+', encoding='UTF-8') as file:
            website_count = 0
            file_data = file.readlines()
            file_data.sort()
            for line in file_data:
                if redirect in line and 'www.' not in line:
                    website_count += 1 
                    print(line, sep="", end="")
            print(f'\nTotal websites: {website_count}')
        if is_windows_os:
            os.system('attrib +s +r +h %s' % hosts_path)
    except PermissionError as error:
        print(error)

def import_host(hosts_path, redirect, is_windows_os) -> None:
    file_to_be_imported = input('Enter file path to be imported: ')
    try:
        with open(file_to_be_imported, 'r+', encoding='UTF-8') as user_file:
            website_list = (line.strip('\n').strip(redirect).strip() for line in user_file.readlines() if redirect in line)
            flag = 'yes'
            write(hosts_path, website_list, flag, redirect, is_windows_os)
        print(f"Importing has been completed from \"{file_to_be_imported}\"")
        del website_list
    except PermissionError as error:
        print(error)

def export_host(export_path) -> None:
    try:
        if is_windows_os:
            os.system('attrib -s -r -h %s' % hosts_path)
        with open(hosts_path, 'r+', encoding='UTF-8') as file:
            file_data = file.readlines()
            file_data.sort()
            container = (line.strip('\n').strip() for line in file_data if redirect in line and 'www.' not in line)
            with open(export_path+'hosts.txt', 'w+', encoding='UTF-8') as export:
                for line in container:
                    export.write(line)
                    export.write('\n')
            print(f"Export successfully completed. Find your file here: \"{export_path+'hosts.txt'}\"")
            if is_windows_os:
                os.system('attrib +s +r +h %s' % hosts_path)
            del container
    except PermissionError as error:
        print(error)

def display_help() -> None:
    print("\nAvailable Commands:")
    print(" - help: Display this help message.")
    print(" - check: List all blocked websites.")
    print(" - del: Unblock a website (shows blocked websites first).")
    print(" - export: Export blocked websites to a file.")
    print(" - import: Import blocked websites from a file.")
    print(" - Type the website URL to block it.")

# Main loop
while True: 
    website_list = []
    WebSite = input("\nType 'help' for all commands\nEnter the website to block or command: ").strip()
    if WebSite.lower() == "help":
        display_help()
    elif WebSite.lower() == "check":
        check_file()
    elif WebSite.lower() == "del":
        delete()
    elif WebSite.lower() == "export":
        export_host(export_path)
    elif WebSite.lower() == "import":
        import_host(hosts_path, redirect, is_windows_os)
    elif "www" in WebSite:
        www_WebSite = WebSite[4:]
    else:
        www_WebSite = "www." + WebSite
    
    if WebSite not in ["help", "check", "del", "export", "import"]:
        flag = input(f'\nAre you sure you want to update "{WebSite}" on the block list? (Yes/Y to confirm, No/N to cancel): ').lower()
        if flag in ('no', 'n'):
            print("\nOperation canceled.")
            continue
        website_list.extend((WebSite, www_WebSite))
        try:
            write(hosts_path, website_list, flag, redirect, is_windows_os)
            del website_list
        except PermissionError as error:
            print(error)
