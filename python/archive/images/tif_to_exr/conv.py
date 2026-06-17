from PIL import Image
import numpy

im = Image.open('/home/elenaberry/Downloads/10m_-88.54_43.82.tif')
imarray = numpy.array(im)
imarray.astype('int16').tofile("image.raw")