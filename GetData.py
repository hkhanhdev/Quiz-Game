import json
import requests

def fetch_questions_from_apis(api_url,params):
    response = requests.get(api_url,params=params)

    if response.status_code == 200:
        questions_data = response.json()
        return questions_data
    else:
        print(f"Failed to fetch questions. Status code: {response.status_code}")
        return None

def save_questions_to_storage(questions, json_file_path):
    with open(json_file_path, 'w') as json_file:
        json.dump(questions, json_file, indent=4)

def fetch_questions_from_storage(json_file_path):
    with open(json_file_path,'r') as json_file:
        content = json.load(json_file)
        return content






