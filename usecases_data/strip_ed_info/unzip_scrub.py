import shutil
from glob import glob
import re
import tarfile
import uuid
from pathlib import Path


black_list = Path('blacklist.csv')
ed_zip = '/Users/wayne.lee/Downloads/HW1.tar.xz'
zip_folder = re.sub('.*/(.*).tar.*', '\\1', ed_zip)
unzip_loc = './'

black_list_ids = []
with black_list.open('r') as f:
    for l in f.readlines():
        black_list_ids.append(l.strip())

with Path('namespace_seed.csv').open('r') as f:
    seed = f.readlines()[0]
    namespace = uuid.uuid3(uuid.NAMESPACE_DNS, seed)

with tarfile.open(ed_zip) as f:
    
    import os
    
    def is_within_directory(directory, target):
        
        abs_directory = os.path.abspath(directory)
        abs_target = os.path.abspath(target)
    
        prefix = os.path.commonprefix([abs_directory, abs_target])
        
        return prefix == abs_directory
    
    def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
    
        for member in tar.getmembers():
            member_path = os.path.join(path, member.name)
            if not is_within_directory(path, member_path):
                raise Exception("Attempted Path Traversal in Tar File")
    
        tar.extractall(path, members, numeric_owner=numeric_owner) 
        
    
    safe_extract(f, unzip_loc)


slides = glob('{}/*'.format(zip_folder))
for slide in slides:
    submissions = glob('{}/*'.format(slide))
    for submission in submissions:
        uni_email = re.sub(r'.*/(.*@[^\.]*\.[^ ]*) .*', '\\1', submission)
        uni = re.sub('([^@]*)@.*', '\\1', uni_email)
        if not uni_email:
            continue
        if uni in black_list_ids:
            shutil.rmtree(Path(submission))
            continue
        assigned_uuid = uuid.uuid3(namespace, uni_email)
        # The formatting must happen after sub() or when uuids start with
        # a number, then it'll conflict with group referencing
        new_name = re.sub(r'(.*/)(.*@[^\.]*\.[^ ]*)( .*)',
                          '\\1{}\\3', submission).format(assigned_uuid)
        Path(submission).rename(new_name)


with tarfile.open('{}_scrubbed.tar.gz'.format(zip_folder), 'w:gz') as tar:
    tar.add(zip_folder)
