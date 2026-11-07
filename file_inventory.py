
from pathlib import Path
import csv

def create_inventory(folder_path):
    folder = Path(folder_path)
    records = []

    if not folder.is_dir():
        print("Error: Folder does not exist.")
        return

    for file in folder.rglob("*"):
        if file.is_file():
            records.append({
                "filename": file.name,
                "extension": file.suffix,
                "size_bytes": file.stat().st_size,
                "path": str(file.relative_to(folder))
            })

    with open("inventory_report.csv", "w", newline="", encoding="utf-8") as report:
        writer = csv.DictWriter(
            report,
            fieldnames=["filename", "extension", "size_bytes", "path"]
        )
        writer.writeheader()
        writer.writerows(records)

    print(f"Inventory complete: {len(records)} files recorded.")

if __name__ == "__main__":
    folder_path = input("Enter the folder path to scan: ")
    create_inventory(folder_path)
