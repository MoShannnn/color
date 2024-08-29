
from PIL import Image

import openai
from decouple import config
import numpy as np



# Set your OpenAI API key
openai.api_key = config("OPENAI_API_KEY")

def classify_skin_tone(image):
    # open image
    image = Image.open(image.file)
    # Convert the image to RGB
    image = image.convert("RGB")
    # Resize image for processing
    image = image.resize((50, 50))
    # Convert image to array
    img_array = np.array(image)

    # Call OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            # {"role": "system", "content": "You are Colorbot, a color analysis expert.Determine my specific one seasonal color  from 12 color seasons."},
            {"role": "user",
             "content": "This is my selfie photo . First, detect my skin tone and  then tell my specific personal color season. "
                       
                        "Give your response with this format."
                        "For example: (give me specific name of one color season that match with my photo (for example: Deep winter, Bright Autumn, and etc ) )based on the following rules for each season: "

                        """
                                        Rules:
# Skin Tone 
- **Light**: White added
- **True**: “Pure” season color/temperature
- **Soft/Muted**: Gray added
- **Deep/Dark**: Black added
- **Bright/Clear**: Extremely saturated and clear

# Color Seasons
- **Bright Spring**: Bright and warm, with either neutral or neutral-warm undertones. You are a Bright Spring if the primary colour aspect of your overall appearance is bright, and the secondary aspect is warm
- **True Spring**: Warm and bright, with warm and golden undertones.  If your primary color aspect is warm and the secondary aspect is bright, then you are a True Spring.
- **Light Spring**: Light and warm, with neutral-warm undertones.If your primary color aspect is light and the secondary aspect is warm, then you are a Light Spring. 
- **Light Summer**: Light and cool, with cool-neutral undertones. If you are a Light Summer, your primary color aspect is light, and the secondary aspect is cool,
- **True Summer**: Cool and muted, with cool undertones and a potential pink tinge. You are a True Summer if the primary colour aspect of your overall appearance is cool.
- **Soft Summer**: Muted and cool, with neutral or neutral-cool with ashy and pinky undertones.If you are a Soft Summer, your primary color aspect is muted, and the secondary aspect is cool. 
- **Soft Autumn**: Muted and warm, neutral-warm with beige and sand undertones.If you are a Soft Autumn, your primary color aspect is muted, and the secondary aspect is warm. 
- **True Autumn**:  Warm and muted, with obvious warm undertones.You are a True Autumn if the primary color aspect of your overall appearance is warm, and the secondary aspect is muted. 
- **Deep Autumn**:Dark and warm, with warm-neutral undertones. A Deep Autumn if the primary colour aspect of your overall appearance is dark, and the secondary aspect is warm.
- **Deep Winter**:Dark and cool, with neutral-cool undertones. The overall appearance is dark, bright and cool.Dark Winter hair is also dark, ranging from medium brown over dark brown to black. 
- **True Winter**: Cool and bright, with clear cool, blue undertones. You are a True Winter if the primary colour aspect of your overall appearance is cool, and the secondary aspect is bright.
- **Bright Winter**: Bright and cool, with cool-neutral undertones. You are a Bright Winter if the primary colour aspect of your overall appearance is bright, and the secondary aspect is cool .

                                        """
                                       
                                        "I want only the name of the color season from your response. No need to include other text.Your response should be the same everytime."},
            {"role": "user", "content": f"Image description: {img_array.tolist()}"}
        ],
        temperature=0.1,
        top_p=0.1,
        seed = 1234,
        

    )

    return response.choices[0].message['content']

