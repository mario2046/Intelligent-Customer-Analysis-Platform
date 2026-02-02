from pydantic import BaseModel
from typing import List


class ProductFeature(BaseModel):
    name: str
    description: str


class ProductSpec(BaseModel):
    category: str
    features: List[ProductFeature]
    compliance_standards: List[str]
    target_industries: List[str]
    pricing_tier: str  # basic, professional, enterprise


class CaseStudy(BaseModel):
    title: str
    description: str
    client_sector: str
    results: List[str]


class ProductInfo(BaseModel):
    product_name: str
    description: str
    specifications: ProductSpec
    case_studies: List[CaseStudy]
    pricing: dict  # pricing tiers with features


class KnowledgeBaseResponse(BaseModel):
    product_info: ProductInfo