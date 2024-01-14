# Google Search Console Data Downloader

## Description

This Python script utilizes the Google Search Console API to download search performance data and save it to a CSV file. The script allows specifying the domain, the number of historical days of data to retrieve, and the credentials file name.

## Requirements

- Python
- Required libraries: \`google-auth\`, \`google-auth-oauthlib\`, \`google-auth-httplib2\`, \`google-api-python-client\`

You can install the dependencies by running:
\`\`\`
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
\`\`\`

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
   \`\`\`
   python3 gsc_download_script.py
   \`\`\`

### Running on Windows

4. Open a Command Prompt or PowerShell and navigate to the script's directory.
5. Run the script:
   \`\`\`
   python gsc_download_script.py
   \`\`\`
