import pandas as pd
import pdfplumber

def convert_to_excel(pdf_path, excel_path):
    all_rows = []
    
    # Open the PDF and iterate through each page
    with pdfplumber.open(pdf_path) as pdf:
        for page_num in range(len(pdf.pages)):
            page = pdf.pages[page_num]
            table = page.extract_table()

            if table:
                # On the first page, capture the headers
                if page_num == 0:
                    headers = table[0]
                    rows = table[1:]
                else:
                    # Subsequent pages should only capture rows, not headers
                    rows = table
                
                # Split data if all columns are in one column (as done earlier)
                if len(headers) == 1 and rows:
                    split_data = [row[0].split() for row in rows]
                    if len(split_data[0]) == 2:
                        if page_num == 0:  # Define headers only once, on the first page
                            headers = ['Student enroll', 'Marks']
                        rows = split_data
                    else:
                        raise ValueError("Unable to split data into columns.")
                
                # Append rows from the current page
                all_rows.extend(rows)

    if not all_rows:
        raise ValueError("No table data found in the PDF.")
    
    # Create a DataFrame with the collected rows
    df = pd.DataFrame(all_rows, columns=headers)
    
    # Convert columns to numeric where appropriate
    for col in df.columns[1:]:  # Assuming first column is names/identifiers
        df[col] = pd.to_numeric(df[col], errors='coerce')
    
    # Calculate "Total Percentage" if needed (you can modify this part based on requirements)
    if len(df.columns) == 1:
        df['Total Percentage'] = df[df.columns[0]]  # Use the only column as percentage
    else:
        df['Total Percentage'] = df[df.columns[1:]].sum(axis=1) / len(df.columns[1:])
    
    # Save the data to an Excel file
    df.to_excel(excel_path, index=False)

    return excel_path
