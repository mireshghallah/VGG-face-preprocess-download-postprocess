# VGG-face-preprocess-download-postprocess
Acquire vgg-face dataset completely, with pre and post processing.

## vgg-face
# Step 1:
Acquire VGG-Face-Dataset:
Download and unzip from website 
http://www.robots.ox.ac.uk/~vgg/data/vgg_face/

# Step 2:
Unzipe: 
tar -xvf vgg_face_dataset.tar.gz vgg_face_dataset/

Then run (python2) 
https://github.com/pby5/vgg_face_dataset_download, or equivalent from this repo (I have modified the size of the images to 224X224 to easily feed the photos to vgg-16 and set the data descriptor address to the files drectory of the vgg_face dataset. 

# Step 3:
Then run 
python delete.py
to delete the corrupted images. 

*To move the photos when they are downloaded to another server, run: 

rsync -avz -r files/ name@server.ucsd.edu:/home/niloofar/

# Step 4:
These images are all in png, and it will be hard for dataloaders to load them and for ML frameworks to use them, since the files are large and consume a lot of memory. To remedy this, run the:

convert_delete.py

to compress dataset and change png to jpg. It also changes the directory formation to match to PyTorch DataLoaders.


