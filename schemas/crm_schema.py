from pydantic import BaseModel
from typing import List
from datetime import datetime
from enum import Enum


class SalesStage(str, Enum):
    lead = "lead"
    qualified = "qualified"
    proposal = "proposal"
    negotiation = "negotiation"
    closed_won = "closed_won"
    closed_lost = "closed_lost"


class CustomerProfile(BaseModel):
    id: str
    name: str
    industry: str
    size: str  # enterprise, mid_market, smb
    region: str
    contact_person: str
    contact_email: str
    contact_phone: str
    annual_revenue: int  # in USD
    primary_product_interest: str


class SalesHistoryItem(BaseModel):
    transaction_id: str
    date: datetime
    product: str
    amount: float
    stage: SalesStage
    notes: str


class SalesPipelineItem(BaseModel):
    opportunity_id: str
    product: str
    stage: SalesStage
    probability: float
    estimated_value: float
    expected_close_date: datetime
    notes: str


class CRMResponse(BaseModel):
    customer_profile: CustomerProfile
    sales_history: List[SalesHistoryItem]
    sales_pipeline: List[SalesPipelineItem]
