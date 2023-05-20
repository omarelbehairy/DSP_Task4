import streamlit as st
import matplotlib.pyplot as plt
import app4 as ap
from PIL import Image
import cv2
import logging
import numpy as np


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

target_size = (500, 500)

# customizing the layout
st.set_page_config(

    layout="wide",
)

flag = 0
left_column, right_column = st.columns(2)
with left_column:
    first_img_container_left = st.container()
    second_img_container_left = st.container()

with right_column:
    mixer_component = st.container()
    result_img_container_right = st.container()

with first_img_container_left:
    left_column, right_column = st.columns(2)
    with left_column:
        uploaded_file1 = st.sidebar.file_uploader(
            "Choose an image1 file", type=['jpg', 'jpeg', 'png'])
        st.write("<p style='font-size:40px; text-align: center;'><b>Image 1</b></p>",
                 unsafe_allow_html=True)

        logger.info('Uploading image 1...')

    with right_column:
        option1 = st.selectbox("choose the desired image1 transformtion",
                               ('FT Magnitude', 'FT Phase', 'FT Real', 'FT Imaginary'))

with second_img_container_left:
    left_column, right_column = st.columns(2)
    with left_column:
        uploaded_file2 = st.sidebar.file_uploader(
            "Choose an image2 file", type=['jpg', 'jpeg', 'png'])
        st.write("<p style='font-size:40px; text-align: center;'><b>Image 2</b></p>",
                 unsafe_allow_html=True)

        logger.info('Uploading image 2...')

    with right_column:
        option2 = st.selectbox("choose the desired image2 transformtion",
                               ('FT Magnitude', 'FT Phase', 'FT Real', 'FT Imaginary'))

with mixer_component:
    output_option = st.selectbox("mixer output to", ('output1', 'output2'))
    left_column, right_column = st.columns(2)
    with left_column:
        comp1 = st.selectbox("component1", ('img1', 'img2'))
    with right_column:
        mixrate1 = st.slider("output1", 0, 100, 0)
    mix_comp1 = st.selectbox("Mag,phase,real,imaginary,uniphase,uniMag",
                             ('Mag', 'phase', 'real', 'imaginary', 'uniphase', 'uniMag'))
    left_column1, right_column1 = st.columns(2)
    with left_column1:
        comp2 = st.selectbox("component2", ('img1', 'img2'))
    with right_column1:
        mixrate2 = st.slider("output2", 0, 100, 0)
    mix_comp2 = st.selectbox("2Mag,phase,real,imaginary,uniphase,uniMag",
                             ('Mag', 'phase', 'real', 'imaginary', 'uniphase', 'uniMag'))

with result_img_container_right:
    left_column, right_column = st.columns(2)

# importing style css.file
hide_st_style = """ <style> #MainMenu {visibility: hidden;} footer {visibility: hidden;}
header {visibility: hidden;} </style>"""
st.markdown(hide_st_style, unsafe_allow_html=True)
with open("file.css") as fl:
    st.markdown(f"<style>{fl.read()}</style>", unsafe_allow_html=True)

