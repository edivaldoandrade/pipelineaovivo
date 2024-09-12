from datetime import datetime, time

import streamlit as st
from pydantic import ValidationError

from contracto import Vendas
from database import salvar_no_postgres


def main():
    
    st.title("Sistema de CRM e Vendas")

    email      = st.text_input("Inserir email do vendedor")
    data       = st.date_input("Data da venda", datetime.now())
    hora       = st.time_input("Hora da venda", value=time(9,0))
    valor      = st.number_input("Valor da Venda", min_value=0.0, format="%.2f")
    quantidade = st.number_input("Quantidade de produtos", min_value=1, step=1)
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

        try:
            data_hora = datetime.combine(data, hora)

            venda = Vendas(
                email = email,
                data = data_hora,
                valor = valor,
                quantidade = quantidade,
                produto = produto
            )
            st.write(venda)
            salvar_no_postgres(venda)
        except ValidationError as e:
            st.error(f"Ocorreu um erro {e}")

        


if __name__=="__main__":
    main()