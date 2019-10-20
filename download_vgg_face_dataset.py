#Download the VGG face dataset from URLs given by http://www.robots.ox.ac.uk/~vgg/data/vgg_face/vgg_face_dataset.tar.gz
from scipy import misc
import numpy as np
from skimage import io
import time
import os
import socket
from urllib2 import HTTPError, URLError
from httplib import HTTPException

def main():
  socket.setdefaulttimeout(30)
  datasetDescriptor = '/home/niloofar/vgg_face_dataset_download/files'
  #resultPath = '/home/gavinpan/workspace/dataset/vgg_face_dataset/imgs'
  textFileNames = os.listdir(datasetDescriptor)
  person = 0
  for textFileName in textFileNames:
    if textFileName.endswith('.txt'):
      person += 1
      with open(os.path.join(datasetDescriptor, textFileName), 'rt') as f:
        lines = f.readlines()
      dirName = textFileName.split('.')[0]
      classPath = os.path.join(datasetDescriptor, dirName)
      if not os.path.exists(classPath):
        os.makedirs(classPath)
      else:
        files = os.listdir(classPath)
        if len(files) == 1000:
          #print "imgs of %s download end" % classPath

          if person % 1 == 0:
            print("download finish {}".format(float(person)/2622))
            
          continue
        else:
          pass
        #time.sleep(100)
      for line in lines:
        x = line.split(' ')
        fileName = x[0]
        url = x[1]
        box = np.rint(np.array(map(float, x[2:6])))  # x1,y1,x2,y2
        imagePath = os.path.join(datasetDescriptor, dirName, fileName+'.png')
        errorPath = os.path.join(datasetDescriptor, dirName, fileName+'.err')
        if not os.path.exists(imagePath) and not os.path.exists(errorPath):
          try:
              print (url)
              img = io.imread(url)
            
          except (HTTPException, HTTPError, URLError, IOError, ValueError, IndexError, OSError) as e:
            errorMessage = '{}: {}'.format(url, e)
            saveErrorMessageFile(errorPath, errorMessage)
          else:
            try:
              #if image is gray and then translate to rgb
              if img.ndim == 2:
                img = toRgb(img)
              if img.ndim != 3:
                raise ValueError('Wrong number of image dimensions')
              hist = np.histogram(img, 255, density=True)
              if hist[0][0]>0.9 and hist[0][254]>0.9:
                raise ValueError('Image is mainly black or white')
              else:
                print(box[1], "box")
                box = box.astype(np.int64)
                # Crop image according to dataset descriptor
                imgCropped = img[box[1]:box[3],box[0]:box[2],:]
                # Scale to 256x256
                imgResized = misc.imresize(imgCropped, (224,224))
                # Save image as .png
                misc.imsave(imagePath, imgResized)
            except ValueError as e:
              errorMessage = '{}: {}'.format(url, e)
              saveErrorMessageFile(errorPath, errorMessage)
            
def saveErrorMessageFile(fileName, errorMessage):
  #print(errorMessage)
  with open(fileName, "w") as textFile:
    textFile.write(errorMessage)
          
def toRgb(img):
  w, h = img.shape
  ret = np.empty((w, h, 3), dtype=np.uint8)
  ret[:, :, 0] = ret[:, :, 1] = ret[:, :, 2] = img
  return ret
  
if __name__ == '__main__':
  main()
