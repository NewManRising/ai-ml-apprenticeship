from pydantic import BaseModel
from enum import Enum


class Qualification(str, Enum):
  HIGH = "HIGH"
  MEDIUM = "MEDIUM"
  LOW = "LOW"


class CompanyEnrichment(BaseModel):
  company_summary: str
  products_services: list[str]
  sales_insight: str
  qualification: Qualification
  qualification_reason: str