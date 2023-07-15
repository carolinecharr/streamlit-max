import streamlit as st
from bs4 import BeautifulSoup
import requests
import pandas as pd

# Define the LinkedIn search URL and keywords
search_url = "https://www.linkedin.com/search/results/people/?keywords={}"
keywords = "your_keywords_here"

# Scrape LinkedIn search results
def scrape_linkedin(search_url, keywords):
    leads = []

    # Create the search URL with keywords
    url = search_url.format(keywords)

    # Send GET request to the URL
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract lead information
    results = soup.find_all("li", {"class": "search-result"})
    for result in results:
        lead = {}
        lead["Name"] = result.find("span", {"class": "name actor-name"}).text.strip()
        lead["LinkedProfile"] = "https://www.linkedin.com" + result.find("a", href=True)["href"]
        lead["LinkedIn Title"] = result.find("p", {"class": "subline-level-1 t-14 t-black t-normal search-result__truncate"}).text.strip()
        lead["Location"] = result.find("p", {"class": "subline-level-2 t-12 t-black--light t-normal search-result__truncate"}).text.strip()
        lead["Company"] = result.find("p", {"class": "subline-level-2 t-12 t-black--light t-normal search-result__truncate"}).find_next_sibling("p").text.strip()
        lead["email"] = ""  # Add your email extraction logic here
        leads.append(lead)

    return leads

# Streamlit app
def main():
    # Page title
    st.title("LinkedIn Lead Collector")

    # Collect leads
    leads = scrape_linkedin(search_url, keywords)

    # Create a DataFrame from the leads
    leads_df = pd.DataFrame(leads)

    # Add a column for user input (stage)
    stages = ["Not Started", "In Progress", "Done", "Cancelled"]
    leads_df["Stage"] = st.sidebar.selectbox("Select Stage", stages)

    # Display leads table
    st.header("Leads Table")
    st.dataframe(leads_df)

if __name__ == "__main__":
    main()
