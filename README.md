# Multi-Modal Carrier Route Optimization API Integrator

An intelligent Supply Chain Management (SCM) optimization engine engineered to evaluate global freight transit networks. The pipeline dynamically ingests logistics vectors via the Google GenAI SDK [†], wraps payload parameters inside strict type-safe Pydantic verification layers, and processes a multi-objective linear scoring protocol to instantly flag the most carbon-efficient, lowest-cost, and fastest transportation routes.

---

## 🛠️ Tech Stack & Key Capabilities
* **Zero-Regex Architecture:** Eliminates fragile text-parsing exceptions by enforcing rigid JSON schemas.
* **Multi-Objective Optimizing Engine:** Automatically evaluates trade-offs across competing logistics variables (50% Cost, 35% Transit Lead Time, 15% Carbon Footprint).
* **Automated Decision Marking:** Intelligently tags and highlights discrete operational rows as `🏆 OPTIMAL ROUTE`, `⚡ FASTEST OPTIONS`, or `🟢 CHEAPEST OPTIONS`.

---

## 📊 Live Pipeline Execution Results (Dhaka ──> Hamburg)

Upon running the execution pipeline for a **1,250 KG Cargo Load** moving from the Dhaka Factory to the Hamburg Fulfillment Center, the system generated the following structured relational matrix:

| transport_mode | carrier_name | estimated_cost_usd | transit_time_days | carbon_footprint_kg | efficiency_score | recommendation_flag |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Ocean Freight | Maersk | 1200.00 | 28.0 | 450.0 | 961.50 | 🟢 CHEAPEST OPTIONS (Most Economical) |
| Rail | DB Cargo | 2400.00 | 16.0 | 620.0 | 1461.00 | 🏆 OPTIMAL ROUTE (Best Balanced Choice) |
| Road | DHL Global | 3100.00 | 12.0 | 980.0 | 1823.00 | Standard Route Choice |
| Air Freight | FedEx Priority | 6800.00 | 3.0 | 4200.0 | 4126.50 | ⚡ FASTEST OPTIONS (Time-Sensitive) |

### 💻 System Operational Telemetry Logs:
```text
[*] Booting Multi-Modal Carrier Route Optimizer Engine...
[*] Analyzing Transit Lane: Dhaka, Bangladesh ──> Hamburg, Germany (1250.00 KG)

[+] Gemini API Key successfully loaded from workspace secrets.
[+] AI Router Node Execution: Data parsed successfully via LLM (Latency: 2.14s)

===========================================================================
[++] ROUTE MATRIX COMPILATION COMPLETE! Output locked at: /content/multi_modal_route_optimization.xlsx
===========================================================================
```

---

## 🚀 Getting Started & Local Deployment

### 1. Resolve System Dependencies
Ensure Python 3.8+ is mapped onto your environment terminal spaces. Install the core operational matrices packages:
```bash
pip install google-genai pydantic pandas openpyxl tabulate
```

### 2. Set Up Context Credentials & Run
Configure your environment context tokens and launch the primary execution engine runtime node:
```bash
export GEMINI_API_KEY="your_api_key_here"
python main.py
```
