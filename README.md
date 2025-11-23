# Vityarthi
# Community Lost & Found Hub

## Project Overview

The **Community Lost & Found Hub** is a simple, command-line application designed to solve a common, real-world problem: connecting people who have lost items with those who have found them.

This project serves as a local, digital bulletin board. It is built entirely using **fundamental Python concepts**, making it an excellent example of how lists, dictionaries, functions, and control flow can be used to create a genuinely useful tool without relying on complex libraries or databases.

---

## Key Features

The application is straightforward and includes these core functions:

* **Report a Lost Item:** Allows users to input details (name, location, contact) about something they have misplaced.
* **Report a Found Item:** Allows users to post information about an item they have recovered.
* **Keyword Search:** Users can search both the lost and found lists using a single keyword (e.g., searching "wallet" will find "Black Leather Wallet").
* **Automatic Date Stamp:** Every item entry is automatically recorded with the date it was posted (Day-Month-Year format).
* **Simple Interface:** The application runs entirely within the terminal, guided by clear, numbered menu options.

---

## Technologies and Tools

This project is intentionally kept simple to focus on basic programming logic.

* **Language:** **Python 3**.
* **Core Concepts:** Uses only Python's basic structures: **functions**, **lists**, **dictionaries**, and **if/else** control flow.
* **Module Used:** The **`time`** standard library module (used only for date stamping and pausing the terminal output).
* **Storage:** Data is stored in memory (in Python lists) for the duration the program is running.

---

## How to Install and Run the Project

Getting the Hub running is quick and easy, as no external installations are required.

### 1. Preparation

1.  Create a folder on your computer for the project (e.g., `lost-found-hub`).
2.  Save the Python code file inside this folder, naming it **`hub.py`**.

### 2. Execution

1.  Open your operating system's **terminal** or **command prompt**.
2.  Navigate to the project folder using the `cd` command:
    ```bash
    cd lost-found-hub
    ```
3.  Execute the script using the Python interpreter:
    ```bash
    python hub.py
    ```

The main menu will load, allowing you to begin posting and searching.

---

## Testing Instructions

To ensure the application is working correctly, you can follow these simple test scenarios.

### Scenario A: Successful Reporting and Matching

1.  **Post Lost Item (Option 1):**
    * Enter: `Brown Glasses Case`, `Coffee Shop`, `owner@email.com`.
2.  **Post Found Item (Option 2):**
    * Enter: `Black Leather Wallet`, `Park Bench`, `finder@phone.com`.
3.  **Search (Option 3):**
    * Search keyword: `glasses`.
    * **Expected Result:** The "Brown Glasses Case" item should be displayed under **Matching LOST Items**.

### Scenario B: Unsuccessful Search

1.  **Search (Option 3):**
    * Search keyword: `laptop`.
2.  **Expected Result:** The message "Sorry, we found nothing matching 'laptop'." should be displayed, and no items should be listed.

### Scenario C: Program Exit

1.  **Exit (Option 4):**
2.  **Expected Result:** The program should print the farewell message and gracefully terminate the process.

![Image](https://github.com/user-attachments/assets/37d5cc2f-7abc-4da3-91d7-eb32f75f8d6d)
![Image](https://github.com/user-attachments/assets/dad9dd0d-6254-4ece-a6c8-7bab45fb8895)![Image](https://github.com/user-attachments/assets/dad9dd0d-6254-4ece-a6c8-7bab45fb8895)

