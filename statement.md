# Project Statement: Community Lost & Found Hub

## 🎯 Problem Statement

The simple act of losing or finding a personal item in a local area (like a school, workplace, or neighborhood) often lacks an effective, immediate, and accessible method for connecting the owner with the finder. People typically resort to static bulletin boards, generalized social media posts, or simply hoping the item turns up. This leads to friction, delays, and a lower success rate for item recovery.

**The core problem is the lack of a centralized, dedicated, and simple digital platform for local lost and found reporting.**

---

## 🧭 Scope of the Project

The scope of the Community Lost & Found Hub is intentionally kept **narrow and foundational** to ensure maximum utility with minimal complexity.

### What is Included (In Scope)

* **Core Functionality:** The ability to add new **LOST** item reports and new **FOUND** item reports.
* **Search Functionality:** A simple keyword search feature to match names and descriptions between the two lists.
* **Data Structure:** Using **Python lists and dictionaries** for in-memory storage of item records.
* **Interface:** A clear, interactive, command-line (terminal) interface for all user interactions.

### What is Excluded (Out of Scope)

* **Persistence:** The project **will not** save data to a file or database. All records are cleared when the program exits.
* **Advanced Matching:** No fuzzy logic, image recognition, or complex date filtering is included.
* **User Accounts:** There is no authentication or distinction between different users.

---

## 🧑‍🤝‍🧑 Target Users

This tool is designed for anyone who needs a quick and easy solution for local item tracking:

1.  **Community Organizers/Neighborhood Watch:** Individuals looking for a lightweight tool to manage local postings without setting up a full website.
2.  **School/Campus Administrators:** Staff who need a simple system to track items reported within their buildings.
3.  **General Public:** Anyone who has lost an item (keys, wallet, phone) or found one and wants a fast, direct way to post information.
4.  **Beginner Developers:** Students and new coders looking for a practical, self-contained Python project that clearly demonstrates core concepts.

---

## ✨ High-Level Features

The application is modularized into these key user workflows:

1.  **Report Feature:** Allows the user to select the item's status (**LOST** or **FOUND**) and prompts them to enter the essential details (name, location, contact).
2.  **Tracking:** Stores all collected item information in a list format, recording the date of submission.
3.  **Search Feature:** Scans the lists for both lost and found records that contain the user-specified keyword, displaying any potential matches.
4.  **Main Loop:** Runs the entire application, presenting a clear menu and continuously accepting user input until the 'Exit' command is given.
