import streamlit as st
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

# Inicializa o client
client = genai.Client(api_key="AIzaSyCiGZy3IrHb0rJyBAM6JVfAyiCTrOwsguI")

st.title("🔮 Gerador de Imagens com Gemini")

# Text area com key única
prompt = st.text_area(
    "Digite um prompt para gerar a imagem:",
    key="prompt_area"
)

# Botão para disparar geração
if st.button("Gerar Imagem", key="generate_button"):
    with st.spinner("Gerando imagem..."):
        try:
            # Gera uma imagem com o modelo Imagen 3
            response = client.models.generate_images(
                model="imagen-3.0-generate-002",
                prompt=prompt,
                config=types.GenerateImagesConfig(
                    number_of_images=1,
                    # outros parâmetros opcionais aqui...
                ),
            )

            if not response.generated_images:
                st.error("Nenhuma imagem foi gerada.")
            else:
                # 1) Extrai os bytes da imagem
                raw_bytes = response.generated_images[0].image.image_bytes

                # 2) Converte para PIL.Image
                pil_image = Image.open(BytesIO(raw_bytes))

                # 3) Exibe no Streamlit
                st.image(
                    pil_image,
                    caption="Imagem gerada",
                    use_container_width=True
                )

                # 4) Prepara buffer para download
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
