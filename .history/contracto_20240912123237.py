from datetime import datetime
from enum import Enum
from typing import Tuple

from pydantic import BaseModel, EmailStr


class ProdutoEnum(str, Enum):
    produto1 = "ZapFlow com Gemini"
    produto2 = "ZapFlow com ChapGPT" 
    produto3 = "ZapFlow com Lhama 3.0"

class Vendas(BaseModel):
    email: EmailStr
    data: datetime
    valor: float
    quantidade: int
    produto: str



