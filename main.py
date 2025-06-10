import streamlit as st
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

api_key = st.secrets("API_KEY")
client = genai.Client(api_key=api_key)

st.title("🔮 Gerador de Imagens com Gemini SaaS")


if "history" not in st.session_state:
    st.session_state["history"] = []  


tab_generate, tab_history = st.tabs(["🖼️ Gerar Imagem", "📂 Histórico"])


with tab_generate:
    prompt = st.text_area(
        "Digite um prompt para gerar a imagem:",
        key="prompt_area"
    )

    if st.button("Gerar Imagem", key="generate_button"):
        with st.spinner("Gerando imagem..."):
            try:
                response = client.models.generate_images(
                    model="imagen-3.0-generate-002",
                    prompt=prompt,
                    config=types.GenerateImagesConfig(
                        number_of_images=1,
                    ),
                )

                if not response.generated_images:
                    st.error("Nenhuma imagem foi gerada.")
                else:
                    
                    raw_bytes = response.generated_images[0].image.image_bytes
                    pil_image = Image.open(BytesIO(raw_bytes))

                    
                    st.image(pil_image, caption="🆕 Imagem gerada", use_container_width=True)

                    # Guarda no histórico (bytes)
                    st.session_state["history"].append(raw_bytes)

                    # Botão de download
                    buf = BytesIO()
                    pil_image.save(buf, format="PNG")
                    buf.seek(0)
                    st.download_button(
                        "📥 Baixar Imagem",
                        data=buf,
                        file_name="imagem_gerada.png",
                        mime="image/png"
                    )

            except Exception as e:
                st.error(f"Erro ao gerar imagem: {e}")


with tab_history:
    st.markdown("### Seu histórico de imagens geradas nesta sessão")
    if not st.session_state["history"]:
        st.info("Nenhuma imagem ainda. Vá para a aba “Gerar Imagem” para criar a primeira.")
    else:
        for idx, img_bytes in enumerate(reversed(st.session_state["history"]), start=1):
            pil_img = Image.open(BytesIO(img_bytes))
           
            st.image(
                pil_img,
                caption=f"Histórico #{idx}",
                use_container_width=True  
            )
            st.download_button(
                f"📥 Baixar Histórico #{idx}",
                data=img_bytes,
                file_name=f"historico_{idx}.png",
                mime="image/png",
                key=f"download_{idx}"
            )
