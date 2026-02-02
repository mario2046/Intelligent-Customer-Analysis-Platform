# Customer Archetypes
CUSTOMER_ARCHETYPES = [
    {
        "name": "Acme Corp",
        "industry": "Technology",
        "size": "enterprise",
        "region": "North America",
        "primary_interest": "cloud_security",
        "annual_revenue_range": (1000000000, 5000000000),
        "contact_info": {
            "person": "John Smith",
            "email": "john.smith@acmecorp.com",
            "phone": "+1-555-0101"
        }
    },
    {
        "name": "HealthPlus Hospitals",
        "industry": "Healthcare",
        "size": "enterprise",
        "region": "North America",
        "primary_interest": "compliance_solutions",
        "annual_revenue_range": (500000000, 2000000000),
        "contact_info": {
            "person": "Sarah Johnson",
            "email": "s.johnson@healthplus.org",
            "phone": "+1-555-0102"
        }
    },
    {
        "name": "FinSecure Inc.",
        "industry": "Financial Services",
        "size": "enterprise",
        "region": "Europe",
        "primary_interest": "fraud_detection",
        "annual_revenue_range": (2000000000, 8000000000),
        "contact_info": {
            "person": "Michael Chen",
            "email": "m.chen@finsecure.com",
            "phone": "+44-20-1234-5678"
        }
    },
    {
        "name": "Global Manufacturing Ltd",
        "industry": "Manufacturing",
        "size": "enterprise",
        "region": "Asia Pacific",
        "primary_interest": "operational_efficiency",
        "annual_revenue_range": (1500000000, 6000000000),
        "contact_info": {
            "person": "Yuki Tanaka",
            "email": "y.tanaka@globamanuf.co.jp",
            "phone": "+81-3-1234-5678"
        }
    },
    {
        "name": "ShopEase Online",
        "industry": "E-commerce",
        "size": "mid_market",
        "region": "North America",
        "primary_interest": "scalability_solutions",
        "annual_revenue_range": (50000000, 500000000),
        "contact_info": {
            "person": "Emma Rodriguez",
            "email": "emma@shopease.com",
            "phone": "+1-555-0103"
        }
    }
]

# Products
PRODUCTS = [
    {
        "name": "Cloud Security Suite",
        "description": "Comprehensive security solution for cloud environments",
        "category": "security",
        "features": [
            {"name": "Threat Detection", "description": "Real-time monitoring for threats"},
            {"name": "Encryption", "description": "End-to-end encryption protocols"},
            {"name": "Access Control", "description": "Role-based access management"}
        ],
        "compliance_standards": ["SOC 2", "GDPR", "HIPAA"],
        "target_industries": ["Technology", "Healthcare", "Financial Services"],
        "pricing": {
            "basic": {"price": 1000, "features": ["Threat Detection"]},
            "professional": {"price": 5000, "features": ["Threat Detection", "Encryption"]},
            "enterprise": {"price": 15000, "features": ["Threat Detection", "Encryption", "Access Control"]}
        }
    },
    {
        "name": "Compliance Management Pro",
        "description": "Complete compliance solution for regulated industries",
        "category": "compliance",
        "features": [
            {"name": "Audit Trail", "description": "Complete audit logging"},
            {"name": "Policy Management", "description": "Centralized policy controls"},
            {"name": "Reporting", "description": "Regulatory reporting tools"}
        ],
        "compliance_standards": ["SOX", "HIPAA", "PCI-DSS"],
        "target_industries": ["Healthcare", "Financial Services", "Government"],
        "pricing": {
            "basic": {"price": 1500, "features": ["Audit Trail"]},
            "professional": {"price": 7000, "features": ["Audit Trail", "Policy Management"]},
            "enterprise": {"price": 20000, "features": ["Audit Trail", "Policy Management", "Reporting"]}
        }
    },
    {
        "name": "Fraud Detection AI",
        "description": "Advanced AI-powered fraud detection system",
        "category": "security",
        "features": [
            {"name": "Anomaly Detection", "description": "ML-based anomaly detection"},
            {"name": "Behavioral Analysis", "description": "User behavior profiling"},
            {"name": "Real-time Alerts", "description": "Instant fraud alerts"}
        ],
        "compliance_standards": ["PCI-DSS", "GDPR"],
        "target_industries": ["Financial Services", "E-commerce", "Insurance"],
        "pricing": {
            "basic": {"price": 2000, "features": ["Anomaly Detection"]},
            "professional": {"price": 8000, "features": ["Anomaly Detection", "Behavioral Analysis"]},
            "enterprise": {"price": 25000, "features": ["Anomaly Detection", "Behavioral Analysis", "Real-time Alerts"]}
        }
    },
    {
        "name": "Operational Efficiency Suite",
        "description": "Optimization tools for operational efficiency",
        "category": "efficiency",
        "features": [
            {"name": "Process Automation", "description": "Workflow automation tools"},
            {"name": "Resource Optimization", "description": "Resource allocation optimization"},
            {"name": "Analytics", "description": "Performance tracking and analytics"}
        ],
        "compliance_standards": [],
        "target_industries": ["Manufacturing", "Logistics", "Retail"],
        "pricing": {
            "basic": {"price": 800, "features": ["Process Automation"]},
            "professional": {"price": 4000, "features": ["Process Automation", "Resource Optimization"]},
            "enterprise": {"price": 12000, "features": ["Process Automation", "Resource Optimization", "Analytics"]}
        }
    },
    {
        "name": "Scalability Solutions Pro",
        "description": "Infrastructure solutions for scaling applications",
        "category": "infrastructure",
        "features": [
            {"name": "Auto-scaling", "description": "Automatic resource scaling"},
            {"name": "Load Balancing", "description": "Traffic distribution across servers"},
            {"name": "CDN Integration", "description": "Content delivery network support"}
        ],
        "compliance_standards": ["SOC 2", "ISO 27001"],
        "target_industries": ["E-commerce", "SaaS", "Media"],
        "pricing": {
            "basic": {"price": 1200, "features": ["Auto-scaling"]},
            "professional": {"price": 6000, "features": ["Auto-scaling", "Load Balancing"]},
            "enterprise": {"price": 18000, "features": ["Auto-scaling", "Load Balancing", "CDN Integration"]}
        }
    }
]

# Engagement categories by industry
ENGAGEMENT_CATEGORIES = {
    "Technology": ["security", "cloud", "devops"],
    "Healthcare": ["compliance", "data privacy", "ehr systems"],
    "Financial Services": ["fraud prevention", "regulation", "risk management"],
    "Manufacturing": ["automation", "supply chain", "quality control"],
    "E-commerce": ["scalability", "user experience", "payment processing"]
}

# Market news categories by industry
NEWS_CATEGORIES = {
    "Technology": ["expansion", "funding", "partnership", "product launch"],
    "Healthcare": ["regulatory approval", "merger", "healthcare policy", "digital transformation"],
    "Financial Services": ["regulation change", "merger", "fintech innovation", "market trends"],
    "Manufacturing": ["supply chain", "automation", "sustainability", "trade policy"],
    "E-commerce": ["market expansion", "logistics", "consumer behavior", "digital payments"]
}
