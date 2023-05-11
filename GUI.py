import streamlit as st
import matplotlib.pyplot as plt
import app4 as ap
from PIL import Image
import cv2

#page layout
st.set_page_config(layout="wide")
fig1, (ax1, ax2) = plt.subplots(1, 2, figsize=(5,3))

#importing style css.file
with open("file.css") as fl:
    st.markdown(f"<style>{fl.read()}</style>", unsafe_allow_html = True)

#customizing the layout
left_column, right_column = st.columns(2)
with left_column:
    first_img_container_left  = st.container()
    second_img_container_left = st.container()

with left_column:
    mixer_component = st.container()
    result_img_container_right = st.container()
    
with first_img_container_left:
    left_column, right_column = st.columns(2)
    with left_column:
        uploaded_file = st.file_uploader("Choose an image file")
    with right_column:
        option = st.selectbox("choose the desired image transformation",('FT Magnitude','FT Phase','FT Real','FT Imaginary'))
    #x,y = ap.modes_for_the_image(uploaded_file)
    #st.write (x,y)
    if uploaded_file is not None:
        image = cv2.imread(uploaded_file.name,cv2.IMREAD_GRAYSCALE)
        #updatedimage = image.resize((200,200))
        #st.image(updatedimage, caption='Uploaded Image')
        x,y = ap.modes_for_the_image(image)
        #st.write(x,y)

        # Display the result
        #ax1 = plt.subplot(1,2,1)
        ax1.imshow(image, cmap='gray')    
        ax1.set_title('Input Image')
        ax1.axis('off')

        if option == "FT Magnitude":
            ax2.imshow(x, cmap='gray')
            ax2.set_title('Magnitude Spectrum')
        elif option == "FT Phase":
            ax2.imshow(y, cmap='gray')
            ax2.set_title('Phase Spectrum')
        ax2.axis('off')

        st.pyplot(fig1)


with second_img_container_left:
    left_column, right_column = st.columns(2)
    with left_column:
        uploaded_file = st.file_uploader("Choose an Img file")
    with right_column:
        option = st.selectbox("choose the desired image transformtion",('FT Magnitude','FT Phase','FT Real','FT Imaginary'))
    #x,y = ap.modes_for_the_image(uploaded_file)
    #st.write (x,y)
    if uploaded_file is not None:
        image = cv2.imread(uploaded_file.name,cv2.IMREAD_GRAYSCALE)
        #updatedimage = image.resize((200,200))
        #st.image(updatedimage, caption='Uploaded Image')
        x,y = ap.modes_for_the_image(image)
        #st.write(x,y)

        # Display the result
        #ax1 = plt.subplot(1,2,1)
        ax1.imshow(image, cmap='gray')    
        ax1.set_title('Input Image')
        ax1.axis('off')

        if option == "FT Magnitude":
            ax2.imshow(x, cmap='gray')
            ax2.set_title('Magnitude Spectrum')
        elif option == "FT Phase":
            ax2.imshow(y, cmap='gray')
            ax2.set_title('Phase Spectrum')
        ax2.axis('off')

        st.pyplot(fig1)
    


        
        
