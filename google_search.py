from googlesearch import search

def google_search(query, num_results=10):
    search_results = []
    
    # Perform Google search
    for result in search(query, num_results=num_results, lang="en"):
        search_results.append(result)
    
    return search_results

if __name__ == "__main__":
    query = "yuhi chala chal rahi lyrics"
    results = google_search(query)
    
    for idx, result in enumerate(results, start=1):
        print(f"{idx}. {result}")
    breakpoint()