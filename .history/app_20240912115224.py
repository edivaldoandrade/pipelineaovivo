import streamlit as st

def main():
    
    st.title("Sistema de CRM e Vendas")
    st.text_input("Inserir email do vendedor")
    st.date_input("Data da venda")
    st.time_input("Hora da venda")
    st.number_input("Valor da Venda")
    st.number_input("Quantidade de produtos")
    st.selectbox("Produtos vendidos", 
                [
                    "ZapFlow com Gemini", 
                    "ZapFlow com ChapGPT", 
                    "ZapFlow com Lhama 3.0"
                ],
                index=None,
                placeholder="Selecione os Produtos"
            )

if __name__=="__main__":
    main()