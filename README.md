# 🔭 Observer Log

> A Python-based astronomical observation management system built with **Object-Oriented Programming, SQLite, Pandas, NumPy, and Matplotlib**.

Observer Log is a terminal-based application for recording, managing, analyzing, and visualizing astronomical observation data.

The project started as a simple Python program using lists and dictionaries and was later redesigned using **Object-Oriented Programming (OOP)** and extended with a database, data analysis, numerical processing, CSV export, and data visualization.

---

## ✨ Features

### 🔭 Observation Management

- Add new astronomical observations
- Store:
  - Target name
  - Exposure time
  - Observer name
  - Filter name
- Display all recorded observations
- Search observations by target

### 🗄️ SQLite Database

All observations are stored in a local SQLite database.

The application automatically creates:

```text
observer_log.db
````

No external database server is required.

### 📊 Data Analysis with Pandas

The project provides statistical analysis including:

* Number of observations
* Average exposure time
* Maximum exposure time
* Minimum exposure time
* Total exposure time
* Statistical summary using `describe()`
* Most frequently observed targets
* Most frequently used filters
* Observations grouped by target
* Observations grouped by filter
* Observations grouped by observer

### 🔢 Numerical Analysis with NumPy

NumPy can be used to convert exposure-time data into numerical arrays and perform calculations such as:

* Mean
* Maximum
* Minimum
* Sum
* Numerical array operations

Example:

```python
exposures = df["Exposure"].to_numpy()

average = np.mean(exposures)
maximum = np.max(exposures)
minimum = np.min(exposures)
total = np.sum(exposures)
```

### 📈 Data Visualization with Matplotlib

The project can generate different charts, including:

* Total exposure time by target
* Exposure time histogram
* Average exposure time by filter
* Exposure time for each observation

### 📄 CSV Export

Observation data can be exported to a CSV file for use in:

* Microsoft Excel
* Google Sheets
* Pandas
* Other data-analysis software

---

# 🧠 Technologies

| Technology    | Purpose                   |
| ------------- | ------------------------- |
| 🐍 Python     | Main programming language |
| 🧱 OOP        | Project architecture      |
| 🗄️ SQLite    | Data storage              |
| 🐼 Pandas     | Data analysis             |
| 🔢 NumPy      | Numerical computation     |
| 📊 Matplotlib | Data visualization        |
| 📄 CSV        | Data export               |

---

# 🏗️ Project Architecture

The application follows an object-oriented architecture.

```text
Observation
     │
     ▼
ObserverLog
     │
     ├── Database
     │      │
     │      └── SQLite
     │
     ├── Pandas
     │      │
     │      └── Data Analysis
     │
     ├── NumPy
     │      │
     │      └── Numerical Analysis
     │
     └── Matplotlib
            │
            └── Visualization
```

---

# 📦 Main Classes

## `Observation`

Represents a single astronomical observation.

```python
class Observation:
    def __init__(self, target, exposure, observer, filt):
        self.target = target
        self.exposure = exposure
        self.observer = observer
        self.filter = filt
```

Each observation contains four main properties:

```text
Target
Exposure
Observer
Filter
```

---

## `Database`

Responsible for communication with the SQLite database.

Its responsibilities include:

* Creating the database
* Creating the observations table
* Saving observations
* Loading observations
* Managing database operations

The database table contains:

```text
id
target
exposure
observer
filter
```

---

## `ObserverLog`

This is the main application class.

It manages:

* Observations
* User interaction
* Searching
* Data analysis
* CSV export
* Charts
* Database communication

---

# 🔄 Data Flow

```text
                 User
                  │
                  ▼
          Add Observation
                  │
                  ▼
          Observation Object
                  │
                  ▼
             ObserverLog
                  │
          ┌───────┴────────┐
          ▼                ▼
       SQLite          Pandas DataFrame
          │                │
          │          ┌─────┴─────┐
          │          ▼           ▼
          │        NumPy     Analysis
          │                      │
          │                      ▼
          │                 Matplotlib
          │                      │
          ▼                      ▼
       Database               Charts
```

---

# 🚀 Installation

Make sure Python 3.10 or newer is installed.

Install the required libraries:

```bash
pip install pandas numpy matplotlib
```

> `sqlite3` is included with Python and does not need to be installed separately.

You can also install all Python dependencies using:

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

Run the main Python file:

```bash
python main.py
```

If your main file has another name, replace `main.py` with the appropriate filename.

---

# 🖥️ Application Menu

The application provides a menu similar to:

```text
========================================
          Welcome to Observer Log
========================================

