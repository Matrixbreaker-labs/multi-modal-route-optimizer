# ===========================================================================
# 1. DEPENDENCY INITIALIZATION & ENVIRONMENT SETUP
# ===========================================================================
# Install official 2026 Google GenAI SDK and data rendering dependencies
!pip install --quiet google-genai pydantic pandas openpyxl tabulate

import os
import time
import pandas as pd
from typing import List, Literal, Optional
from pydantic import BaseModel, Field
from google import genai
from google.genai import types
from google.colab import userdata

# Initialize API Key safely from Google Colab Workspace Context Secrets
try:
    os.environ["GEMINI_API_KEY"] = userdata.get("GEMINI_API_KEY")
    print("[+] Gemini API Key successfully loaded from workspace secrets.")
except Exception:
    # Direct inline token assignment fallback for fast localized execution passes
    os.environ["GEMINI_API_KEY"] = "YOUR_RAW_GEMINI_API_KEY_HERE"
    print("[!] Warning: Runtime fallback triggered. Using inline fallback token bounds.")

# ===========================================================================
# 2. SCHEMA ARCHITECTURE (Type-Safe Supply Chain Mapping Constraints)
# ===========================================================================
class RouteOption(BaseModel):
    transport_mode: Literal["Air Freight", "Ocean Freight", "Rail", "Road"] = Field(description="The primary multi-modal transportation medium used.")
    carrier_name: str = Field(description="The logistics provider name (e.g., DHL, Maersk, FedEx).")
    estimated_cost_usd: float = Field(description="Total dynamic pricing quote for this specific route execution in USD.")
    transit_time_days: float = Field(description="Total projected time to complete the journey from origin to destination in days.")
    carbon_footprint_kg: float = Field(description="Estimated CO2 emissions associated with this specific logistics profile in kilograms.")

class OptimizationPayload(BaseModel):
    available_routes: List[RouteOption]

# ===========================================================================
# 3. AI COGNITIVE LOGISTICS ANALYSER NODE
# ===========================================================================
def fetch_live_carrier_quotes(origin: str, destination: str, cargo_weight_kg: float, client: genai.Client) -> Optional[OptimizationPayload]:
    """Simulates live multi-modal carrier API feeds using structural Gemini analysis."""
    prompt = f"""
    You are an advanced Multi-Modal Supply Chain Router. Synthesize live logistical pricing quotes and transit factors.
    Origin Location: {origin}
    Destination Location: {destination}
    Total Cargo Weight: {cargo_weight_kg} kg

    Generate exactly 4 distinct multi-modal route choices (Air Freight, Ocean Freight, Rail, Road) matching this transit lane.
    Calculate logical baseline values: Ocean Freight must be cheap but slow, Air Freight must be fast but expensive, etc.
    Convert all variables into numeric float data structures mapping exactly to the schema.
    """
    
    try:
        # Utilizing standard active production model endpoint for 2026 operations
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=OptimizationPayload,
                temperature=0.2 # Clamp temperature bounds to enforce deterministic matrix structure
            )
        )
        return OptimizationPayload.model_validate_json(response.text)
    except Exception as e:
        print(f"[-] AI Router Node Interruption Failure: {e}")
        return None

# ===========================================================================
# 4. OPTIMIZATION COMPILER ENGINE (Linear Scoring Protocol)
# ===========================================================================
def optimize_supply_chain_route(origin: str, destination: str, cargo_weight_kg: float):
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    
    print(f"[*] Booting Multi-Modal Carrier Route Optimizer Engine...")
    print(f"[*] Analyzing Transit Lane: {origin} ──> {destination} ({cargo_weight_kg} KG)\n")
    
    # Trigger structural extraction execution node
    route_payload = fetch_live_carrier_quotes(origin, destination, cargo_weight_kg, client)
    
    if not route_payload or not route_payload.available_routes:
        print("[-] Optimization halted: Carrier network matrix returned empty.")
        return
        
    processed_routes = []
    
    # Multi-Objective Optimizing Algorithm Matrix Parameters:
    # Linear Weight Metrics: 50% Operational Cost, 35% Transit Lead Speed, 15% Green Carbon Compliance
    for route in route_payload.available_routes:
        route_data = route.model_dump()
        
        # Lower vector index score represents higher optimization efficiency
        efficiency_score = (route.estimated_cost_usd * 0.50) + (route.transit_time_days * 30.0 * 0.35) + (route.carbon_footprint_kg * 0.15)
        route_data["efficiency_score"] = round(efficiency_score, 2)
        processed_routes.append(route_data)
        
    # Standardize data frames and sort matrix elements by top efficiency index
    df = pd.DataFrame(processed_routes)
    df = df.sort_values(by="efficiency_score").reset_index(drop=True)
    
    # Apply structural flag recommendations
    df['recommendation_flag'] = "Standard Route Choice"
    df.loc[df['estimated_cost_usd'].idxmin(), 'recommendation_flag'] = "🟢 CHEAPEST OPTIONS (Most Economical)"
    df.loc[df['transit_time_days'].idxmin(), 'recommendation_flag'] = "⚡ FASTEST OPTIONS (Time-Sensitive)"
    df.loc[df['efficiency_score'].idxmin(), 'recommendation_flag'] = "🏆 OPTIMAL ROUTE (Best Balanced Choice)"
    
    # Commit analytical dataset directly to disk workspace
    output_filename = "multi_modal_route_optimization.xlsx"
    df.to_excel(output_filename, index=False)
    
    print("="*75)
    print(f"[++] ROUTE MATRIX COMPILATION COMPLETE! Output locked at: {os.path.abspath(output_filename)}")
    print("="*75)
    print(df.to_markdown(index=False))

if __name__ == "__main__":
    # Test Lane Execution Parameters: Dhaka Factory to Hamburg Fulfillment Center
    optimize_supply_chain_route(
        origin="Dhaka, Bangladesh", 
        destination="Hamburg, Germany", 
        cargo_weight_kg=1250.00
    )
