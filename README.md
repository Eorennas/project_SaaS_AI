# project_SaaS_AI

Um SaaS simples de geração de imagens a partir de prompts, construído com Streamlit e Google GenAI (Gemini).

---

## 🔍 Descrição

Este projeto é um aplicativo web que permite ao usuário:

- Gerar imagens a partir de um prompt de texto usando o modelo **imagen-3.0-generate-002** do Google GenAI.  
- Manter em cache, na sessão do Streamlit, o histórico de todas as imagens geradas.  
- Baixar qualquer imagem (nova ou do histórico) com um clique.  
- Navegar entre abas “Gerar Imagem” e “Histórico” de forma intuitiva.

---

## ✨ Funcionalidades

1. **Geração de Imagem**  
2. **Histórico em Sessão** (via `st.session_state`)  
3. **Download** das imagens geradas  
4. Layout responsivo usando `st.tabs()` e `use_container_width=True`

---

## 🚀 Pré-requisitos

- Python 3.9 ou superior  
- Conta Google Cloud com acesso à API GenAI e uma **API Key** válida  
- (Opcional) Docker, para containerizar e facilitar o deploy  

---

## 📦 Instalação e Execução Local

1. **Clone o repositório**  
   ```bash
   git clone https://github.com/seu_usuario/project_SaaS_AI.git
   cd project_SaaS_AI
2. **Crie e ative um virtualenv**  
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate       # Linux / macOS
    .venv\Scripts\activate          # Windows
3. **Instale as dependências**  
    ```bash
    pip install --upgrade pip
    pip install -r requirements.txt
4. **Defina sua API Key**  
    ```bash
    api_key = "SUA_GOOGLE_GENAI_API_KEY"
5. **Execute o aplicativo**
    ```bash
    streamlit run main.py
---
---
## 📁 Estrutura de Pastas

project_SaaS_AI/
├── LICENSE                  # licença MIT
├── main.py                  # código principal Streamlit
└── requirements.txt         # dependências Python
---