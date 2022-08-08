# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
from pathlib import Path

def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

def save_csv(data):
    # Saves the CSV file to path provided
    # Args: 
        # data: list of qualifying loans

    bank_data = data

    #Headers for output file
    header = ["lender", "Max Loan Amount", "Max_Loan_Amount", "Max LTV", "Max DTI" ," Min Credit Score", "Interest Rate"]
    
    # create new csv file in write mode and write data from qualifying loans
    csvpath = Path("qualifying_loans.csv")

    with open(csvpath, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter = ",")
        csvwriter.writerow(header)
        for row in bank_data:
            csvwriter.writerow(row)
    return data

