import pulp
import pandas as pd

def optimize_allocation(df, total_officers_budget):
    model = pulp.LpProblem("Police_Allocation_Optimization", pulp.LpMaximize)
    districts = df['District'].astype(str).tolist()

    risk_scores = dict(zip(districts, df['Risk_Score']))
    min_reqs = dict(zip(districts, df['Min_Req']))
    max_caps = dict(zip(districts, df['Max_Cap']))

    # FIXED: Positional arguments only
    x = {i: pulp.LpVariable(f"Officers_{i}", 0, None, pulp.LpInteger) for i in districts}

    model += pulp.lpSum([risk_scores[i] * x[i] for i in districts]), "Total_Risk_Mitigated"
    model += pulp.lpSum([x[i] for i in districts]) <= total_officers_budget, "Budget_Constraint"

    for i in districts:
        model += x[i] >= min_reqs[i], f"Min_Coverage_{i}"
        model += x[i] <= max_caps[i], f"Max_Capacity_{i}"

    model.solve()

    allocation_results = []
    for i in districts:
        if x[i].varValue is not None:
            allocation_results.append(int(x[i].varValue))
        else:
            allocation_results.append(0)

    df['Allocated_Officers'] = allocation_results
    return df, pulp.LpStatus[model.status]