import requests

class CrewAIResearch:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://api.crewai.co'

    def send_research_request(self, query):
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        payload = {
            'query': query
        }
        response = requests.post(f'{self.base_url}/research', headers=headers, json=payload)
        return response.json()

    def get_research_result(self, request_id):
        headers = {
            'Authorization': f'Bearer {self.api_key}'
        }
        response = requests.get(f'{self.base_url}/research/{request_id}', headers=headers)
        return response.json()

# Example usage:
# api_key = 'your_api_key_here'
# research_client = CrewAIResearch(api_key)
# research_request = research_client.send_research_request('What is the impact of AI on economy?')
# print(research_request)
# request_id = research_request.get('id')
# research_result = research_client.get_research_result(request_id)
# print(research_result)