1. Add Observation
2. Show Observation
3. Average Exposure
4. Maximum Exposure
5. Minimum Exposure
6. Total Exposure
7. Search Observation
8. Data Analysis
9. Save to CSV
10. Charts
11. Reload Database
12. Exit
```

---

# 📝 Example Observation

Suppose we record:

```text
Target: M42
Exposure time: 120
Observer: Ali
Filter: H-alpha
```

The application creates an `Observation` object:

```python
Observation(
    target="M42",
    exposure=120,
    observer="Ali",
    filt="H-alpha"
)
```

The observation is then stored in the database and becomes available for analysis.

---

# 📊 Example Analysis

If the database contains:

| Target | Exposure |
| ------ | -------: |
| M42    |      120 |
| M31    |      180 |
| M42    |      240 |
| M45    |       90 |

Pandas can calculate:

```text
Number of observations: 4
Average exposure: 157.5 sec
Maximum exposure: 240 sec
Minimum exposure: 90 sec
Total exposure: 630 sec
```

The same data can also be visualized using Matplotlib.

---

# 📈 Visualization

The project can create charts such as:

### Total Exposure by Target

A bar chart can be used to compare the total exposure time for different astronomical targets.

### Exposure Distribution

A histogram can be used to understand how exposure times are distributed across observations.

### Average Exposure by Filter

This allows the observer to compare different filters based on their average exposure time.

---

# 💾 Data Persistence

One of the important improvements over a simple Python list is **data persistence**.

In the original version, observations were stored using:

```python
observations = []
```

This meant that all data disappeared when the program closed.

The new version uses SQLite:

```text
observer_log.db
```

Therefore, observations remain available after restarting the application.

---

# 🧩 Project Evolution

This project was developed step by step.

### Version 1 — Basic Python

Initially, observations were represented using dictionaries:

```python
obs = {
    "target": target,
    "exposure": exposure,
    "observer": observer,
    "filter": filt
}
```

### Version 2 — Object-Oriented Programming

The dictionary-based design was replaced with an `Observation` class:

```python
obs = Observation(
    target,
    exposure,
    observer,
    filt
)
```

This made the program more organized and scalable.

### Version 3 — Database

SQLite was added to make the data persistent.

```text
Python Objects
      ↓
SQLite Database
```

### Version 4 — Data Analysis

Pandas was introduced to turn observation data into a DataFrame:

```python
df = pd.DataFrame(data)
```

### Version 5 — Numerical Computing

NumPy was introduced for numerical operations on exposure-time data:

```python
exposures = df["Exposure"].to_numpy()
```

### Version 6 — Visualization

Matplotlib was added to visualize the collected data:

```text
Data
 ↓
Pandas
 ↓
NumPy
 ↓
Matplotlib
 ↓
Charts
```

---

# 🎯 What This Project Demonstrates

This project demonstrates several important concepts in Python development:

* Variables and data types
* Functions
* Loops
* Conditional statements
* Lists and dictionaries
* Classes and objects
* Object-Oriented Programming
* Encapsulation
* Exception handling
* File handling
* CSV files
* SQLite databases
* SQL queries
* Pandas DataFrames
* NumPy arrays
* Statistical analysis
* Data visualization
* Modular programming

---

# 📁 Recommended Project Structure

```text
Observer-Log/
│
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
└── observer_log.db
```

> The SQLite database file can be excluded from GitHub using `.gitignore` if you don't want to upload generated user data.

---

# 🔮 Future Improvements

Possible future features include:

* ✏️ Edit existing observations
* 🗑️ Delete individual observations
* 🔍 Advanced search and filtering
* 📅 Observation date and time
* 📍 Observation location
* 🌡️ Temperature and weather conditions
* 🔭 Telescope information
* 📷 Camera information
* 🌌 Object coordinates (RA/DEC)
* 📊 More advanced statistical analysis
* 📈 Interactive dashboards
* 🌐 Web interface
* 🖥️ GUI using Tkinter or PyQt
* 🔐 User accounts
* ☁️ Cloud database
* 📡 Integration with astronomical APIs

---

# 🌌 Future Vision

The long-term goal could be to transform Observer Log from a terminal application into a complete astronomical observation platform:

```text
                  Observer Log
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
   Observation      Database       Analytics
        │              │              │
        ▼              ▼              ▼
     Telescope       SQLite         Pandas
     Camera          SQL            NumPy
     Location                       Matplotlib
        │                              │
        └──────────────┬───────────────┘
                       ▼
                Visualization
                       │
                       ▼
                Astronomical Data
```

---

# 🛠️ Requirements

Recommended environment:

```text
Python 3.10+
Pandas
NumPy
Matplotlib
SQLite3
```

---

# 👨‍💻 Author

Developed as a Python learning project with a focus on:

**Python → OOP → SQL → Data Analysis → Numerical Computing → Visualization**

---

# ⭐ Why Observer Log?

Observer Log is more than a simple CRUD application.

It combines several important areas of Python development into one practical project:

> **Object-Oriented Programming + Database Management + Data Analysis + Numerical Computing + Data Visualization**

This makes it a useful project for practicing Python while working with a realistic scientific-data scenario.

---

## 📜 License

This project is created for educational and learning purposes.
