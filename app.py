import io
import streamlit as st
from generate_funcs import generate_text_gemini, generate_image_imagen, generate_description_gemini
from PIL import Image as im
import auth_token

def app():
# --- Streamlit App ---
    st.title("Gemini and Imagen Fun App")

    # --- Email Generation Section ---
    st.header("Email Generation")
    email_prompt = st.text_area("Enter the prompt for email generation for your content")
    if st.button("Generate Email"):
        full_email_prompt = f"Be cheerful, fun and sassy. {email_prompt}"
        generated_email = generate_text_gemini(full_email_prompt)
        st.write(generated_email)

    # --- Instagram Post Generation Section ---
    st.header("Instagram Post Generation")
    insta_prompt = st.text_area("Enter the prompt for instagram caption generation for your content.")
    if st.button("Generate Instagram Campaign"):
        full_insta_prompt = f"Be cheerful, fun and sassy. {insta_prompt}"
        generated_insta_post = generate_text_gemini(full_insta_prompt)
        st.write(generated_insta_post)

    # --- Image Generation Section ---
    st.header("Image Generation")
    image_prompt = st.text_area("Enter Image Description", "A vibrant sunset over a futuristic city")
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