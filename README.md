# OptiGuard: AI-Powered Police Resource Allocation

OptiGuard is a dynamic Operations Research web dashboard designed to optimize police deployments across city districts. By leveraging Integer Linear Programming (ILP), the system mathematically maximizes risk mitigation while adhering to strict personnel budgets and baseline coverage constraints.

## Features
* **Dynamic Budgeting:** Interactive sliders allow users to input total available police force capacity in real-time.
* **ILP Optimization Engine:** Guarantees mathematically optimal, non-fractional officer assignments without exceeding budget constraints.
* **Geospatial Intelligence:** Generates an interactive Folium heatmap to visualize critical risk hotspots (Red/Orange) versus baseline safety zones (Blue/Green).
* **Responsive Architecture:** Built with a two-page Flask architecture, featuring a high-contrast, modern UI (Glassmorphism) optimized for readability.

## Tech Stack
* **Backend:** Python, Flask, Pandas
* **Optimization:** PuLP (Integer Linear Programming)
* **Frontend:** HTML5, CSS3, Bootstrap 5
* **Mapping:** Folium
* **Deployment:** Gunicorn, Render

## Project Structure
```text
optiguard-dashboard/
│── app.py                        # Main Flask application and routing
│── requirements.txt              # Production dependencies
│── data/
│   └── processed_district_risks.csv # Core dataset
│── src/
│   ├── optimization.py           # ILP algorithm logic
│   └── mapping.py                # Folium heatmap generation
│── static/
│   └── style.css                 # Custom CSS and dark theme rendering
└── templates/
    ├── landing.html              # Explanatory home page
    └── index.html                # Interactive map dashboard