if uploaded_file1 is not None and uploaded_file2 is not None:

    file_size1 = uploaded_file1.size
    file_size2 = uploaded_file2.size

    if file_size1 != file_size2:
        logger.error('Error the two image not same size')
        flag = 1

    class TotalGui:
        def __init__(self):

            self.path1 = uploaded_file1
            self.path2 = uploaded_file2

            self.image1 = Image.open(self.path1)
            self.image1 = self.image1.convert('L')  # convert to grayscale
            self.image1 = np.array(self.image1)

            self.image2 = Image.open(self.path2)
            self.image2 = self.image2.convert('L')  # convert to grayscale
            self.image2 = np.array(self.image2)

            self.magnitudeSpec1, self.phaseSpec1, self.realSpec1, self.imagSpec1 = ap.modes_for_the_image(
                self.image1)
            self.magnitudeSpec2, self.phaseSpec2, self.realSpec2, self.imagSpec2 = ap.modes_for_the_image(
                self.image2)

            if 'tempimage' not in st.session_state:
                st.session_state['tempimage'] = None
            if 'tempimage2' not in st.session_state:
                st.session_state['tempimage2'] = None

            # self.fig1, (self.ax1, self.ax2) = plt.subplots(1, 2, figsize=(5,3))
            # self.fig2, (self.ax12, self.ax22) = plt.subplots(1, 2, figsize=(5,3))

            self.logger = logging.getLogger('my_logger')
            self.logger.setLevel(logging.DEBUG)

            file_handler = logging.FileHandler('my_logs.txt')
            file_handler.setLevel(logging.DEBUG)

            formatter = logging.Formatter(
                '%(asctime)s - %(levelname)s - %(message)s')

            file_handler.setFormatter(formatter)

            self.logger.addHandler(file_handler)

        def selectModes(self):

            fig1, (ax1, ax2) = plt.subplots(1, 2, figsize=(3, 2))
            ax1 = plt.subplot(1, 2, 1)
            ax1.imshow(self.image1, cmap='gray')
            ax1.axis('off')
            ax2 = plt.subplot(1, 2, 2)

            if (option1 == 'FT Magnitude'):
                ax2.imshow(self.magnitudeSpec1, cmap='gray')
            elif (option1 == 'FT Phase'):
                ax2.imshow(self.phaseSpec1, cmap='gray')
            elif (option1 == 'FT Real'):
                ax2.imshow(self.realSpec1, cmap='gray')
            elif (option1 == 'FT Imaginary'):
                ax2.imshow(self.imagSpec1, cmap='gray')
            with first_img_container_left:
                ax2.axis('off')
                fig1.tight_layout()
                st.pyplot(fig1)

            fig2, (ax12, ax22) = plt.subplots(1, 2, figsize=(3, 2))
            ax12 = plt.subplot(1, 2, 1)
            ax12.imshow(self.image2, cmap='gray')
            ax12.axis('off')
            ax22 = plt.subplot(1, 2, 2)

            if (option2 == 'FT Magnitude'):
                ax22.imshow(self.magnitudeSpec2, cmap='gray')
            elif (option2 == 'FT Phase'):
                ax22.imshow(self.phaseSpec2, cmap='gray')
            elif (option2 == 'FT Real'):
                ax22.imshow(self.realSpec2, cmap='gray')
            elif (option2 == 'FT Imaginary'):
                ax22.imshow(self.imagSpec2, cmap='gray')
            with second_img_container_left:
                ax22.axis('off')
                fig2.tight_layout()
                st.pyplot(fig2)

        def drawOP(self, Total_img, output):

            if np.any(Total_img):
                st.image(Total_img, use_column_width=True)

                if output == 'output2':
                    st.session_state.tempimage2 = Total_img
                    if st.session_state.tempimage is not None and st.session_state.tempimage2 is not None: 
                        with left_column:
                            st.image(st.session_state.tempimage)
                if output == 'output1':
                    st.session_state.tempimage = Total_img
                    if st.session_state.tempimage is not None and st.session_state.tempimage2 is not None: 
                        with right_column:
                            st.image(st.session_state.tempimage2)
            else:
                st.write("not valid combination")

        def output(self, output):
            if ((comp1 != comp2) and (comp1 == 'img2')):
                Total_img = ap.mix_photos(
                    self.image2, self.image1, mixrate1, mixrate2, mix_comp1, mix_comp2)
                self.drawOP(Total_img, output)
            elif (comp1 == comp2 == 'img1'):
                Total_img = ap.mix_photos(
                    self.image1, self.image1, mixrate1, mixrate2, mix_comp1, mix_comp2)
                self.drawOP(Total_img, output)
            elif (comp1 == comp2 == 'img2'):
                Total_img = ap.mix_photos(
                    self.image2, self.image2, mixrate1, mixrate2, mix_comp1, mix_comp2)
                self.drawOP(Total_img, output)
            else:
                Total_img = ap.mix_photos(
                    self.image1, self.image2, mixrate1, mixrate2, mix_comp1, mix_comp2)
                self.drawOP(Total_img, output)

        def adjust_output_location(self):
            if output_option == 'output1':
                with result_img_container_right:
                    with left_column:
                        self.output('output1')

            if output_option == 'output2':
                with result_img_container_right:
                    with right_column:
                        self.output('output2')

    result = TotalGui()
    result.selectModes()
    logger.info('Displaying images different spectrum ...')
    result.adjust_output_location()
    logger.info('Mixing images ...')
