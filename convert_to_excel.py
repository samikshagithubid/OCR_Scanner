import pdfplumber
import pandas as pd

def process_pdf(pdf_path, pass_threshold):
    all_data = []
    
    with pdfplumber.open(pdf_path) as pdf:
        total_pages = len(pdf.pages)
        for page_num in range(total_pages):  # Iterate through all pages in the PDF
            page = pdf.pages[page_num]
            print(f"Processing page {page_num+1}")
            
            # Try to extract tables from the page
            table = page.extract_table()
            if table:
                print(f"Table found on page {page_num+1}")
                for row in table[1:]:  # Skip the header row
                    if len(row) >= 2:
                        enroll, marks = row[0], row[1]
                        try:
                            marks = int(marks)
                        except ValueError:
                            continue  # Skip rows with invalid marks
                        
                        # Determine pass/fail based on the threshold
                        status = "Pass" if marks >= pass_threshold else "Fail"
                        all_data.append([enroll, marks, marks, status])
    
    # Convert to DataFrame
    df = pd.DataFrame(all_data, columns=['Student Enrollment', 'Marks', 'Total Percentage', 'Status'])
    
    return df

# Example usage
pdf_path = 'sheet_marks.pdf'  # Path to your PDF file
pass_threshold = 30 # Set your desired threshold here
result_df = process_pdf(pdf_path, pass_threshold)
print(table)
# Output or save the result to an Excel file
result_df.to_excel("processed_results.xlsx", index=False)