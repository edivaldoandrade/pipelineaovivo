from datetime import datetime
from enum import Enum
from typing import Tuple

from pydantic import BaseModel, EmailStr, validate_call, PositiveFloat, PositiveInt


class ProdutoEnum(str, Enum):
    produto1 = "ZapFlow com Gemini"
    produto2 = "ZapFlow com ChapGPT" 
    produto3 = "ZapFlow com Lhama 3.0"

class Vendas(BaseModel):
    email: EmailStr
    data: datetime
    valor: PositiveFloat
    quantidade: PositiveInt
    produto: ProdutoEnum


    @validate_call('produto')
    def categoria_no_enum(cls, v):
        return v



