import streamlit as st 
from dotenv import load_dotenv
import os 
import openai
from diffusers import StableDiffusionPipeline
import torch

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

#function to generate AI based images using OpenAI Dall-E
def generate_images_using_openai(text):
    response = openai.Image.create(prompt= text, n=1, size="512x512")
    image_url = response['data'][0]['url']
    return image_url


#function to generate AI based images using Huggingface Diffusers
def generate_images_using_huggingface_diffusers(text):
    pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16)
    pipe = pipe.to("cuda")
    prompt = text
    image = pipe(prompt).images[0] 
    return image

st.subheader("Φαντάσου ο")
option1 = st.selectbox('Character',('R2-D2', 'C-3PO', 'Bubmblebee', 'ET', 'Darth Vader', 'Alien'))
st.subheader("να:")
option2 = st.selectbox('Doing what?',('Dancin tango', 'laying on the beach', 'swimming', 'with a stylish hat'))
final_opt = (option1, ' ', option2)
input_prompt = 
if input_prompt is not None:
    if st.button("Generate Image"):
        image_output = generate_images_using_huggingface_diffusers(input_prompt)
        st.info("Generating image.....")
        st.success("Image Generated Successfully")
        st.image(image_output, caption="Generated by Huggingface Diffusers")
