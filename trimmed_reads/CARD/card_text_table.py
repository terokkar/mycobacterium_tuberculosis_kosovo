import pandas as pd
from textwrap import wrap

# Load the CARD results
df = pd.read_csv("kosovo_trimmed_CARD.fasta.txt", sep="\t")

# Select relevant columns
columns = ["Best_Hit_ARO", "Drug Class", "Resistance Mechanism", "Model_type", "Best_Identities", "Antibiotic"]
df = df[columns]

# Rename columns for display
df.columns = ["Gene", "Drug Class", "Mechanism", "Model", "%ID", "Antibiotics"]

# Optional: round identity
df["%ID"] = df["%ID"].round(1)

# Truncate antibiotics and wrap drug class for readability
def wrap_field(val, width=40):
    return '\n'.join(wrap(str(val), width=width))

df["Drug Class"] = df["Drug Class"].apply(lambda x: wrap_field(x, 40))
df["Antibiotics"] = df["Antibiotics"].apply(lambda x: wrap_field(x, 40))

# Convert to plain-text table
for index, row in df.iterrows():
    print("=" * 60)
    print(f"Gene:        {row['Gene']}")
    print(f"Drug Class:  {row['Drug Class']}")
    print(f"Mechanism:   {row['Mechanism']}")
    print(f"Model:       {row['Model']}")
    print(f"% Identity:  {row['%ID']}%")
    print(f"Antibiotics: {row['Antibiotics']}")
    print("=" * 60 + "\n")