import os
import json
import serpapi

def run_agent(query: str):
    # Fetch API Key from environment variable
    api_key = os.getenv("SERPAPI_API_KEY")
    if not api_key:
        raise ValueError("SERPAPI_API_KEY environment variable is not set.")

    # Initialize SerpApi Client
    client = serpapi.Client(api_key=api_key)
    
    print(f"Searching web using SerpApi for: '{query}'...")
    
    # Query Google Search via SerpApi
    results = client.search(
        engine="google",
        q=query,
        gl="in",  # Region: India
        hl="en"   # Language: English
    )
    
    # Extract organic results
    organic_results = results.get("organic_results", [])
    
    formatted_data = []
    for item in organic_results[:5]:
        formatted_data.append({
            "title": item.get("title"),
            "link": item.get("link"),
            "snippet": item.get("snippet")
        })
        
    return formatted_data

if __name__ == "__main__":
    topic = input("Enter a research topic: ")
    output = run_agent(topic)
    print("\n--- Search Results ---")
    print(json.dumps(output, indent=2))