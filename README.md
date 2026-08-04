# 🌐 ShadowFox Web Scraper

A Python-based web scraping project developed as part of the **ShadowFox Python Development Internship (Intermediate Level)**. This project demonstrates how to extract website information using **Requests** and **BeautifulSoup**, process the data, and save it in structured formats for future analysis.

---

## 📌 Project Overview

This scraper connects to the official **ShadowFox** website, retrieves its HTML content, extracts useful information, and stores the scraped data into **CSV** and **JSON** files.

The project follows a clean folder structure, includes configuration management, utility functions, logging, and proper exception handling.

---

## ✨ Features

- 🌍 Connects to the ShadowFox website
- 📄 Extracts the website title
- 🏷 Extracts the main heading
- 📊 Extracts website statistics
- 💾 Saves scraped data to CSV
- 📁 Saves scraped data to JSON
- 📝 Maintains execution logs
- ⚠ Handles network errors gracefully
- 📂 Organized project structure

---

## 🛠 Technologies Used

- Python 3.x
- Requests
- BeautifulSoup4
- CSV Module
- JSON Module
- Logging Module

---

## 📁 Project Structure

```
Python-Development-Internship-Intermediate/
│
├── requirements.txt
├── .gitignore
│
└── Task_01_Web_Scraper/
    │
    ├── scraper.py
    ├── config.py
    ├── utils.py
    ├── README.md
    │
    ├── output/
    │   ├── shadowfox_data.csv
    │   └── shadowfox_data.json
    │
    ├── logs/
    │   └── scraper.log
    │
    └── screenshots/
```

---

## ⚙ Installation

Clone the repository:

```bash
git clone https://github.com/avishkarbhagat01/Python-Development-Internship-Intermediate.git
```

Navigate into the project:

```bash
cd Python-Development-Internship-Intermediate
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python Task_01_Web_Scraper/scraper.py
```

---

## 📄 Sample Output

```
Connecting to website...

Connection Successful!

Status Code: 200

Website Title:
ShadowFox | Learn, Create, Lead

Main Heading:
A Learning Brand built for outcomes.

Website Statistics:

0+ - learners impacted
0+ - industry programs
0% - satisfaction rate

CSV File Saved Successfully!

JSON File Saved Successfully!
```

---

## 📂 Output Files

After successful execution, the following files are generated automatically:

```
output/
├── shadowfox_data.csv
└── shadowfox_data.json
```

---

## 📝 Logging

Execution logs are stored inside:

```
logs/
└── scraper.log
```

Example:

```
Website connected successfully.
CSV file created successfully.
JSON file created successfully.
Web scraping completed successfully.
```

---

## 📚 Concepts Used

- HTTP Requests
- HTML Parsing
- BeautifulSoup
- File Handling
- CSV Operations
- JSON Operations
- Exception Handling
- Logging
- Project Structure
- Python Modules

---

## 🚀 Future Improvements

- Extract additional website content
- Scrape multiple pages
- Export data to Excel
- Store data in SQLite/MySQL
- Automate scraping using scheduling
- Use Selenium for JavaScript-rendered websites

---

## 👨‍💻 Author

**Avishkar Bhagat**

B.Tech Computer Science & Engineering
GitHub: https://github.com/avishkarbhagat01

---

## 📜 License

This project was developed for educational purposes as part of the **ShadowFox Python Development Internship**.

---
⭐ If you found this project useful, consider giving the repository a star.
