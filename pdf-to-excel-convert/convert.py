import tabula
import pandas as pd

# Define your file name
pdf_file = "https___www.iebc.or.ke_docs_rov_per_polling_station.pdf" # Change this to your filename

print("Starting conversion... This may take a minute for 700 pages.")

# Step 1: Read the PDF
# 'pages="all"' tells the script to scan every page
# 'multiple_tables=True' handles cases where pages have different table layouts
tables = tabula.read_pdf(pdf_file, pages='all', multiple_tables=True)

# Step 2: Combine all tables into one single DataFrame
# Sometimes one table spans multiple pages; this stitches them together
df = pd.concat(tables)

# Step 3: Export to Excel
output_file = "meru-county-polling-data.xlsx"
df.to_excel(output_file, index=False)

print(f"Success! Your file is ready: {output_file}")