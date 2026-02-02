from pydantic import BaseModel
from typing import List
from datetime import datetime


class MarketingEvent(BaseModel):
    event_id: str
    date: datetime
    event_type: str  # webinar, conference, trade_show, email_campaign
    title: str
    attended: bool
    engagement_level: int  # 1-5 scale
    outcome: str


class ContentDownload(BaseModel):
    download_id: str
    date: datetime
    title: str
    type: str  # whitepaper, case_study, datasheet, video
    category: str  # security, compliance, performance, etc.
    viewed_percentage: int


class EngagementResponse(BaseModel):
    customer_name: str
    marketing_events: List[MarketingEvent]
    content_downloads: List[ContentDownload]