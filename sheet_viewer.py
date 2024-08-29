import pandas as pd

def print_sheet(excel_stream):
    df = pd.read_excel(excel_stream, engine='openpyxl')
    print(df.head(8))

if __name__ == "__main__":
    # Load the Excel file
    df = pd.read_excel('sheet.xlsx')

    # Display the first few rows
    print(df.head())

