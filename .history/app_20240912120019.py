import streamlit as st

def main():
    
    st.title("Sistema de CRM e Vendas")

    email      = st.text_input("Inserir email do vendedor")
    data       = st.date_input("Data da venda")
    hora       = st.time_input("Hora da venda")
    valor      = st.number_input("Valor da Venda")
    quantidade = st.number_input("Quantidade de produtos")
    produto    = st.selectbox("Produto vendido", 
                        [
                            "ZapFlow com Gemini", 
                            "ZapFlow com ChapGPT", 
                            "ZapFlow com Lhama 3.0"
                        ],
                        index=None,
                        placeholder="Selecione o Produto"
                    )
    if st.button("Salvar"):
        st.write("**Dados da Venda:**")
        st.write(f"Email do vendedor: {email}")
        st.write(f"Data e hora da compra: {data_hora}")
        st.write(f"Valor da venda: {valor:.2f}")
        st.write(f"Quantidade de produtos: {quantidade}")
        st.write(f"Produto: {produto}")


if __name__=="__main__":
    main()