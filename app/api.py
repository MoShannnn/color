
from PIL import Image

import openai
from decouple import config
import numpy as np



# Set your OpenAI API key
openai.api_key = config("OPENAI_API_KEY")

def classify_skin_tone(image):
    # Open the image file
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
            #{"role": "system", "content": "You are Colorbot, a color analysis expert.Determine my specific one seasonal color  from 12 color seasons."},
            {"role": "user", "content": "This is my selfie photo . First, detect my skin tone and  then tell my specific personal color season. "
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
- **Bright Spring**: Warm-Neutral undertone, Bright characteristic
- **True Spring**: Warm undertone, Saturated characteristic
- **Light Spring**: Warm-Neutral undertone, Light characteristic
- **Light Summer**: Cool-Neutral undertone, Light characteristic
- **True Summer**: Cool undertone, Muted characteristic
- **Soft Summer**: Cool-Neutral undertone, Soft characteristic
- **Soft Autumn**: Warm-Neutral undertone, Soft characteristic
- **True Autumn**: Warm undertone, Muted characteristic
- **Deep Autumn**: Warm-Neutral undertone, Deep characteristic
- **Deep Winter**: Cool-Neutral undertone, Deep characteristic
- **True Winter**: Cool undertone, Saturated characteristic
- **Bright Winter**: Cool-Neutral undertone, Bright characteristic

                                        """
                                       
                                        "I want only the name of the color season from your response. No need to include other text.Your response should be the same everytime."},
            {"role": "user", "content": f"Image description: {img_array}"}
        ],
        temperature=0.1,
        top_p=0.1,
        seed = 1234
        #frequency_penalty=0.1

    )

    return response.choices[0].message['content']

