# py-archive-extractor-processor
python script to extract files from a .tar.xz file and process the files in memory (process files directly from an archive)

## Usage:

With python installed, call the script as follows:

` py decompress [archive_file] [output_folder]

- archive_file - the name/path to a .tar.xz file. You can generate this kind of file using 7zip by making a .tar file, then compressing it in the .xz format. You can also use Python's tar library, and pass the 'w:xz' to the 'open' function (I don't think the compression is as good though).

- output_folder - the files will be created in this output folder, preserving the folder structure is present inside the .tar.xz file