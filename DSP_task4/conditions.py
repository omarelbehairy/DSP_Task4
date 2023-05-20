import streamlit as st
import cv2 
import numpy as np

st.title('Counter Example')

# Streamlit runs from top to bottom on every iteraction so
# we check if `count` has already been initialized in st.session_state.

# If no, then initialize count to 0
# If count is already initialized, don't do anything
if 'count' not in st.session_state:
	st.session_state.count = 0

# Create a button which will increment the counter
increment = st.button('Increment')
if increment:
    st.session_state.count += 1

# A button to decrement the counter
decrement = st.button('Decrement')
if decrement:
    st.session_state.count -= 1

st.write('Count = ', st.session_state.count)

uploaded_file = st.file_uploader("Choose an image2 file",type=['jpg','jpeg','png'])
if uploaded_file is not None:
    # Read the image using OpenCV
    image = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), 1)
    # Display the image using Streamlit
    st.image(image, channels="BGR") 

    if 'image' not in st.session_state:
        st.session_state.image = image

    if 'image2' not in st.session_state:
        st.session_state.image2 = st.session_state.image


    
    left_column,right_column = st.columns(2)
    with left_column:
        st.image(st.session_state.image)
        #st.session_state.image = image
    #with right_column:    
    #    st.image(st.session_state.image2) 
    #    st.session_state.image2 = image
