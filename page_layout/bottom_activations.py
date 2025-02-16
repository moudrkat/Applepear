import src
import matplotlib.pyplot as plt
import tensorflow as tf
from PIL import Image
import streamlit as st

def bottom_activations(model, img_array):
    st.write("Hello! I'm a convolutional neural network, trained to recognize apples and pears. I’m pretty good at it, if I do say so myself.")
    st.write(" Am I smart? I’ve been trained on over 570.000 apple sketches and nearly 470.000 pear sketches. How many sketch examples would YOU need to see to tell apples and pears apart? 10? 5? 1?")
    st.write('Apples and pears are pretty much all I know. So, if you draw anything else, I’ll tell you at least if it’s more apple-like (let’s call that "applish" just for fun) or more pear-like ("pearish").')
    st.write('But what exactly do "applish" and "pearish" mean? Let’s take a look at your image through my eyes and I’ll show you how I see it.')
    st.write("The heatmap highlights the parts of the image that matter most to me when making my decision. If I recognize your drawing as an apple, the bright areas show the most 'applish' parts of the picture. If I claim it's a pear, the bright areas highlight the most 'pearish' parts.")
    st.write("(Sometimes the whole surface of the picture is equally important, especially in the case of large and symmetric apples.)")
    # Convert the image to a TensorFlow tensor
    img_tensor = tf.convert_to_tensor(img_array, dtype=tf.float32)

    # Compute Grad-CAM heatmap
    heatmap = src.grad_cam(model, img_tensor, layer_name='conv2d_2')  # last conv layer

    # Convert the input image tensor to a numpy array for plotting
    img = img_tensor[0].numpy()

    # Plot the result with the heatmap overlaid
    plothtmp = src.plot_grad_cam(img, heatmap)
    st.image(plothtmp,width=192)
    st.write('Why are broad regions highlighted instead of just the parts of the lines in the sketch? Let me show you how I process the image to explain:')
    
    # Define a new model that outputs the activations of each layer
    layer_outputs = [layer.output for layer in model.layers]
    activation_model = tf.keras.models.Model(inputs=model.input, outputs=layer_outputs)

    # Get the activations of all layers
    activations = activation_model.predict(img_array)
    
    # Visualize activations for each layer in Streamlit
    st.write("I don’t see a sketch—I see an array of numbers between 0 and 1 (grayscale pixels). My algorithm goes through several steps (layers) to detect key patterns (features), which I’ve been trained to examine. Let me show you exactly how I process your sketch at each layer.")
    src.visualise_activations(activations,activation_model)