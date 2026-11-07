# Bit-by-Bit Preservation
### A Digital Archive Integrity & Preservation Toolkit

**Preserving information, one bit at a time.**

Bit-by-Bit Preservation is a Python-based portfolio project exploring digital file integrity, archival organization, and preservation practices.

The project was developed to connect my background in records management, documentation, and information stewardship with the technical skills I gained through my IT training and CompTIA A+ certification.

Digital preservation involves more than storing files. It also means understanding whether those files have changed, identifying redundant copies, and maintaining accurate records of digital collections.

## Project Features

**1. File Inventory — `file_inventory.py`**

- Scans folders and subfolders.
- Records filenames, extensions, file sizes, and paths.
- Generates a CSV inventory report.

**2. File Integrity Verification — `hash_checker.py`**

- Generates SHA-256 checksums.
- Creates a baseline of original file hashes.
- Detects modified, missing, and newly added files.

**3. Duplicate File Detection — `duplicate_finder.py`**

- Identifies files with matching SHA-256 hashes.
- Detects duplicates even when filenames differ.
- Reports duplicate files without deleting or modifying them.

## Technologies Used

- Python 3
- Git and GitHub
- GitHub Codespaces
- SHA-256 hashing
- CSV and JSON
- File system operations

## Getting Started

Run the scripts from the repository's root directory using Python 3.

### Generate a File Inventory

```bash
python file_inventory.py
```

Enter `sample_data` when prompted.

### Create an Integrity Baseline

```bash
python hash_checker.py
```

Select option `1`, then enter `sample_data`.

### Verify File Integrity

Run `hash_checker.py` again, select option `2`, and enter `sample_data`.

### Find Duplicate Files

```bash
python duplicate_finder.py
```

Enter `sample_data` when prompted.

## Testing

The toolkit was tested using fictional archival records.

Testing included creating file inventories, generating checksum baselines, modifying documents to verify change detection, and creating identical files with different names to test duplicate identification.

No real archival records or confidential information were used.

## Limitations and Future Development

SHA-256 verification helps identify changes to file contents, but it does not independently establish authenticity, detect every form of corruption, or guarantee long-term accessibility.

Future improvements may include:

- File format identification and preservation risk reporting.
- Automated integrity reports.
- Improved error handling.
- Unit testing and automated validation.
- Expanded metadata collection.

## About This Project

My professional background includes public administration, records management, legal documentation, publishing, and independent business operations.

After completing my IT training and earning my CompTIA A+ certification, I wanted to create something that connected those experiences with my interest in digital archives and long-term information preservation.

This project is an opportunity to apply technical skills to a subject I genuinely care about: ensuring that information remains organized, trustworthy, and accessible for the people who need it.