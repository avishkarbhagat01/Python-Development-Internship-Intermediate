import requests
import csv
import json
import logging
from bs4 import BeautifulSoup

from config import URL, HEADERS, TIMEOUT
from utils import create_output_folder, create_logs_folder

# Create required folders
create_output_folder()
create_logs_folder()

# Configure Logging
logging.basicConfig(
    filename="Task_01_Web_Scraper/logs/scraper.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

print("Connecting to website...")

try:
    # Send HTTP GET request
    response = requests.get(
        URL,
        headers=HEADERS,
        timeout=TIMEOUT
    )

    response.raise_for_status()

    logging.info("Website connected successfully.")

    print("Connection Successful!")
    print("Status Code:", response.status_code)

    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # -----------------------
    # Website Title
    # -----------------------
    title = soup.title.get_text(strip=True)

    print("\nWebsite Title:")
    print(title)

    # -----------------------
    # Main Heading
    # -----------------------
    heading = soup.find("h1").get_text(separator=" ", strip=True)

    print("\nMain Heading:")
    print(heading)

    # -----------------------
    # Website Statistics
    # -----------------------
    print("\nWebsite Statistics:\n")

    p_tags = soup.find_all("p")
    stats = []

    for i in range(len(p_tags) - 1):

        number = p_tags[i].get_text(strip=True)
        label = p_tags[i + 1].get_text(strip=True)

        if label in [
            "learners impacted",
            "industry programs",
            "satisfaction rate"
        ]:

            stats.append({
                "Number": number,
                "Label": label
            })

            print(f"{number} - {label}")

    # -----------------------
    # Save CSV
    # -----------------------
    csv_file = "Task_01_Web_Scraper/output/shadowfox_data.csv"

    with open(csv_file, "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow(["Title", title])
        writer.writerow(["Main Heading", heading])
        writer.writerow([])
        writer.writerow(["Number", "Description"])

        for item in stats:
            writer.writerow([item["Number"], item["Label"]])

    logging.info("CSV file created successfully.")

    print("\nCSV File Saved Successfully!")
    print(csv_file)

    # -----------------------
    # Save JSON
    # -----------------------
    json_file = "Task_01_Web_Scraper/output/shadowfox_data.json"

    data = {
        "Website Title": title,
        "Main Heading": heading,
        "Statistics": stats
    }

    with open(json_file, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    logging.info("JSON file created successfully.")

    print("\nJSON File Saved Successfully!")
    print(json_file)

    logging.info("Web scraping completed successfully.")

except requests.exceptions.RequestException as e:
    logging.error(f"Error: {e}")
    print("Error:", e)