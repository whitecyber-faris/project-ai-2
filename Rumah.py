import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle
from skimage import transform
from skimage.io import imread, imshow

house = imread('artsy_house.png')
plt.figure(num=None, figsize=(8, 6), dpi=80)


points_of_interest =[[105, 60], 
                     [260, 85], 
                     [275, 295], 
                     [110, 290]]
projection = [[100, 75],
              [275, 75],
              [275, 290],
              [100, 290]]
color = 'green'
patches = []
fig, ax = plt.subplots(1,2, figsize=(15, 10), dpi = 80)
for coordinates in (points_of_interest + projection):
    patch = Circle((coordinates[0],coordinates[1]), 10, 
                    facecolor = color)
    patches.append(patch)
for p in patches[:4]:
    ax[0].add_patch(p)
ax[0].imshow(house);
for p in patches[4:]:
    ax[1].add_patch(p)
ax[1].imshow(np.ones((house.shape[0], house.shape[1])));


points_of_interest = np.array(points_of_interest)
projection = np.array(projection)
tform = transform.estimate_transform('projective', points_of_interest, projection)
tf_img_warp = transform.warp(house, tform.inverse, mode = 'edge')
plt.figure(num=None, figsize=(8, 6), dpi=80)
fig, ax = plt.subplots(1,2, figsize=(15, 10), dpi = 80)
ax[0].set_title(f'Original', fontsize = 15)
ax[0].imshow(house)
ax[0].set_axis_off();
ax[1].set_title(f'Transformed', fontsize = 15)
ax[1].imshow(tf_img_warp)
ax[1].set_axis_off();