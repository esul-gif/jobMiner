import requests
import os

def search_jobs(keywords):
    app_key = "65f3396f4b93531083b8bdf53f203870"
    app_id = "3e7ce06b"
    country = "us"

    url = f'https://api.adzuna.com/v1/api/jobs/{country}/search/1'

    # Split keywords into manageable chunks
    keyword_chunks = [keywords[i:i + 1] for i in range(0, len(keywords), 1)]

    all_results = []
    
    for chunk in keyword_chunks:
        keyword_query = " OR ".join(chunk)
        print("Querying with keyword chunk: ", keyword_query)
        
        params = {
            'app_id': app_id,
            'app_key': app_key,
            'what': keyword_query,
            'where': 'New York'
        }

        # Send the request for each keyword chunk
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            job_data = response.json()
            all_results.extend(job_data.get('results', []))  # Add results to the list if found
        else:
            print(f"Error with chunk '{keyword_query}':", response.status_code, response.text)

    # Check if any results were found across all queries
    if all_results:
        for job in all_results:
            title = job.get('title', 'No title available')
            description = job.get('description', 'No description available')
            job_url = job.get('redirect_url', 'No link available')
            print(f"Job Title: {title}")
            print(f"Job Description: {description}")
            print(f"Job Link: {job_url}\n")
    else:
        print("No results found for the given keywords.")
