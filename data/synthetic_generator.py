import random
from datetime import datetime, timedelta
from typing import List, Dict, Tuple
from faker import Faker
from .constants import CUSTOMER_ARCHETYPES, PRODUCTS, ENGAGEMENT_CATEGORIES, NEWS_CATEGORIES
from schemas.crm_schema import CustomerProfile, SalesHistoryItem, SalesPipelineItem, CRMResponse
from schemas.engagement_schema import MarketingEvent, ContentDownload, EngagementResponse
from schemas.market_schema import NewsItem, FilingItem, MarketIntelligenceResponse
from schemas.kb_schema import ProductInfo, ProductSpec, ProductFeature, CaseStudy


class SyntheticDataGenerator:
    def __init__(self):
        self.fake = Faker()
        self.customers = CUSTOMER_ARCHETYPES
        self.products = PRODUCTS
        self.customer_data_map = {}
        
        # Generate consistent data for each customer
        self._generate_all_customer_data()

    def _generate_all_customer_data(self):
        """Generate consistent synthetic data for all customers"""
        for customer in self.customers:
            customer_name = customer["name"]
            
            # Generate CRM data
            crm_data = self._generate_crm_data(customer)
            
            # Generate engagement data based on CRM data
            engagement_data = self._generate_engagement_data(customer_name, customer["industry"])
            
            # Generate market intelligence based on company
            market_data = self._generate_market_data(customer_name, customer["industry"])
            
            # Store all data for this customer
            self.customer_data_map[customer_name] = {
                "crm": crm_data,
                "engagement": engagement_data,
                "market": market_data
            }

    def _generate_crm_data(self, customer: Dict) -> CRMResponse:
        """Generate CRM data for a customer based on their archetype"""
        # Determine annual revenue within range
        min_rev, max_rev = customer["annual_revenue_range"]
        annual_revenue = random.randint(min_rev, max_rev)
        
        # Create customer profile
        profile = CustomerProfile(
            id=f"CUST_{customer['name'].split()[0].upper()}",
            name=customer["name"],
            industry=customer["industry"],
            size=customer["size"],
            region=customer["region"],
            contact_person=customer["contact_info"]["person"],
            contact_email=customer["contact_info"]["email"],
            contact_phone=customer["contact_info"]["phone"],
            annual_revenue=annual_revenue,
            primary_product_interest=customer["primary_interest"]
        )
        
        # Generate sales history based on customer profile
        sales_history = self._generate_sales_history(customer["name"], profile.primary_product_interest)
        
        # Generate sales pipeline based on customer profile and history
        sales_pipeline = self._generate_sales_pipeline(customer["name"], profile.primary_product_interest)
        
        return CRMResponse(
            customer_profile=profile,
            sales_history=sales_history,
            sales_pipeline=sales_pipeline
        )

    def _generate_sales_history(self, customer_name: str, primary_interest: str) -> List[SalesHistoryItem]:
        """Generate sales history based on customer's primary interest"""
        history = []
        
        # Find products related to primary interest
        relevant_products = [p for p in self.products if primary_interest.replace('_', ' ') in p['name'].lower()]
        if not relevant_products:
            # If no relevant products, pick randomly
            relevant_products = self.products
            
        for i in range(5):  # 5 historical transactions
            product = random.choice(relevant_products)
            days_ago = random.randint(30, 730)  # Within last 2 years
            date = datetime.now() - timedelta(days=days_ago)
            
            history.append(SalesHistoryItem(
                transaction_id=f"TXN_{customer_name.split()[0]}_{i+1}",
                date=date,
                product=product["name"],
                amount=random.uniform(10000, 500000),
                stage=random.choice(["closed_won", "closed_lost"]),
                notes=f"Sale related to {product['category']} needs"
            ))
        
        return history

    def _generate_sales_pipeline(self, customer_name: str, primary_interest: str) -> List[SalesPipelineItem]:
        """Generate sales pipeline based on customer's primary interest"""
        pipeline = []
        
        # Find products related to primary interest
        relevant_products = [p for p in self.products if primary_interest.replace('_', ' ') in p['name'].lower()]
        if not relevant_products:
            # If no relevant products, pick randomly
            relevant_products = self.products
            
        for i in range(3):  # 3 pipeline opportunities
            product = random.choice(relevant_products)
            days_to_close = random.randint(30, 180)
            expected_close = datetime.now() + timedelta(days=days_to_close)
            
            stage = random.choice(["qualified", "proposal", "negotiation"])
            probability_map = {"qualified": 0.3, "proposal": 0.5, "negotiation": 0.7}
            
            pipeline.append(SalesPipelineItem(
                opportunity_id=f"OPP_{customer_name.split()[0]}_{i+1}",
                product=product["name"],
                stage=stage,
                probability=probability_map[stage],
                estimated_value=random.uniform(50000, 1000000),
                expected_close_date=expected_close,
                notes=f"Opportunity for {product['category']} solution"
            ))
        
        return pipeline

    def _generate_engagement_data(self, customer_name: str, industry: str) -> EngagementResponse:
        """Generate engagement history based on customer's industry"""
        marketing_events = []
        content_downloads = []
        
        # Get engagement categories for this industry
        categories = ENGAGEMENT_CATEGORIES.get(industry, ["general"])
        
        # Generate marketing events
        for i in range(5):
            days_ago = random.randint(10, 365)
            event_date = datetime.now() - timedelta(days=days_ago)
            
            event_types = ["webinar", "conference", "trade_show", "email_campaign"]
            event_type = random.choice(event_types)
            
            marketing_events.append(MarketingEvent(
                event_id=f"EVT_{customer_name.split()[0]}_{i+1}",
                date=event_date,
                event_type=event_type,
                title=f"{random.choice(categories)} in {industry} industry",
                attended=random.choice([True, False]),
                engagement_level=random.randint(1, 5),
                outcome="Positive interest expressed" if random.choice([True, False]) else "Follow-up required"
            ))
        
        # Generate content downloads
        for i in range(5):
            days_ago = random.randint(5, 300)
            download_date = datetime.now() - timedelta(days=days_ago)
            
            content_types = ["whitepaper", "case_study", "datasheet", "video"]
            content_type = random.choice(content_types)
            
            content_downloads.append(ContentDownload(
                download_id=f"DWN_{customer_name.split()[0]}_{i+1}",
                date=download_date,
                title=f"{random.choice(categories)} {content_type.title()}",
                type=content_type,
                category=random.choice(categories),
                viewed_percentage=random.randint(20, 100)
            ))
        
        return EngagementResponse(
            customer_name=customer_name,
            marketing_events=marketing_events,
            content_downloads=content_downloads
        )

    def _generate_market_data(self, company_name: str, industry: str) -> MarketIntelligenceResponse:
        """Generate market intelligence based on company's industry"""
        news_items = []
        filing_items = []
        
        # Get news categories for this industry
        categories = NEWS_CATEGORIES.get(industry, ["general"])
        
        # Generate recent news
        for i in range(3):
            days_ago = random.randint(1, 90)
            news_date = datetime.now() - timedelta(days=days_ago)
            
            category = random.choice(categories)
            news_items.append(NewsItem(
                id=f"NEWS_{company_name.split()[0]}_{i+1}",
                date=news_date,
                title=f"{company_name} {random.choice(['announces', 'expands', 'partners with'])} in {category} space",
                source=random.choice(["Industry Journal", "Market Watch", "Business Times", "Tech Insider"]),
                category=random.choice(["financial", "product_launch", "acquisition", "regulation"]),
                summary=f"{company_name} continues to show strong performance in the {industry} sector with new {category}-focused initiatives.",
                relevance_score=random.uniform(0.6, 1.0)
            ))
        
        # Generate regulatory filings
        for i in range(2):
            days_ago = random.randint(1, 180)
            filing_date = datetime.now() - timedelta(days=days_ago)
            
            filing_types = ["10K", "10Q", "proxy_statement", "press_release"]
            filing_type = random.choice(filing_types)
            
            filing_items.append(FilingItem(
                id=f"FIL_{company_name.split()[0]}_{i+1}",
                date=filing_date,
                type=filing_type.lower(),  # Ensure lowercase to match enum
                title=f"{company_name} {filing_type} filing Q{random.randint(1, 4)}",
                url=f"https://sec.gov/filings/{company_name.replace(' ', '')}_{filing_type}_{i+1}",
                key_points=[
                    f"Revenue growth in {random.choice(categories)} segment",
                    f"Investment in {industry}-specific solutions",
                    f"Compliance updates for {random.choice(categories)} regulations"
                ]
            ))
        
        return MarketIntelligenceResponse(
            company_name=company_name,
            recent_news=news_items,
            regulatory_filings=filing_items
        )

    def _find_product_by_name(self, product_name: str) -> ProductInfo:
        """Find and return product info by name"""
        product_data = next((p for p in self.products if p["name"] == product_name), None)
        if not product_data:
            # Default fallback
            product_data = self.products[0]
        
        features = [ProductFeature(name=f["name"], description=f["description"]) for f in product_data["features"]]
        
        spec = ProductSpec(
            category=product_data["category"],
            features=features,
            compliance_standards=product_data["compliance_standards"],
            target_industries=product_data["target_industries"],
            pricing_tier="professional"  # Default
        )
        
        case_studies = [
            CaseStudy(
                title=f"How {random.choice(self.customers)['name']} achieved success with {product_data['name']}",
                description=f"Detailed overview of successful implementation of {product_data['name']} at a {random.choice(self.customers)['industry']} company.",
                client_sector=random.choice(self.customers)['industry'],
                results=[f"Increased operational efficiency by {random.randint(20, 50)}%", 
                        f"Reduced costs by ${random.randint(100000, 1000000)} annually"]
            )
        ]
        
        return ProductInfo(
            product_name=product_data["name"],
            description=product_data["description"],
            specifications=spec,
            case_studies=case_studies,
            pricing=product_data["pricing"]
        )

    def get_crm_data(self, customer_name: str) -> CRMResponse:
        """Retrieve CRM data for a given customer"""
        if customer_name in self.customer_data_map:
            return self.customer_data_map[customer_name]["crm"]
        return None

    def get_engagement_data(self, customer_name: str) -> EngagementResponse:
        """Retrieve engagement data for a given customer"""
        if customer_name in self.customer_data_map:
            return self.customer_data_map[customer_name]["engagement"]
        return None

    def get_market_data(self, customer_name: str) -> MarketIntelligenceResponse:
        """Retrieve market data for a given customer"""
        if customer_name in self.customer_data_map:
            return self.customer_data_map[customer_name]["market"]
        return None

    def get_kb_data(self, product_name: str) -> ProductInfo:
        """Retrieve knowledge base data for a given product"""
        return self._find_product_by_name(product_name)

    def get_all_customers(self) -> List[str]:
        """Return list of all customer names"""
        return [c["name"] for c in self.customers]


# Initialize the generator
synthetic_data_generator = SyntheticDataGenerator()