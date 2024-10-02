import pandas as pd

def process_excel(file_path, pass_threshold):
    # Load the Excel file
    df = pd.read_excel(file_path)
    
    # Print DataFrame and columns for debugging
    print("DataFrame Columns:", df.columns)
    print("First few rows of DataFrame:\n", df.head())

    # Verify "Marks" column exists
    marks_column = 'Marks'
    if marks_column not in df.columns:
        raise ValueError(f"Column '{marks_column}' not found in the Excel file.")
    
    # Convert the specified column to numeric
    df[marks_column] = pd.to_numeric(df[marks_column], errors='coerce')
    
    # Debugging output
    print("DataFrame with 'Marks':\n", df)

    # Determine pass/fail based on the provided threshold
    df['Status'] = df[marks_column].apply(lambda x: 'Pass' if x >= pass_threshold else 'Fail')
    
    # Debugging output
    print("DataFrame with 'Status':\n", df)

    # Calculate pass/fail statistics
    total_students = len(df)
    passed_students = len(df[df['Status'] == 'Pass'])
    failed_students = len(df[df['Status'] == 'Fail'])
    
    pass_percentage = (passed_students / total_students) * 100 if total_students > 0 else 0
    fail_percentage = (failed_students / total_students) * 100 if total_students > 0 else 0
    
    # Create separate DataFrames for passed and failed students
    passed_df = df[df['Status'] == 'Pass']
    failed_df = df[df['Status'] == 'Fail']
    
    return df, passed_df, failed_df, passed_students, failed_students, pass_percentage, fail_percentage
