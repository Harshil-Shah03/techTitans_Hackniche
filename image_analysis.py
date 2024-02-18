# # import cv2
# # import easyocr
# # import numpy as np
# # import google.generativeai as genai
# # import PIL
# # import os

# # genai.configure(api_key="AIzaSyAMBoESvU1tZn_3U1eWtp_9HRDbVf3XQ5c")
# # reader = easyocr.Reader(['en'], gpu=False, model_storage_directory='C:/Users/harsh/Desktop/models')

# # def ingredientsfetch(image_path):
# #     try:
# #         img = PIL.Image.open(image_path)
# #         model = genai.GenerativeModel('gemini-pro-vision')
# #         prompt = "Extract all the food ingredients from the following text without any special characters or numbers just , as the separator between ingredients"
# #         result = model.generate_content([prompt,img],stream=True)
# #         result.resolve()
# #         # os.remove(image_path)
# #         return {'result': result.text}
# #     except Exception as e:
# #         print(str(e))
# #         return {'error': str(e)}, 500

# # def geminiocr(image_path):
# #     try:
# #         img = PIL.Image.open(image_path)
# #         model = genai.GenerativeModel('gemini-pro-vision')
# #         result = model.generate_content([img,"Extract all the food ingredients from the image without any special characters or numbers just , as the separator between ingredients"],stream=True)
# #         result.resolve()
# #         # os.remove(image_path)
# #         return {'result': result.text}
# #     except Exception as e:
# #         return {'error': str(e)}, 500

# # # Test the functions with an image path
# # print(ingredientsfetch('download.jpg'))
# # print(geminiocr('download.jpg'))


# import google.generativeai as genai
# import PIL

# # Configure the API
# genai.configure(api_key="AIzaSyAMBoESvU1tZn_3U1eWtp_9HRDbVf3XQ5c")

# # Load the model
# model = genai.GenerativeModel('gemini-pro-vision')

# # Open the image
# img = PIL.Image.open('plswork.jpg')

# # Define the prompt
# prompt = "decorate the wall"

# # Generate the content
# result = model.generate_content([prompt, img], stream=True)

# # Resolve the result
# result.resolve()

# # Save the modified image
# print(result.text)
# # result.image.save('output_image.jpg')
import base64
import os
import requests
from PIL import Image

# Convert image to base64
with open("thisiwllwork.jpg", "rb") as img_file:
    img_base64 = base64.b64encode(img_file.read()).decode('utf-8')
with open("plswork.jpg", "rb") as img2_file:
  img2_base64 = base64.b64encode(img2_file.read()).decode('utf-8')

body = {
  "samples": 1,
  "height": 512,
  "width": 512,
#   "height": 1024,
#   "width": 1024,
  "steps": 40,
  "cfg_scale": 5,
  "text_prompts": [
    {
      "text": "what lamps can we place on the table?",
      "weight": 1
    },
  ],
    # {
    #   "text": "blurry, bad",
    #   "weight": -1
    # }
  # ],
  "image_prompts": [
    {
      "base64": img_base64,
      "weight": 1
    },
    #  {
    #   "base64": img2_base64,
    #   "weight": 0
    # }
  ],
}

 

response = requests.post(
  "https://api.stability.ai/v1/generation/stable-diffusion-v1-6/text-to-image",
  headers={
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": "Bearer sk-YweXjgJoHKQe0poLtt1j7I3AMoeT2RKPI3kN2i9Bra3yiLv2",
  },
  json=body,
)

if response.status_code != 200:
    raise Exception("Non-200 response: " + str(response.text))

data = response.json()

# make sure the out directory exists
if not os.path.exists("./out"):
    os.makedirs("./out")

for i, image in enumerate(data["artifacts"]):
    with open(f'./out/txt2img_{image["seed"]}.png', "wb") as f:
        f.write(base64.b64decode(image["base64"]))

