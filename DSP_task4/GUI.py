import streamlit as st
import matplotlib.pyplot as plt
import app4 as ap
from PIL import Image
import cv2
import logging
import numpy as np


def _1st_container_comp():
    left_column, right_column = st.columns(2)
    with left_column:
        uploaded_file = st.file_uploader("Choose an image file",type=['jpg','jpeg','png'])
        logger.info('Processing image...')

    with right_column:
        option = st.selectbox("choose the desired image transformation",('FT Magnitude','FT Phase','FT Real','FT Imaginary'))
    #x,y = ap.modes_for_the_image(uploaded_file)
    #st.write (x,y)
    if uploaded_file is not None:
        file_size1 = uploaded_file.size

        if 'image1' not in st.session_state:
            st.session_state['image1'] = Image.open(uploaded_file.name)

        image1 = Image.open(uploaded_file.name)
        image1 = image1.convert('L')  # convert to grayscale
        image1 = np.array(image1)#        imglist[0]=image1
        #imglist.append(image1)
        #updatedimage = image.resize((200,200))
        #st.image(updatedimage, caption='Uploaded Image')
        x,y,real,imagi = ap.modes_for_the_image(image1)
        #st.write(x,y)

        # Display the result
        ax1 = plt.subplot(1,2,1)
        ax1.imshow(image1, cmap='gray')    
        ax1.set_title('Input Image')
        ax1.axis('off')

        fig1, (ax1, ax2) = plt.subplots(1, 2, figsize=(5,3))
        ax1 = plt.subplot(1,2,1)
        fig1.tight_layout()
        ax1.imshow(image1, cmap='gray')    
        ax1.set_title('Input Image')
        ax1.axis('off')

        ax2 = plt.subplot(1,2,2)
        if option == "FT Magnitude":
            ax2.imshow(x, cmap='gray')
            ax2.set_title('Magnitude Spectrum')
        elif option == "FT Phase":
            ax2.imshow(y, cmap='gray')
            ax2.set_title('Phase Spectrum')
        elif option == "FT Real":
            ax2.imshow(real, cmap='gray')
            ax2.set_title('real spectrum')
        elif option == "FT Imaginary":
            ax2.imshow(imagi, cmap='gray')
            ax2.set_title('imaginary Spectrum')
        ax2.axis('off')

        st.pyplot(fig1)
        return image1


def _2nd_container_comp():
    left_column, right_column = st.columns(2)
    with left_column:
        uploaded_file = st.file_uploader("Choose an Img file")
        logger.info('Processing image...')

    with right_column:
        option = st.selectbox("choose the desired image transformtion",('FT Magnitude','FT Phase','FT Real','FT Imaginary'))
    #x,y = ap.modes_for_the_image(uploaded_file)
    #st.write (x,y)
    if uploaded_file is not None:
        file_size2 = uploaded_file.size

        image2 = Image.open(uploaded_file.name)
        image2 = image2.convert('L')  # convert to grayscale
        image2 = np.array(image2)
        #imglist[1]=image2
        #updatedimage = image.resize((200,200))
        #st.image(updatedimage, caption='Uploaded Image')
        x,y,real,imagi = ap.modes_for_the_image(image2)
        #st.write(x,y)

        # Display the result
        fig2, (ax12, ax22) = plt.subplots(1, 2, figsize=(5,3))
        ax12 = plt.subplot(1,2,1)
        fig2.tight_layout()
        ax12.imshow(image2, cmap='gray')    
        ax12.set_title('Input Image')
        ax12.axis('off')
        ax22 = plt.subplot(1,2,2)

        if option == "FT Magnitude":
            ax22.imshow(x, cmap='gray')
            ax22.set_title('Magnitude Spectrum')
        elif option == "FT Phase":
            ax22.imshow(y, cmap='gray')
            ax22.set_title('Phase Spectrum')
        elif option == "FT Real":
            ax22.imshow(real, cmap='gray')
            ax22.set_title('real spectrum')
        elif option == "FT Imaginary":
            ax22.imshow(imagi, cmap='gray')
            ax22.set_title('imaginary Spectrum')
        ax22.axis('off')

        st.pyplot(fig2)
        return image2




mixlist = []
#imglist = []

logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)

logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)

# create file handler and set level to debug
file_handler = logging.FileHandler('my_logs.txt')
file_handler.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# add formatter to file handler
file_handler.setFormatter(formatter)

# add file handler to logger
logger.addHandler(file_handler)


#page layout
st.set_page_config(layout="wide")
fig1, (ax1, ax2) = plt.subplots(1, 2, figsize=(5,3))
fig1.tight_layout()


#importing style css.file
with open("file.css") as fl:
    st.markdown(f"<style>{fl.read()}</style>", unsafe_allow_html = True)

incubator_container =st.container()
#customizing the layout
left_column, right_column = st.columns(2)
with left_column:
    first_img_container_left  = st.container()
    second_img_container_left = st.container()

with right_column:
    mixer_component = st.container()
    result_img_container_right = st.container()


with incubator_container:
    #imglist=[]

    #first container to get image
    with first_img_container_left:
        image1=_1st_container_comp()


        #second container to get image
        with second_img_container_left:
            image2=_2nd_container_comp()
                #if file_size1 != file_size2:
                #    logger.error('Error the two image not same size')
        
        
        #st.write(image1,image2,mixed_image)
        #third container to get image and customize output
        #output_option,comp1,comp2,mixrate1,mixrate2=mixerfrontend()
        #third container to get image and customize output
        
        with mixer_component:
            output_option=st.selectbox("mixer output to",('output1','output2'))
            left_column, right_column = st.columns(2)
            with left_column:
                comp1=st.selectbox("component1",('img1','img2'))
            with right_column:
                mixrate1=st.slider("output1",0,100,0)
                #mixlist.append(mixrate1)
            mix_comp1=st.selectbox("Mag,phase,real,imaginary,uniphase,uniMag",('Mag','phase','real','imaginary','uniphase','uniMag'))
            st.selectbox("options",('mag1','phase1','Real1','imag1'))
            left_column1, right_column1 = st.columns(2)
            with left_column1:
                comp2=st.selectbox("component2",('img1','img2'))
            with right_column1:
                mixrate2=st.slider("output2",0,100,0)
                #mixlist.append(mixrate2)
            mix_comp2=st.selectbox("2Mag,phase,real,imaginary,uniphase,uniMag",('Mag','phase','real','imaginary','uniphase','uniMag'))
            st.selectbox("options2",('mag2','phase2','Real2','imag2'))    
        
        mixed_image=ap.mix_photos(image1,image2,mixrate1,mixrate2,mix_comp1,mix_comp2)
        #st.write(image1,image2,mixed_image)

        with result_img_container_right:
            left_column, right_column = st.columns(2)
            #if output_option == 'output1':
                # Resize the images to have the same shape
                #image_mix = cv2.resize(image1, (200, 200))
                #image_mix =ap.mix_photos(image1,image2,mixlist[0],mixlist[1])
                #left_column=st.image(mixed_image)
            #else:
                # Resize the images to have the same shape
                #image2 = cv2.resize(image2, (200, 200))
                #resultant_image_op2=ap.mix_photos(image2,image2,mixlist[0],mixlist[1])
                #right_column=st.image(mixed_image)
            st.image(mixed_image)
    

    #st.write(imglist)
    #st.write(imglist[0])
    #st.write(imglist[1])

    #image1 = np.array(image1)

    

