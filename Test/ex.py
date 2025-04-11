import csv

def printSpecIt(file_path, row_index=None, column_index=None, column_name=None):
    """
    Prints specific items from a CSV file based on row index, column index, or column name.

    Args:
        file_path (str): The path to the CSV file.
        row_index (int, optional): The index of the row to print. Defaults to None.
        column_index (int, optional): The index of the column to print. Defaults to None.
        column_name (str, optional): The name of the column to print. Defaults to None.
    """
    try:
        with open(file_path, 'r') as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)
            
            if row_index is not None:
                for i, row in enumerate(csv_reader):
                    if i == row_index:
                        if column_index is not None:
                            print(row[column_index])
                        elif column_name is not None:
                            try:
                                column_index = header.index(column_name)
                                print(row[column_index])
                            except ValueError:
                                print(f"Column '{column_name}' not found.")
                        else:
                            print(row)
                        return
                print(f"Row index {row_index} not found.")

            elif column_index is not None:
                for row in csv_reader:
                    print(row[column_index])
            
            elif column_name is not None:
                try:
                    column_index = header.index(column_name)
                    for row in csv_reader:
                        print(row[column_index])
                except ValueError:
                     print(f"Column '{column_name}' not found.")
            
            else:
                 for row in csv_reader:
                    print(row)
    
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except IndexError:
        print("Index out of range.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = 'Test/demofile.csv'

print("Print all data:")
printSpecIt(file_path)

print("\nPrint row at index 1:")
printSpecIt(file_path, row_index=1)

print("\nPrint item at row index 0 and column index 2:")
printSpecIt(file_path, row_index=0, column_index=2)

print("\nPrint column with name 'Name':")
printSpecIt(file_path, column_name="Name")

print("\nPrint item at row index 2 and column name 'Age':")
printSpecIt(file_path, row_index=2, column_name="Age")

print("\nPrint column at index 1:")
printSpecIt(file_path, column_index=1)