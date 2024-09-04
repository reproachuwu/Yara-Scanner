# Yara-Scanner

Yara-Scanner is a Python script that empowers you to perform comprehensive YARA rule scans across your entire system. Simply provide a starting file path, and Yara-Scanner will diligently traverse your file system, applying YARA rules defined in 'yara.yar' to identify potential matches. 

## Features

* **Thorough Scanning:** Recursively walks through directories and subdirectories from the specified starting path.
* **Customizable Rules:**  Leverages YARA rules defined in 'yara.yar', allowing you to tailor scans to your specific needs.
* **Concise Results:** Presents clear and organized scan results, highlighting any YARA rule matches.
* **User-Friendly:**  Simple command-line interface for easy interaction.

## Requirements

* **Python:** Python 3.x is required to run this script.
* **yara-python:** Install the `requirements` library using pip: `pip install -r requirements.txt`
* **YARA Rules:** Create a 'yara.yar' file containing your desired YARA rules.

## Usage

1. **Clone the Repository:**
   ```bash
   git clone [invalid URL removed]
   cd Yara-Scanner
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Script:**
   ```bash
   python main.py
   ```

4. **Provide Path:**
   Enter the base path where you want to start the scan when prompted.