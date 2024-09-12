from datetime import datetime
from typing import Tuple

from pydantic import BaseModel, EmailStr, validator, PositiveFloat, PositiveInt
from enum import Enum

class ProdutoEnum(str, Enum): 
    produto1 = "ZapFlow com Gemini"
    produto2 = "ZapFlow com chatGPT"
    produto3 = "ZapFlow com Lhama3.0"


class Vendas(BaseModel):
    email:EmailStr
    data: datetime
    valor: PositiveFloat
    quantidade: PositiveInt 
    produto: ProdutoEnum

    # @validate_call('produto')
    # def categoria_deve_estar_no_enum(cls,v):
    #     return v