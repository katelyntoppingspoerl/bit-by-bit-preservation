
from pathlib import Path
from collections import defaultdict
import hashlib


def calculate_hash(file_path):
    """Calculate the SHA-256 hash of a file."""
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(65536), b""):
            sha256.update(chunk)

    return sha256.hexdigest()


def find_duplicates(folder_path):
    """Find files with identical contents."""
    folder = Path(folder_path)

    if not folder.is_dir():
        print("Error: Folder does not exist.")
        return

    hashes = defaultdict(list)

    for file in sorted(folder.rglob("*")):
        if file.is_file():
            try:
                file_hash = calculate_hash(file)
                hashes[file_hash].append(
                    str(file.relative_to(folder))
                )
            except OSError as error:
                print(f"Could not read {file}: {error}")

    duplicates_found = False

    for file_hash, filenames in hashes.items():
        if len(filenames) > 1:
            duplicates_found = True
            print("\nDUPLICATE FILES FOUND:")
            for filename in filenames:
                print(f"  - {filename}")

    if not duplicates_found:
        print("No duplicate files found.")

    print("\nScan complete. No files were deleted.")


if __name__ == "__main__":
    print("ARCHIVE GUARDIAN - DUPLICATE FINDER")
    folder_path = input("Enter folder to scan: ")
    find_duplicates(folder_path)
