import os
import tarfile
import time
import sys
from PIL import Image

#note: num files is not read from the archive itself as
# I couldn't figure out how to avoid extracting the entire archive
# with my archive settings.  It is hardcoded in this example
num_files = 2017 #8726

archive_file_path = r'sprites.tar.xz'
output_dir = r'.'

if len(sys.argv) == 3:
    archive_file_path = sys.argv[1]
    output_dir = sys.argv[2]

t = tarfile.open(archive_file_path, 'r:xz')

time_job_start = time.time()
for i, fileinfo in enumerate(t):
    time_passed = time.time() - time_job_start + .1
    rate = time_passed / (i + 1)
    estimated_time_remaining = (num_files-i) * rate
    print('{:4d} of {:4d} ({:.2f}%) eta: {:3d}min {:2d}s - {}'.format(i+1, num_files, (i+1)/ num_files*100, int(estimated_time_remaining/60) , int(estimated_time_remaining%60), fileinfo.name))

    filename_no_ext, ext = os.path.splitext(fileinfo.name)


    if fileinfo.isfile():
        #skip non-bmp files
        if not (ext == '.png' or ext == '.bmp'):
            continue

        x = t.extractfile(fileinfo)
        im = Image.open(x)

        final_image_path = os.path.join(output_dir, filename_no_ext + '.png')
        im.save(final_image_path)
    else:
        os.makedirs(os.path.join(output_dir, fileinfo.name), exist_ok=True)
