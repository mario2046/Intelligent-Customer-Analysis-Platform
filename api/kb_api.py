from fastapi import APIRouter, HTTPException
from typing import List
import logging

from schemas.kb_schema import KnowledgeBaseResponse, ProductInfo
from data.synthetic_generator import synthetic_data_generator

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/product/{product_name}", response_model=KnowledgeBaseResponse)
async def get_product_info(product_name: str):
    """
    Retrieve detailed information for a specific product
    """
    logger.info(f"Retrieving product information for: {product_name}")
    
    # Try to find the product data
    product_data = synthetic_data_generator.get_kb_data(product_name)
    
    if not product_data:
        raise HTTPException(status_code=404, detail=f"Product '{product_name}' not found")
    
    return KnowledgeBaseResponse(product_info=product_data)

@router.get("/products", response_model=List[str])
async def get_all_products():
    """
    Retrieve list of all available products
    """
    logger.info("Retrieving list of all products")
    
    # Return all product names from our constants
    from data.constants import PRODUCTS
    return [product["name"] for product in PRODUCTS]