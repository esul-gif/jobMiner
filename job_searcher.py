from careerjet_api_client import CareerjetAPIClient

def test_careerjet_api():
    # Initialize the Careerjet API client
    cj = CareerjetAPIClient("en_US")  # Use appropriate locale (e.g., "en_US" for United States)

    # Define the search parameters
    search_params = {
        'keywords': 'Software Developer',
        'location': 'Remote',
        'page': 1,
    }

    # Perform the search
    result = cj.search(search_params)

    # Check if any jobs were returned and print a few details
    if result['hits'] > 0:
        print("Job listings found:")
        for job in result['jobs'][:5]:  # Print first 5 job results
            print(f"Title: {job['title']}")
            print(f"Company: {job['company']}")
            print(f"Location: {job['locations']}")
            print(f"URL: {job['url']}")
            print("------")
    else:
        print("No job listings found.")

# Run the test function
if __name__ == "__main__":
    test_careerjet_api()
