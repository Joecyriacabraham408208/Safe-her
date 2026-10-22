from flask import Flask, render_template, request
import pandas as pd
from src.optimization import optimize_allocation
from src.mapping import generate_heatmap

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('landing.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    budget = 77  
    status = "Ready"
    map_html = None
    
    if request.method == 'POST':
        budget = int(request.form.get('budget', 77))
        try:
            df = pd.read_csv("data/processed_district_risks.csv")
            optimized_df, status = optimize_allocation(df, budget)
            
            m = generate_heatmap(optimized_df) 
            
            # Checks if the map is already HTML text, or if it needs conversion
            if isinstance(m, str):
                map_html = m
            else:
                map_html = m._repr_html_()
                
        except Exception as e:
            status = f"Error: {str(e)}"
            
    return render_template('index.html', map_html=map_html, budget=budget, status=status)

if __name__ == '__main__':
    app.run(debug=True)