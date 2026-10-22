import pandas as pd

def evaluate_model(df, total_officers):
    """
    Compares the mathematically optimized allocation against a uniform baseline allocation.
    """
    num_zones = len(df)
    if num_zones == 0:
        print("Error: No zones available to evaluate.")
        return 0
        
    # Baseline Scenario: Distribute officers equally across all zones 
    # (This represents the standard, non-data-driven approach)
    baseline_allocation = total_officers // num_zones 
    
    # Apply baseline to dataframe
    df['Baseline_Officers'] = baseline_allocation
    
    # Calculate how much "Risk" is mitigated by both methods
    df['Baseline_Risk_Mitigated'] = df['Baseline_Officers'] * df['Risk_Score']
    df['Optimized_Risk_Mitigated'] = df['Allocated_Officers'] * df['Risk_Score']
    
    # Sum up the total safety impact
    total_baseline_mitigation = df['Baseline_Risk_Mitigated'].sum()
    total_optimized_mitigation = df['Optimized_Risk_Mitigated'].sum()
    
    # Calculate the percentage improvement of your OR model
    if total_baseline_mitigation > 0:
        improvement = ((total_optimized_mitigation - total_baseline_mitigation) / total_baseline_mitigation) * 100
    else:
        improvement = 0
        
    print("\n--- Model Evaluation Results ---")
    print(f"Total Risk Mitigated (Uniform Baseline):  {total_baseline_mitigation}")
    print(f"Total Risk Mitigated (Optimized Model):   {total_optimized_mitigation}")
    print(f"Algorithm Improvement: {improvement:.2f}% better risk coverage using the exact same budget.")
    
    return improvement