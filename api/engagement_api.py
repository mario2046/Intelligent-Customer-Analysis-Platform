from fastapi import APIRouter, HTTPException
import logging

from schemas.engagement_schema import EngagementResponse
from data.synthetic_generator import synthetic_data_generator

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/customer/{customer_name}/history", response_model=EngagementResponse)
async def get_engagement_history(customer_name: str):
    """
    Retrieve engagement history for a specific customer
    """
    logger.info(f"Retrieving engagement history for customer: {customer_name}")
    
    # Try to find the customer data
    engagement_data = synthetic_data_generator.get_engagement_data(customer_name)
    
    if not engagement_data:
        raise HTTPException(status_code=404, detail=f"Customer '{customer_name}' not found")
    
    return engagement_data