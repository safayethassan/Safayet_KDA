import openpyxl

def generate_report(results):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.append(["Step", "Result"])

    for step, result in results:
        sheet.append([step, result])

    workbook.save("reports/test_report.xlsx")