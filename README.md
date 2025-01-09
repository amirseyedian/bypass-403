# 403 Bypass Script

This script attempts to bypass 403 Forbidden access restrictions by appending and modifying URL paths in different ways. It generates a list of URL variations based on encoding, path traversal, and other techniques.

## How It Works

The script takes a target domain as an argument and appends various URL encoding tricks, path traversal techniques, and common bypass patterns to the given domain. It then attempts to access each generated URL.

## Usage

Run the script with the target domain as an argument:

```sh
python bypass_403.py example.com
```

Run with custom path. example: /secret/

```shell
python bypass_403.py example.com /secret/
```

Features
• Tries different URL encoding techniques
• Uses path traversal and directory manipulation
• Attempts access with special characters and encodings
• Generates multiple variations of the /admin path

By using different encoding techniques and special characters, the script attempts to find alternate paths that may bypass 403 restrictions.

**_Disclaimer: Use this tool responsibly and only on systems where you have permission._**
