from duplicate_finder import find_duplicates
import io
from contextlib import redirect_stdout
from unittest.mock import patch
import hash_checker
import tempfile
import unittest
from pathlib import Path

from hash_checker import calculate_hash


class TestFileHashes(unittest.TestCase):
    def test_identical_files_have_matching_hashes(self):
        with tempfile.TemporaryDirectory() as folder:
            first = Path(folder) / "first.txt"
            second = Path(folder) / "second.txt"

            first.write_bytes(b"Historical archive record")
            second.write_bytes(b"Historical archive record")

            self.assertEqual(
                calculate_hash(first),
                calculate_hash(second),
            )

    def test_different_files_have_different_hashes(self):
        with tempfile.TemporaryDirectory() as folder:
            first = Path(folder) / "first.txt"
            second = Path(folder) / "second.txt"

            first.write_bytes(b"Original archive record")
            second.write_bytes(b"Changed archive record")

            self.assertNotEqual(
                calculate_hash(first),
                calculate_hash(second),
            )

class TestArchiveIntegrity(unittest.TestCase):
    def test_modified_file_is_detected(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            archive = root / "archive"
            archive.mkdir()

            record = archive / "record.txt"
            record.write_bytes(b"Original record")

            temporary_manifest = root / "checksums.json"

            with patch.object(
                hash_checker, "MANIFEST", temporary_manifest
            ):
                with redirect_stdout(io.StringIO()):
                    hash_checker.create_baseline(archive)

                record.write_bytes(b"Updated record")

                output = io.StringIO()
                with redirect_stdout(output):
                    hash_checker.verify_archive(archive)

            self.assertEqual(
                output.getvalue().strip(),
                "MODIFIED: record.txt",
            )
class TestDuplicateFinder(unittest.TestCase):
    def test_duplicate_files_are_identified(self):
        with tempfile.TemporaryDirectory() as folder:
            archive = Path(folder)

            (archive / "original.txt").write_bytes(b"Archive record")
            (archive / "copy.txt").write_bytes(b"Archive record")
            (archive / "unique.txt").write_bytes(b"Different record")

            output = io.StringIO()
            with redirect_stdout(output):
                find_duplicates(archive)

            lines = output.getvalue().splitlines()

            self.assertIn("DUPLICATE FILES FOUND:", lines)
            self.assertIn("  - original.txt", lines)
            self.assertIn("  - copy.txt", lines)
            self.assertNotIn("  - unique.txt", lines)
            self.assertNotIn("No duplicate files found.", lines)
if __name__ == "__main__":
    unittest.main()