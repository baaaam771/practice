import numpy as np

from skimage import io, draw


imageNDArray = np.zeros((100, 100), dtype=np.uint8)

xNDArray = np.array([10, 60, 40, 10])

yNDArray = np.array([10, 25, 80, 50])

x, y = draw.polygon(yNDArray, xNDArray)

imageNDArray[x, y] = 1

io.imshow(imageNDArray)

io.show()
