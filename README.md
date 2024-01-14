# Google Search Console Data Downloader

## Installation

1. Clone the repository
2. Navigate to the project directory: `cd your_project`
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On Linux/Mac: `source venv/bin/activate`
5. Install dependencies: `pip install -r requirements.txt`

## Configuration

- **GSC_JSON_FILE:** Path to the directory containing the Google Search Console credentials JSON file.
- **OUTPUT_FILE_NAME:** Output CSV file name that will contain the downloaded data.

## Usage

1. Make sure you have the dependencies installed.
2. Place the Google Search Console credentials JSON file in the location specified by \`GSC_JSON_FILE\`.
3. Configure the execution parameters such as the domain (\`DOMAIN\`), the number of historical days (\`DAYS_AGO\`), and the credentials file name (\`CREDENTIALS_FILE_NAME\`).

### Running on Linux

4. Open a terminal and navigate to the script's directory.
5. Run the script:

```bash
python3 gsc_download_data.py
```

### Running on Windows

4. Open a Command Prompt or PowerShell and navigate to the script's directory.
5. Run the script:

```bash
python gsc_download_data.py
```
