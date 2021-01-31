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
    f.extractall(unzip_loc)


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
