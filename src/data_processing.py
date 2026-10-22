import pandas as pd

def load_and_clean_data(filepath):
    cols_to_use = ['Date', 'Primary Type', 'Description', 'Domestic', 'District', 'Latitude', 'Longitude']
    df = pd.read_csv(filepath, usecols=cols_to_use)
    df = df.dropna(subset=['Latitude', 'Longitude', 'District'])
    return df

def process_risk_scores(df):
    target_crimes = ['CRIM SEXUAL ASSAULT', 'SEX OFFENSE', 'STALKING']
    safety_df = df[(df['Primary Type'].isin(target_crimes)) | (df['Domestic'] == True)]
    
    district_risk = safety_df.groupby('District').agg(
        Total_Incidents=('Primary Type', 'count'),
        Center_Lat=('Latitude', 'mean'),
        Center_Lon=('Longitude', 'mean')
    ).reset_index()
    
    max_incidents = district_risk['Total_Incidents'].max()
    district_risk['Risk_Score'] = (district_risk['Total_Incidents'] / max_incidents) * 100
    district_risk['Risk_Score'] = district_risk['Risk_Score'].astype(int)
    
    district_risk['Min_Req'] = 2 
    district_risk['Max_Cap'] = 15
    return district_risk

if __name__ == "__main__":
    raw_df = load_and_clean_data("data/chicago_crimes_raw.csv")
    clean_risk_df = process_risk_scores(raw_df)
    clean_risk_df.to_csv("data/processed_district_risks.csv", index=False)
    print("Data processing complete. Saved to data/processed_district_risks.csv")