import os
import shutil
import sys

from copy_static import copy_static_files
from generate_page import generate_files_recusive


dir_path_static = "./static"
dir_path_public = "./docs"
index_path = "./content"
template_path = "./template.html"
dst_index_file = "index.html"
dst_index_path = os.path.join(dir_path_public,dst_index_file)

if len(sys.argv) > 1:
    basepath = sys.argv[1]
else:
    basepath = '/'

def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_static_files(dir_path_static, dir_path_public)

    print("Generating files to public directory...")
    generate_files_recusive(index_path, template_path, dir_path_public, basepath)



main()
