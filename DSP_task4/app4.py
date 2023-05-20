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
    
    magnitude_spectrum=(255*magnitude_spectrum-np.min(magnitude_spectrum)/np.max(magnitude_spectrum)-np.min(magnitude_spectrum))

    #calculate phase spectrum
    phase_spectrum = np.angle(fshift)
    
    # Calculate the real and imaginary spectra
    real_spectrum = np.real(fshift)
    imaginary_spectrum = np.imag(fshift)


    # Convert magnitude and phase images to PIL compatible format    
    #magnitude_spectrum = Image.fromarray(magnitude_spectrum.astype('uint8'))
    phase_spectrum = Image.fromarray(phase_spectrum.astype('uint8'))
    real_spectrum = Image.fromarray(real_spectrum.astype('uint8'))
    imaginary_spectrum = Image.fromarray(imaginary_spectrum.astype('uint8'))

    return magnitude_spectrum, phase_spectrum, real_spectrum, imaginary_spectrum



def produce_mix(image1,image2):
    image1_fft = np.fft.fft2(image1)
    image2_fft = np.fft.fft2(image2)

    image1_fft_shift = np.fft.fftshift(image1_fft)
    image2_fft_shift = np.fft.fftshift(image2_fft)

    image1_real = np.real(image1_fft)
    image1_imaginary = np.imag(image1_fft)

    image2_real = np.real(image2_fft)
    image2_imaginary = np.imag(image2_fft)

    magnitude1 = np.abs(image1_fft)
    magnitude_shift1 = 20*np.log(np.abs(image1_fft_shift))

    magnitude2 = np.abs(image2_fft)
    magnitude_shift2 = 20*np.log(np.abs(image2_fft_shift))

    phase1 = np.angle(image1_fft)
    phase_shift1 = np.angle(image1_fft_shift)

    phase2 = np.angle(image2_fft)
    phase_shift2 = np.angle(image2_fft_shift)

    uniform_magnitude1 = np.ones(magnitude1.shape)
    uniform_phase1 = np.zeros(phase1.shape)
    
    uniform_magnitude2 = np.ones(magnitude2.shape)
    uniform_phase2 = np.zeros(phase2.shape)

    #st.write(uniform_magnitude2)
    return image1_fft,image2_fft,image1_fft_shift,image2_fft_shift,image1_real,image1_imaginary,image2_real,image2_imaginary,magnitude1,magnitude_shift1,magnitude2,magnitude_shift2,phase1,phase_shift1,phase2,phase_shift2,uniform_magnitude1,uniform_phase1,uniform_magnitude2,uniform_phase2 


def Mag_phase_Mix(mixing_ratio1,mixing_ratio2,magnitude1,magnitude2,phase1,phase2):
    mag_mix = magnitude1*(mixing_ratio1/100)+magnitude2*(1-(mixing_ratio1/100))
    phase_mix = phase1*(1-(mixing_ratio2/100))+phase2*(mixing_ratio2/100)

    combined_total = np.multiply(mag_mix, np.exp(1j * phase_mix))
    
    return np.real(np.fft.ifft2(combined_total))

def real_imaginary(mixing_ratio1,mixing_ratio2,image1_real,image2_real,image1_imaginary,image2_imaginary):
    mixed_real = image1_real * (mixing_ratio1 / 100) + image2_real * (1 - mixing_ratio1 / 100)
    mixed_imaginary = image2_imaginary * (mixing_ratio2 / 100) + image1_imaginary * (1 - mixing_ratio2 / 100)

    mixed_fft = mixed_real + 1j * mixed_imaginary
    
    return np.fft.ifft2(mixed_fft).real.astype(np.uint8)


