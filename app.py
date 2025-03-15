import io
import streamlit as st
from generate_funcs import generate_text_gemini, generate_image_imagen, generate_description_gemini, generate_insta_gemini 
from PIL import Image as im
import auth_token

def app():
# --- Streamlit App ---
    st.title("Campaign generation made easier with GenAI")

    # --- Email Generation Section ---
    st.header("Email Generation")
    email_prompt = st.text_area("Enter the prompt for email generation for your content","Write a concise and engaging email to announce our new Spring/Summer collection launch party. Include date, time, location, and a 50% discount for attendees. Highlight the collection's vibrant, seasonal style and encourage prompt RSVPs due to limited space. Use a catchy subject line and a clear call to action.")
    if st.button("Generate Email"):
        full_email_prompt = f"Be cheerful, fun and sassy. {email_prompt}"
        generated_email = generate_text_gemini(full_email_prompt)
        st.write(generated_email)

    # --- Instagram Post Generation Section ---
    st.header("Instagram Post Generation")
    insta_prompt = st.text_area("Enter the prompt for instagram caption generation for your content.","Create an urgent and visually appealing Instagram post for our Spring/Summer launch party. Highlight the limited-time 50% discount and encourage immediate RSVPs due to limited space. Include date, time, and location, and suggest a striking image")
    if st.button("Generate Instagram Campaign"):
        full_insta_prompt = f"Be cheerful, fun and sassy. {insta_prompt}"
        generated_insta_post = generate_insta_gemini(full_insta_prompt)
        st.write(generated_insta_post)

    # --- Image Generation Section ---
    st.header("Image Generation")
    image_prompt = st.text_area("Enter Image Description", "Design a visually compelling promotional piece for a Spring Summer collection launch party. The core message is '50% Off Everything!' and should be prominently featured. The imagery should evoke feelings of excitement and urgency, highlighting the incredible value being offered. The atmosphere should be celebratory, with a focus on the new collection's vibrant colors and on-trend styles. Imagine customers eagerly browsing racks of clothing, trying on pieces, and enjoying the party atmosphere. The prompt should communicate the idea of a stylish, accessible event where everyone can find something they love at an unbeatable price. Make sure that the spelling are accurate in the image and no grammatical errors and no additional text written.")
    if st.button("Generate Image"):
        generate_image_imagen(image_prompt)
        generated_image = im.open("./generated_image.png")
        st.image(generated_image, caption="Generated Image")


    # --- Product Description from Image Section ---
    st.header("Product Description from Image")
    uploaded_file = st.file_uploader("Upload an image of the product", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = im.open(uploaded_file)
        st.image(image, caption="Uploaded Image")

        if st.button("Generate Product Description"):
            generated_desc = generate_description_gemini(image)
            st.write(generated_desc)

if __name__ == "__main__":
    auth_token.authentication();
    app();