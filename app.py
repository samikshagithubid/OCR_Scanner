from flask import Flask, request, render_template, send_from_directory
import os
from werkzeug.utils import secure_filename
from pdf_to_excel import convert_to_excel
from excel_processing import process_excel

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['pdf_file']
        pass_threshold = request.form.get('pass_threshold', default=22, type=int)

        if file and file.filename.endswith('.pdf'):
            filename = secure_filename(file.filename)
            pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(pdf_path)

            # Convert PDF to Excel
            excel_filename = 'converted_' + filename.replace('.pdf', '.xlsx')
            excel_path = os.path.join(app.config['UPLOAD_FOLDER'], excel_filename)

            try:
                convert_to_excel(pdf_path, excel_path)

                # Process the Excel file with the user-defined pass threshold
                df, passed_df, failed_df, passed, failed, pass_percentage, fail_percentage = process_excel(excel_path, pass_threshold)

                # Save the processed Excel files
                processed_filename = 'processed_' + excel_filename
                processed_path = os.path.join(app.config['UPLOAD_FOLDER'], processed_filename)
                df.to_excel(processed_path, index=False)

                passed_filename = 'passed_' + excel_filename
                passed_path = os.path.join(app.config['UPLOAD_FOLDER'], passed_filename)
                passed_df.to_excel(passed_path, index=False)

                failed_filename = 'failed_' + excel_filename
                failed_path = os.path.join(app.config['UPLOAD_FOLDER'], failed_filename)
                failed_df.to_excel(failed_path, index=False)

                return render_template('results.html', passed=passed, failed=failed,
                                       pass_percentage=pass_percentage, fail_percentage=fail_percentage,
                                       total_file=processed_filename, passed_file=passed_filename, failed_file=failed_filename)
            except Exception as e:
                return str(e)

    return render_template('index.html')


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
