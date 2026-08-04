import os


def create_output_folder():
    os.makedirs("Task_01_Web_Scraper/output", exist_ok=True)


def create_logs_folder():
    os.makedirs("Task_01_Web_Scraper/logs", exist_ok=True)