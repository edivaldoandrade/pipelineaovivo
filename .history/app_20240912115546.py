import streamlit as st

def main():
    
    st.title("Sistema de CRM e Vendas")

    email= st.text_input("Inserir email do vendedor")
    data = st.date_input("Data da venda")
    hora = st.time_input("Hora da venda")
    st.number_input("Valor da Venda")
    st.number_input("Quantidade de produtos")
    st.selectbox("Produto vendido", 
                [
                    "ZapFlow com Gemini", 
                    "ZapFlow com ChapGPT", 
                    "ZapFlow com Lhama 3.0"
                ],
                index=None,
                placeholder="Selecione o Produto"
            )
    if st.button("Salvar"):


if __name__=="__main__":
    main()