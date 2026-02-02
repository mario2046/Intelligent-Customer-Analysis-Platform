# Customer 360 Data APIs

This project provides HTTP APIs for customer data including CRM, engagement, market intelligence, and knowledge base information. It serves as a data backend for the Customer 360 platform.

## Features

- **CRM API**: Customer profiles, sales history, and pipeline data
- **Engagement API**: Marketing event attendance and content engagement history
- **Market Intelligence API**: Industry news and market trends
- **Knowledge Base API**: Product information and case studies
- **Dummy Data**: Pre-populated with realistic customer archetypes

## API Endpoints

- `GET /crm/customer/{customer_name}` - Retrieve CRM data for a specific customer
- `GET /crm/customers` - Retrieve list of all available customers
- `GET /engagement/customer/{customer_name}/history` - Retrieve engagement history
- `GET /market/company/{company_name}/news` - Retrieve market intelligence
- `GET /kb/product/{product_name}` - Retrieve product information
- `GET /kb/products` - Retrieve list of all available products
- `GET /` - Welcome page with links to documentation
- `GET /health` - Health check endpoint

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd customer_360_data_apis
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Start the HTTP API server:

```bash
uvicorn main:app --reload
```

By default, the server runs on `http://localhost:8000`. If you encounter port conflicts, you can specify a different port:

```bash
uvicorn main:app --reload --port 8001
```

Alternatively, run the server directly with custom port:

```bash
python main.py --port 8080
```

Interactive API documentation is available at `/docs`.

## Available Customers

The system comes with 5 pre-generated customer archetypes:

- Acme Corp
- HealthPlus Hospitals
- FinSecure Inc.
- Global Manufacturing Ltd
- ShopEase Online

## Architecture

The system consists of four main components:

1. **CRM System**: Contains customer profiles, sales history, and pipeline data
2. **Engagement History**: Tracks marketing events attended and content downloaded by customers
3. **Market Intelligence**: Provides industry news and regulatory filings
4. **Knowledge Base**: Contains product information and case studies

## Customization

To adapt the system to your specific industry or use case:

1. Modify the Pydantic schemas in the `schemas/` directory to match your data structures
2. Update the synthetic data generator in `data/synthetic_generator.py` to create relevant customer profiles
3. Adjust the API endpoints in the `api/` directory to match your data sources

## Troubleshooting

- If you encounter port conflicts, try running the server on a different port (e.g., `--port 8001`)
- Check that all dependencies are properly installed in your virtual environment