
📊 CSV Editor & Calculator

A Python-based GUI application using Tkinter that allows users to load, view, edit, and perform calculations on CSV files. The app is ideal for quick statistical analysis and manipulation of CSV data without needing spreadsheet software.
Features

    Load & View CSV: Open a .csv file and view its contents in multiple synchronized listboxes, each representing a column.

    Save CSV: Save your modified CSV data back to disk.

    Calculate Values: Perform column-based statistical calculations:

        sum: Total of the values

        avg / mean: Average value

        stddev: Standard deviation

        maxdelta: Maximum difference between consecutive entries

        mindelta: Minimum difference between consecutive entries

        charcalc: Custom character range arithmetic (e.g., "16 to 61")

    Find & Replace: Replace strings across the entire CSV file.

    View History: See a log of all performed calculations stored in calculation_history.txt.

    All Calculations: Run all supported calculations on all numeric columns and generate a full report saved to calculation_report.txt.


Interface

    Built with tkinter and uses Listbox widgets to display each CSV column.

    Uses simpledialog for user input and messagebox for feedback.

Data Handling

    CSV data is loaded into memory (self.csv_data) as a list of rows.

    Displayed in columnar format by transposing rows into individual Listbox widgets.

    Scroll synchronization is handled across all columns.
    Notes:
    Indexing is zero-based (i.e., column 0 is the first column).

    Make sure the target column contains numeric values if using statistical calculations.

The application currently does not support CSV files with inconsistent row lengths.
