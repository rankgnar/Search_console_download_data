from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import json
import os
import csv
import datetime


GSC_JSON_FILE = "path/to/gsc/json/files"
OUTPUT_FILE_NAME = "output.csv"


def prepare_credentials_gsc(credentials_file_name):
    oauth_json_file = os.path.join(GSC_JSON_FILE, credentials_file_name)
    with open(oauth_json_file, 'r') as json_file:
        creds = json.load(json_file)
    creds = Credentials.from_authorized_user_info(creds)
    return creds


def create_webmasters_service(creds):
    return build('webmasters', 'v3', credentials=creds)


def download_data_gsc(credentials_file_name, domain, days_ago=7):
    creds = prepare_credentials_gsc(credentials_file_name)
    service = create_webmasters_service(creds)
    data = get_data_gsc(service, domain, days_ago)
    save_data(data)


def get_data_gsc(service, domain, days_ago):
    request = {
        'startDate': (datetime.date.today() - datetime.timedelta(days_ago)).strftime('%Y-%m-%d'),
        'endDate': datetime.date.today().strftime('%Y-%m-%d'),
        'dimensions': ['query', 'page'],
        'rowLimit': 5000
    }
    response = service.searchanalytics().query(siteUrl=domain, body=request).execute()

    if 'rows' not in response:
        print('No data')
        return []

    return response["rows"]


def save_data(data):
    columns = ['URL', 'Keyword', 'Clicks', 'Impressions', 'CTR', 'Position']
    processed_data = process_data_gsc(data, columns)
    output_file_path = os.path.join(GSC_JSON_FILE, OUTPUT_FILE_NAME)
    with open(output_file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(columns)
        writer.writerows(processed_data)


def process_data_gsc(rows, columns):
    processed_data = []
    for row in rows:
        new_row = [
            row['keys'][1] if len(row['keys']) > 1 else '',
            row['keys'][0] if len(row['keys']) > 0 else '',
            int(row['clicks']),
            int(row['impressions']),
            round(float(row['ctr']) * 100, 2),
            round(float(row['position']), 2)
        ]
        processed_data.append(new_row)
    return processed_data

# Execute data download
DOMAIN = "example.com"  # Replace with your domain
DAYS_AGO = 7  # Replace with the number of days ago you want
CREDENTIALS_FILE_NAME = "your_credentials_file.json"  # Replace with your credentials file
download_data_gsc(CREDENTIALS_FILE_NAME, DOMAIN, DAYS_AGO)
