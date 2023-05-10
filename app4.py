import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image
img = cv2.imread('367244e514bb9ab1e0034fbb0660b555.jpg', cv2.IMREAD_GRAYSCALE)

# Perform the FFT
f = np.fft.fft2(img)

# Shift the zero-frequency component to the center of the spectrum
fshift = np.fft.fftshift(f)

# Calculate the magnitude spectrum (in dB to enhance the contrast)
magnitude_spectrum = 20*np.log(np.abs(fshift))

#calculate phase spectrum
phase_spectrum = np.angle(fshift)

ax1 = plt.subplot(1,2,1)
ax1.imshow(img, cmap='gray')

ax2 = plt.subplot(1,2,2)
ax2.imshow(phase_spectrum, cmap='gray')

plt.show()

# Display the result
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()


