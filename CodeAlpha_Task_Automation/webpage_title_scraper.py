import requests
import re
from datetime import datetime

print("===================================")
print("      WEBPAGE TITLE SCRAPER")
print("===================================")

# Fixed webpage URL
url = "https://www.python.org"

try:
    # Send request
    response = requests.get(url)
    response.raise_for_status()

    # Extract title using regex
    title_match = re.search(
        r"<title>(.*?)</title>",
        response.text,
        re.IGNORECASE | re.DOTALL
    )

    if title_match:
        title = title_match.group(1).strip()

        print("\nWebsite URL :", url)
        print("Page Title  :", title)

        # Save title to file
        with open("title.txt", "w", encoding="utf-8") as file:
            file.write("WEBPAGE TITLE REPORT\n")
            file.write("====================\n")
            file.write(f"URL: {url}\n")
            file.write(f"Title: {title}\n")
            file.write(
                f"Scraped On: {datetime.now()}\n"
            )

        print("\nTitle saved successfully!")
        print("File created: title.txt")

    else:
        print("No title found on the webpage.")

except requests.exceptions.RequestException as e:
    print("Error accessing webpage:")
    print(e)

print("\nProgram Finished.")