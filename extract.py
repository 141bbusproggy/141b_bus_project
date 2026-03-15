import os
import tarfile
import glob

source_dir = "./datasets"
dest_dir = "./data/predictions"

os.makedirs(dest_dir, exist_ok=True)
# get tar files by regex
tar_files = glob.glob(os.path.join(source_dir, "*.tar.gz"))

if not tar_files:
    print("no dataset files fonud, check if you've downloaded the repo properly")
else:

    for tar_path in tar_files:
        tar_name = os.path.basename(tar_path)
        try:
            with tarfile.open(tar_path, "r:gz") as tar:
                tar.extractall(path=dest_dir)
        except Exception as e:
            print(f"error extracting {tar_name}: {e}")
print("done")
