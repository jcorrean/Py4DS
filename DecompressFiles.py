```{python}
import bz2
from pathlib import Path

def decompress_bz2_files(directory_path):
    """Decompresses .bz2 files only if the corresponding CSV files don't exist.

    Args:
        directory_path (str): Path to the directory containing .bz2 files.
    """

    for file in Path(directory_path).rglob('*.bz2'):
        output_file = str(file).replace('.bz2', '')

        # Check if the output CSV file already exists
        if not Path(output_file).exists():
            with bz2.open(file, 'rb') as bz_file:
                decompressed_data = bz_file.read()

            with open(output_file, 'wb') as out_file:
                out_file.write(decompressed_data)
            print(f"Decompressed: {file}")
        else:
            print(f"CSV file already exists: {output_file}")

# Replace 'your_directory_path' with the actual path to your .bz2 files
directory_path = '/home/jcc/dataverse_files'
decompress_bz2_files(directory_path)
```
