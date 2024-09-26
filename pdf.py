#import weasyprint

# Convert HTML report to PDF
# The following line reads the 'report.html' file and converts it to a PDF file named 'report.pdf'
#weasyprint.HTML('report.html').write_pdf('report.pdf')
import os
from playwright.sync_api import sync_playwright

directory_path = 'F:/TRAININGS-RECORDING-ALL/SANJEEV-PYTEST/'

# List all files in the directory
files = os.listdir(directory_path)
print("Files in directory:", files)

def html_to_pdf():
    # Verify if the file exists
    file_path = 'F:/TRAININGS-RECORDING-ALL/SANJEEV-PYTEST/reports/report.html'
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        # Provide the correct absolute path to your report.html
        page.goto(f'file:///{file_path}')
        page.pdf(path='report.pdf')  # Save the PDF output
        browser.close()

if __name__ == "__main__":
    html_to_pdf()