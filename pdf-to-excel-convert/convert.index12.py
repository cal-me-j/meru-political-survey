import tabula
import pandas as pd

pdf_file = "https___www.iebc.or.ke_docs_rov_per_polling_station.pdf" 

print("Reading PDF...")
tables = tabula.read_pdf(pdf_file, pages='all', multiple_tables=True)
df = pd.concat(tables)

# --- NEW FILTERING STEP ---
# This keeps only rows where the index is 12
df_filtered = df[df.iloc[:, 11].astype(str) == "12"] 
# --------------------------

print("Saving to Excel...")
output_file = "meru-data-county-code-12.xlsx"
df_filtered.to_excel(output_file, index=True) # Keep index=True to see the '12'

print(f"Done! Saved to {output_file}")