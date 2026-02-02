from pydantic import BaseModel
from typing import List
from datetime import datetime


class NewsItem(BaseModel):
    id: str
    date: datetime
    title: str
    source: str
    category: str  # financial, product_launch, acquisition, regulation
    summary: str
    relevance_score: float  # 0-1


class FilingItem(BaseModel):
    id: str
    date: datetime
    type: str  # 10k, 10q, proxy_statement, press_release
    title: str
    url: str
    key_points: List[str]


class MarketIntelligenceResponse(BaseModel):
    company_name: str
    recent_news: List[NewsItem]
    regulatory_filings: List[FilingItem]