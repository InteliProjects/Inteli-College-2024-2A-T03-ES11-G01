import streamlit as st
import requests
from components.card import card_container
url_img = "/home/bruno/Documents/GitHub/2024-2A-T03-ES11-G01/src/frontend/assets/logo.png"
import base64
url = 'http://localhost:5001'

def get_image_as_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()
    
image_base64 = get_image_as_base64(url_img)

with card_container():

    st.markdown(
        f"""
        <div style="text-align: center;">
            <img src="data:image/png;base64,{image_base64}" width="150">
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<h4 style='text-align: center;'>Bem vindo ao DataLoom!</h4>", unsafe_allow_html=True)

    input_style = """
        <style>
        /* Estiliza todos os inputs de texto */
        .stTextInput div[data-baseweb="input"] {
            border: 1px solid #F3F3F6;
            background-color: #F3F3F6;
            border-radius: 4px;
            padding: 5px;
        }
        </style>
    """

    st.markdown(input_style, unsafe_allow_html=True)

    email = st.text_input("Email", placeholder="Digite seu email")
    senha = st.text_input("Senha", placeholder="Digite sua senha", type="password")

    button_style = """
        <style>
        .stButton > button {
            background-color: #297846;
            color: #FFFFFF;
            padding: 10px 24px;
            border-radius: 4px;
            border: none;
            cursor: pointer;
            font-size: 16px;
            width: 100%;
        }
        
        .stButton > button:hover {
            background-color: #297846;
        }
        </style>
    """

    st.markdown(button_style, unsafe_allow_html=True)

    if st.button("Entrar"):
        payload = {
            'email': email,
            'password': senha
        }

        response = requests.post(f"{url}/auth/login", json=payload)

        if response.status_code == 200:
            print('Login bem-sucedido:', response.json())
            st.success(f"Bem-vindo(a), {email}!")

            access_token = response.json().get('access_token')

            headers = {
                'Authorization': f'Bearer {access_token}'
            }

            who_am_i_response = requests.get(f"{url}/auth/who_am_i", headers=headers)
            user_data = who_am_i_response.json()
            print(user_data['is_seller'])

            if user_data['is_seller']:
                st.switch_page("./pages/home_vendedor.py")
            else:
                st.switch_page("./pages/home_gerente.py")
                
        else:
            print('Falha no login:', response.json())
            st.error("Email ou senha incorretos. Por favor, tente novamente.")

    st.markdown("""
        <style>
        .css-1aumxhk {
            max-width: 400px;
            margin: auto;
        }
        </style>
        """, unsafe_allow_html=True)
