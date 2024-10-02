# OCR_Scanner


Objective: Develop a system that scans mark sheets or rough sheets, extracts the data related to the total number of passed and failed students, and automatically populates this data into an Excel sheet.
Inputs:Scanned Image/PDF of Mark Sheets: A set of scanned images or PDF files containing the mark sheets of students.
Criteria for Passing/Failing: The conditions or thresholds that determine whether a student has passed or failed.
Outputs:Excel Sheet: An Excel file containing the total number of passed and failed students, organized in a structured format.

Technologies Used:
Optical Character Recognition (OCR): To convert scanned images or PDFs into text. (e.g., Tesseract OCR)
Python: For processing the OCR output and analyzing the data.
Excel Libraries: To create and manage Excel files. (e.g. pandas)

Software Used:
Tesseract OCR: For converting scanned images or PDFs into text.
Python: Used for processing the OCR output and analyzing the data.
Libraries:
pdfplumber (for extracting text and tables from PDFs).
pytesseract (for handling OCR tasks with Tesseract).
pandas (for data manipulation and managing Excel files).
Flask: For creating a web interface (if needed) to manage file uploads and display results.
