import requests
import json

def get_latest_samples():
    url = "https://mb-api.abuse.ch/api/v1/"
    data = {
        'query': 'get_recent',
        'selector': 'time'  # Fetching samples from the past 60 minutes
    }
    
    response = requests.post(url, data=data)
    
    if response.status_code == 200:
        response_data = response.json()
        if response_data.get('query_status') == 'ok' and 'data' in response_data:
            return response_data['data']
        else:
            print(f"API response issue: {response_data.get('query_status')}")
            return []
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return []

def save_to_json(samples):
    desired_keys = ["file_name", "first_seen", "last_seen", "sha256_hash", "sha1_hash", "md5_hash"]
    filtered_samples = []
    
    for sample in samples:
        filtered_sample = {key: sample[key] for key in desired_keys if key in sample}
        filtered_samples.append(filtered_sample)
    
    with open("malware_samples.json", "w") as file:
        json.dump(filtered_samples, file, indent=4)

def main():
    samples = get_latest_samples()
    if samples:
        save_to_json(samples)
        print("Samples saved to 'malware_samples.json'.")

if __name__ == "__main__":
    main()
