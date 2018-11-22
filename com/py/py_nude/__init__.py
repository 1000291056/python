import os
from nude import Nude


IMAGE_ROOT = ROOT = r"D:\project\ffw\python\\img"
for file_name in os.listdir(IMAGE_ROOT):
    file_path = os.path.join(IMAGE_ROOT, file_name)
    if os.path.isdir(file_path):
        continue
    n = Nude(file_path)
    n.parse()
    print(n.result, n.message)