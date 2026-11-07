
from pathlib import Path
import hashlib
import json

MANIFEST = Path("checksums.json")


def calculate_hash(file_path):
    """Calculate the SHA-256 checksum of a file."""
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(65536), b""):
            sha256.update(chunk)

    return sha256.hexdigest()


def create_baseline(folder_path):
    """Record original checksums for an archive."""
    folder = Path(folder_path)
    checksums = {}

    if not folder.is_dir():
        print("Error: Folder does not exist.")
        return

    for file in sorted(folder.rglob("*")):
        if file.is_file():
            relative_path = str(file.relative_to(folder))
            checksums[relative_path] = calculate_hash(file)

    with open(MANIFEST, "w", encoding="utf-8") as output:
        json.dump(checksums, output, indent=4)

    print(f"Baseline created for {len(checksums)} files.")


def verify_archive(folder_path):
    """Compare current files against saved checksums."""
    folder = Path(folder_path)

    if not folder.is_dir():
        print("Error: Folder does not exist.")
        return

    if not MANIFEST.is_file():
        print("Error: No checksum baseline found.")
        return

    with open(MANIFEST, "r", encoding="utf-8") as source:
        original = json.load(source)

    current = {}

    for file in sorted(folder.rglob("*")):
        if file.is_file():
            relative_path = str(file.relative_to(folder))
            current[relative_path] = calculate_hash(file)

    for filename, original_hash in original.items():
        if filename not in current:
            print(f"MISSING: {filename}")
        elif current[filename] != original_hash:
            print(f"MODIFIED: {filename}")
        else:
            print(f"VERIFIED: {filename}")

    for filename in current:
        if filename not in original:
            print(f"NEW FILE: {filename}")


if __name__ == "__main__":
    print("ARCHIVE GUARDIAN - FILE INTEGRITY CHECKER")
    print("1. Create checksum baseline")
    print("2. Verify archive integrity")

    choice = input("Select an option (1 or 2): ")
    folder_path = input("Enter folder to scan: ")

    if choice == "1":
        create_baseline(folder_path)
    elif choice == "2":
        verify_archive(folder_path)
    else:
        print("Invalid option.")
