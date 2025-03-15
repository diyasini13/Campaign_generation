
from google.cloud import aiplatform
from PIL import Image as im
import io
from base64 import b64decode
import os
import vertexai
from vertexai.preview.vision_models import Image, ImageGenerationModel
from vertexai.generative_models import GenerativeModel
from vertexai.generative_models import Image as image_gen , Part


# --- Configuration ---
PROJECT_ID = "heroprojectlivedemo"  # Replace with your project ID
LOCATION = "us-central1"  # Replace with your location
MODEL_GEMINI = "gemini-1.5-flash-002"
MODEL_IMAGEN = "imagen-3.0-generate-002"

# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './path-to-credential'
# os.environ['GOOGLE_CLOUD_PROJECT'] = ''

# # --- Initialize Gemini and Vertex AI ---

# aiplatform.init(project=PROJECT_ID, location=LOCATION)
    # Initialize Vertex AI with the project ID and location
vertexai.init(project=PROJECT_ID, location="us-central1")

def generate_text_gemini(prompt):
    model =  GenerativeModel(MODEL_GEMINI)
    response = model.generate_content(f"""Write a cheerful email for a sales campaign based on the : {prompt} """)
    return response.text

def generate_insta_gemini(prompt):
    model =  GenerativeModel(MODEL_GEMINI)
    response = model.generate_content(f"""Write a cheerful insta post/story content for a sales campaign based on the : {prompt} """)
    return response.text

def generate_image_imagen(prompt):
    output_file = "./generated_image.png" 
    generation_model = ImageGenerationModel.from_pretrained(MODEL_IMAGEN)
    images = generation_model.generate_images(
        prompt=prompt,
        negative_prompt="", # You can add a negative prompt here if needed.
        aspect_ratio="1:1", # You can change the aspect ratio. Examples: "16:9", "9:16", "4:3", "3:4"
    )
     # Save the generated image
    images[0].save(location=output_file, include_generation_parameters=False)
    


def image_to_bytes(image: im) -> str:
    """Converts a PIL object to a base64 string."""
    with io.BytesIO() as buffer:
        image.save(buffer, format="JPEG")
        img_bytes = buffer.getvalue()
    return img_bytes

def generate_description_gemini(image):
    model = GenerativeModel("gemini-1.5-flash-002")
    image_bytes = image_to_bytes(image)
    prompt_parts = [
            Part.from_data(data=image_bytes, mime_type=f"image/{image.format.lower()}"),
            "Write product description and an email to sell this product in detail. Be cheerful, fun and sassy.",
        ]
    response = model.generate_content(prompt_parts)
    return response.text