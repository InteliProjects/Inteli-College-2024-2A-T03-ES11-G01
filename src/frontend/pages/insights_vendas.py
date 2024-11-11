import streamlit as st
from components.card import card_container

st.set_page_config(page_title="Insight de vendas", layout="centered")

st.title("Insights de vendas")

# mocks - to-do get data from backend
products = [
    {"name": "Anthelios AOX Daily Antioxidant", "desc": "Protetor solar La Roche-Posay", "price": "R$60,00", "discount": "12% - R$7,00"},
    {"name": "Effaclar Duo+", "desc": "Gel anti-acne La Roche-Posay", "price": "R$80,00", "discount": "15% - R$12,00"},
    {"name": "Normaderm Phytosolution", "desc": "Gel hidratante Vichy", "price": "R$90,00", "discount": "10% - R$9,00"},
    {"name": "Cicaplast Baume B5", "desc": "Bálsamo reparador La Roche-Posay", "price": "R$55,00", "discount": "8% - R$4,50"}
]

if 'product_index' not in st.session_state:
    st.session_state['product_index'] = 0

def previous_product():
    if st.session_state['product_index'] > 0:
        st.session_state['product_index'] -= 1

def next_product():
    if st.session_state['product_index'] < len(products) - 1:
        st.session_state['product_index'] += 1

# -- Products with high profit --
with card_container():
    st.markdown("""
        <style>
                
        .block-container {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: row; /* Alinha os itens na coluna */
            align-content: center;
        }

        .stButton > button {
            color: #2b2b2b;
            border-radius: 50%;
            border: none;
            width: 40px;
            height: 40px;
            background-color: #FFFFFF;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .product-card {
            background-color: #E8F5F6; /* Fundo levemente azul */
            border: 2px solid #8ED1DC; /* Borda azul clara */
            border-radius: 10px;
            padding: 20px;
            width: 250px;
            height: 200px; /* Altura fixa */
            text-align: center;
            margin: 0 auto;
        }

        .product-name {
            font-weight: bold;
            font-size: 18px;
            color: #202124;
            margin-bottom: 5px;
        }

        .product-desc {
            font-size: 14px;
            color: #202124;
            margin-bottom: 10px;
        }

        .product-price {
            font-weight: bold;
            font-size: 20px;
            color: #202124;
            margin-bottom: 5px;
        }

        .product-discount {
            font-size: 14px;
            color: #202124;
        }

        .arrow {
            font-size: 24px;
            color: #8ED1DC;
            cursor: pointer;
            display: flex;
            justify-content: space-around;
            align-content: center;
        }

        .indicator {
            margin-top: 10px;
            text-align: center;
        }

        .indicator span {
            display: inline-block;
            width: 10px;
            height: 10px;
            background-color: #C4C4C4;
            border-radius: 50%;
            margin: 0 5px;
        }

        .active {
            background-color: #8ED1DC;
        }
        </style>
        """, unsafe_allow_html=True)

    st.markdown("<h3>Produtos com maior margem de lucro</h3>", unsafe_allow_html=True)
    st.markdown("<p>Agosto - 2024</p>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([0.1, 1, 0.1], vertical_alignment="center", gap="small")

    # btn - previious product
    with col1:
        st.markdown("<div class='arrow' >", unsafe_allow_html=True)
        if st.button("◀", key="prev"):
            previous_product()
            print(st.session_state['product_index'])

    # btn - next product
    with col3:
        st.markdown("<div class='arrow'>", unsafe_allow_html=True)
        if st.button("▶", key="next"):
            next_product()
            print(st.session_state['product_index'])

    current_product = products[st.session_state['product_index']]

    with col2:
        st.markdown(f"""
        <div class='product-card'>
            <div class='product-name'>{current_product['name']}</div>
            <div class='product-desc'>{current_product['desc']}</div>
            <div class='product-price'>{current_product['price']}</div>
            <div class='product-discount'>{current_product['discount']}</div>
        </div>
        """, unsafe_allow_html=True)

    # user location
    indicators = "".join(
        [
            f"<span class='{'active' if i == st.session_state['product_index'] else ''}'></span>"
            for i in range(len(products))
        ]
    )

    st.markdown(f"""
    <div class='indicator'>
        {indicators}
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='height: 45px;'></div>", unsafe_allow_html=True)

# -- Cross selling --
with card_container(key="venda-cruzada"):
    # st.markdown("""
    #     <style>
    #     .search-input {
    #         width: 80%;
    #         padding: 10px;
    #         border: 1px solid #DADCE0;
    #         border-radius: 5px;
    #         font-size: 16px;
    #         color: #5F6368;
    #         display: inline-block;
    #     }
    #     </style>
    #     """, unsafe_allow_html=True)

    st.markdown("<h3>Venda cruzada</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color:#5F6368'>Descubra sugestões de produtos que são vendidos juntos</p>", unsafe_allow_html=True)

    search_query_cross_sell = st.text_input('', placeholder="Busque por um produto", key="search_input_cross_sell")

    if search_query_cross_sell:
        st.markdown("""
        <div style="margin-top: 20px;">
            <p>Aromatics Elixir Eau de (90%)</p>
            <p>Limited Edition Happy Perfume (82.1%)</p>
            <p>Hypnotic Poison Eau De (80%)</p>
        </div>
        """, unsafe_allow_html=True)

# -- Substitutes --
with card_container(key="produtos-substitutos"):
    # st.markdown("""
    #     <style>
    #     .search-input {
    #         width: 80%;
    #         padding: 10px;
    #         border: 1px solid #DADCE0;
    #         border-radius: 5px;
    #         font-size: 16px;
    #         color: #5F6368;
    #         display: inline-block;
    #     }
    #     </style>
    #     """, unsafe_allow_html=True)

    st.markdown("<h3>Produtos substitutos</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color:#5F6368'>Descubra sugestões de produtos similares</p>", unsafe_allow_html=True)

    search_query_substitute = st.text_input('', placeholder="Busque por um produto", key="search_input_substitute")

    if search_query_substitute:
        st.markdown("""
        <div style="margin-top: 20px;">
            <p>Aromatics Elixir Eau de (80%)</p>
        </div>
        """, unsafe_allow_html=True)