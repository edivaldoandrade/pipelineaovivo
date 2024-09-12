from datetime import datetime
from typing import Tuple

from pydantic import BaseModel


class Vendas(BaseModel):
    email: str
    data: datetime
    valor: float
    quantidade: int
    produto: str
