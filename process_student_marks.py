import pandas as pd
from tkinter import Tk, filedialog

# Initialize Tkinter
root = Tk()
root.withdraw()  # Hide the main window

# Open file dialog to select the file
file_path = filedialog.askopenfilename(
    title="Select the Excel file",
    filetypes=[("Excel files", "*.xlsx")]
)

# Check if the file path is valid
if file_path:
    # Load the data from the selected file
    df = pd.read_excel(file_path)

    # Check if the necessary columns are present
    if 'Marks' in df.columns:
        # Determine Pass/Fail
        df['Status'] = df['Marks'].apply(lambda x: 'Pass' if x >= 22 else 'Fail')

        # Save the result to a new Excel file
        output_file = 'student_results.xlsx'
        df.to_excel(output_file, index=False)

        print(f"Results have been saved to {output_file}")
    else:
        print("The selected file does not contain the required columns.")
else:
    print("No file was selected. Exiting.")