def mix_photos(image1, image2, mixing_ratio1,mixing_ratio2,comp1,comp2):
    
    #st.write(image1,image2)
    image1_fft,image2_fft,image1_fft_shift,image2_fft_shift,image1_real,image1_imaginary,image2_real,image2_imaginary,magnitude1,magnitude_shift1,magnitude2,magnitude_shift2,phase1,phase_shift1,phase2,phase_shift2,uniform_magnitude1,uniform_phase1,uniform_magnitude2,uniform_phase2 = produce_mix(image1,image2)
    #st.write(image1_real,image2_real)
    if((comp1 == 'real' or comp1 == 'imaginary') and (comp2 == 'real' or comp2 == 'imaginary')):

        #mixreal=image1_real*mixing_ratio1/100+image2_real*mixing_ratio2/100
        #miximaginary=image1_imaginary*mixing_ratio1/100+image2_imaginary*mixing_ratio2/100
        #combined = mixreal + miximaginary * 1j
        #mixed_image = np.real(np.fft.ifft2(combined))
        mixed_image = real_imaginary(mixing_ratio1,mixing_ratio2,image1_real,image2_real,image1_imaginary,image2_imaginary)

    elif((comp1 == 'Mag' or comp1 == 'phase' ) and ( comp2 == 'phase' or comp2 =='Mag')):
        mixed_image = Mag_phase_Mix(mixing_ratio1,mixing_ratio2,magnitude1,magnitude2,phase1,phase2)
    # elif((comp1 == 'phase' ) and ( comp2 == 'Mag')):
    #     # mag_mix = magnitude2*(mixing_ratio1/100)+magnitude1*(1-(mixing_ratio1/100))
    #     # phase_mix = phase2*(1-(mixing_ratio2/100))+phase1*(mixing_ratio2/100)

    #     # combined_total = np.multiply(mag_mix, np.exp(1j * phase_mix))
    #     # mixed_image = np.real(np.fft.ifft2(combined_total))
    #     mag_mix = magnitude2*(mixing_ratio2/100)+magnitude1*(1-(mixing_ratio2/100))
    #     phase_mix = phase1*((mixing_ratio1/100))+phase2*(1-(mixing_ratio1/100))

    #     combined_total = np.multiply(mag_mix, np.exp(1j * phase_mix))
    #     mixed_image = np.real(np.fft.ifft2(combined_total))
    
    elif((comp1 == 'uniphase'  ) and ( comp2 == 'Mag' )):
        mag_mix = magnitude2*(mixing_ratio2/100)+magnitude1*(1-(mixing_ratio2/100))
        phase_mix = uniform_phase1*(mixing_ratio1/100)+phase2*(1-(mixing_ratio1/100))

        combined_total = np.multiply(mag_mix, np.exp(1j * phase_mix))
        mixed_image = np.real(np.fft.ifft2(combined_total))

    elif((comp1 == 'Mag'  ) and ( comp2 == 'uniphase' )):
        mag_mix=magnitude1*(mixing_ratio1/100)+magnitude2*(1-(mixing_ratio1/100))
        phase_mix =uniform_phase2*(mixing_ratio2/100)+phase1*(1-(mixing_ratio2/100))
    
        combined_total = np.multiply(mag_mix, np.exp(1j * phase_mix))
        mixed_image = np.real(np.fft.ifft2(combined_total))

    elif(comp1 == 'uniMag' and comp2 == 'phase' ) :
        mag_mix = uniform_magnitude1*(mixing_ratio1/100)+uniform_magnitude2*(1-(mixing_ratio1/100))
        phase_mix = phase2*(mixing_ratio2/100)+phase1*(1-(mixing_ratio2/100))

        combined_total = np.multiply(mag_mix, np.exp(1j * phase_mix))
        mixed_image = np.real(np.fft.ifft2(combined_total))

    elif(comp1 == 'phase' and comp2 == 'uniMag' ) :

        mag_mix = uniform_magnitude2*(mixing_ratio2/100)+uniform_magnitude1*(1-(mixing_ratio2/100))
        phase_mix = phase1*(mixing_ratio1/100)+phase2*(1-(mixing_ratio1/100))

        combined_total = np.multiply(mag_mix, np.exp(1j * phase_mix))
        mixed_image = np.real(np.fft.ifft2(combined_total))

        # phase_mix = phase1*(mixing_ratio1/100)+phase2*(1-(mixing_ratio1/100))
        # mag_mix = uniform_magnitude2*(mixing_ratio2/100)+magnitude1*(1-(mixing_ratio2/100))

        # combined_total = np.multiply(mag_mix, np.exp(1j * phase_mix))
        # mixed_image = np.real(np.fft.ifft2(combined_total))
    else:
        return
    #t.write(phase1,phase2)
    mixed_image = (mixed_image - np.min(mixed_image)) / (np.max(mixed_image) - np.min(mixed_image))

    return abs(mixed_image)




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
