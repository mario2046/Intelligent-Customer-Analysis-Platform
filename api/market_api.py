from fastapi import APIRouter, HTTPException
import logging

from schemas.market_schema import MarketIntelligenceResponse
from data.synthetic_generator import synthetic_data_generator

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/company/{company_name}/news", response_model=MarketIntelligenceResponse)
async def get_company_news(company_name: str):
    """
    Retrieve market intelligence for a specific company
    """
    logger.info(f"Retrieving market intelligence for company: {company_name}")
    
    # Try to find the company data
    market_data = synthetic_data_generator.get_market_data(company_name)
    
    if not market_data:
        raise HTTPException(status_code=404, detail=f"Company '{company_name}' not found")
    
    return market_data