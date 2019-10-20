import os

for parent, dirnames, filenames in os.walk('/home/niloofar/VGG-Face'):
    for fn in filenames:
        if fn.lower().endswith('.err'):
            os.remove(os.path.join(parent, fn))
