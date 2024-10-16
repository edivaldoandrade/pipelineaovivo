from datetime import datetime
from enum import Enum
from typing import Tuple

from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt


class ProdutoEnum(str, Enum):
    produto1 = "ZapFlow com Gemini"
    produto2 = "ZapFlow com ChapGPT" 
    produto3 = "ZapFlow com Lhama 3.0"

class Vendas(BaseModel):
    """
    Modelo de dados para vendas.

    Args:
        email (EmailStr): email do comprador
        data
        valor
        produto
        quantidade
    """
    email: EmailStr
    data: datetime
    valor: PositiveFloat
    quantidade: PositiveInt
    produto: ProdutoEnum




