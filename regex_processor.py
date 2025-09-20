import re

def classify_with_regex(text):
    pattrens = {
        r"Backup (started|ended) at .*": "System Notification",
        r"User User\d+ logged (in|out)": "User Action",
        r"Backup completed successfully": "Syatem Notification",
        r"System updated to version .*": "system Notification",
        r"File .* uploaded Successfully.": "System Notification",
        r"Disk Cleanup completed successfully.": "System Notification",
        r"System reoot initiated by user .*": "System Notification",
        r"Account with id .* created by .*": "User Action"
    }

    for pattren, label in pattrens.items():
        if re.search(pattren, text, re.IGNORECASE):
            return label   
    return None

if __name__ == "__main__":
    test_strings = [
        "Backup started at 2023-10-01 10:00:00",
        "User User123 logged in",
        "Backup completed successfully",
        "System updated to version 1.2.3",
        "File report.pdf uploaded successfully.",
        "Disk Cleanup completed successfully.",
        "System reboot initiated by user Admin",
        "Account with id 456 created by Admin"
    ]

    for s in test_strings:
        label = classify_with_regex(s)
        print(f"Text: {s} => Label: {label}")