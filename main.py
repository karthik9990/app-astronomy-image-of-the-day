import streamlit as st
import requests


api_key = "oE4BnvtmCcuiFXQ824U9R3sfDBsduTckqXbKX8Na"
url = ("https://api.nasa.gov/planetary/apod?"
       f"api_key={api_key}")


response1 = requests.get(url)
content = response1.json()

# print(content)

title = content["title"]
image_url = content["url"]
explanation = content["explanation"]

image_filepath = "img.png"
response2 = requests.get(image_url)
with open(image_filepath, 'wb') as file:
    file.write(response2.content)

st.title(title)
st.image(image_filepath)
st.write(explanation)