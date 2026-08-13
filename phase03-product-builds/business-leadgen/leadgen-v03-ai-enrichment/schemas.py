from pydantic import BaseModel

class CompanyEnrichment(BaseModel):
  company_summary: str
  products_services: list[str]
  sales_insight: str
  qualification: str