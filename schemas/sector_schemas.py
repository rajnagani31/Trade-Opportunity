from enum import Enum
from pydantic import BaseModel

class SectorEnum(str,Enum):
    pharmaceuticals = "pharmaceuticals"
    technology = "technology"
    agriculture = "agriculture"
    finance = "finance"
    energy = "energy"
    infrastructure = "infrastructure"
    healthcare = "healthcare"
    manufacturing = "manufacturing"
    real_estate = "real_estate"
    retail = "retail"
    ecommerce = "E-commerce"
    transportation = "transportation"

class SectorRequest(BaseModel):
    sector: SectorEnum
