import re
import sys


EMAIL_PATTERN = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"


def extract_emails(input_file, output_file="extracted_emails.txt"):
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: '{input_file}' not found.")
        sys.exit(1)

    emails = re.findall(EMAIL_PATTERN, content)
    unique_emails = sorted(set(emails))

    with open(output_file, "w", encoding="utf-8") as f:
        for email in unique_emails:
            f.write(email + "\n")

    print(f"Found {len(unique_emails)} unique email(s).")
    print(f"Saved to {output_file}")
    return unique_emails


if _name_ == "_main_":
    input_path = input("Enter path to the .txt file to scan: ").strip()
    extract_emails(input_path)