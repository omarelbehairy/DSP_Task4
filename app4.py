import cv2
import numpy as np
from matplotlib import pyplot as plt
import streamlit as st
from PIL import ImageTk, Image


fig1, (ax1, ax2) = plt.subplots(1, 2, figsize=(5,3))


def modes_for_the_image(img):
    # Perform the FFT
    f = np.fft.fft2(img)

    # Shift the zero-frequency component to the center of the spectrum
    fshift = np.fft.fftshift(f)

    # Calculate the magnitude spectrum (in dB to enhance the contrast)
    magnitude_spectrum = 20*np.log(np.abs(fshift))

    #calculate phase spectrum
    phase_spectrum = np.angle(fshift)

    # Convert magnitude and phase images to PIL compatible format    
    magnitude_spectrum = Image.fromarray(magnitude_spectrum.astype('uint8'))
    phase_spectrum = Image.fromarray(phase_spectrum.astype('uint8'))

    return magnitude_spectrum,phase_spectrum


    # Display images in tkinter window
    #mag_photo = ImageTk.PhotoImage(magnitude_spectrum)
    #mag_label.config(image=mag_photo)
    #mag_label.image = mag_photo
    #phase_photo = ImageTk.PhotoImage(phase_spectrum)
    #phase_label.config(image=phase_photo)
    #phase_label.image = phase_photo


    #ax1 = plt.subplot(1,2,1)
    #ax1.imshow(img, cmap='gray')

    #ax2 = plt.subplot(1,2,2)
    #ax2.imshow(phase_spectrum, cmap='gray')

    #plt.show()

    # Display the result
    #plt.subplot(121),plt.imshow(img, cmap = 'gray')
    #plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    #plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
    #plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    #plt.show()

#show_Ftmagnitude_and_phase = tk.Button(root, text="show result", command=extract_fourier_characteristics)
#select_button.pack()

# Start the main event loop to display the window
#root.mainloop()
