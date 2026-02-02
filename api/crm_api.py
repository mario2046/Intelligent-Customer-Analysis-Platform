from fastapi import APIRouter, HTTPException
from typing import List
import logging

from schemas.crm_schema import CRMResponse
from data.synthetic_generator import synthetic_data_generator

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/customer/{customer_name}", response_model=CRMResponse)
async def get_customer_data(customer_name: str):
    """
    Retrieve CRM data for a specific customer
    """
    logger.info(f"Retrieving CRM data for customer: {customer_name}")
    
    # Try to find the customer data
    crm_data = synthetic_data_generator.get_crm_data(customer_name)
    
    if not crm_data:
        raise HTTPException(status_code=404, detail=f"Customer '{customer_name}' not found")
    
    return crm_data

@router.get("/customers", response_model=List[str])
async def get_all_customers():
    """
    Retrieve list of all available customers
    """
    logger.info("Retrieving list of all customers")
    
    customers = synthetic_data_generator.get_all_customers()
    return customers
