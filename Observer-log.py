#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# Observation Class
# ============================================================

class Observation:

    def __init__(self, target, exposure, observer, filt):
        self.target = target
        self.exposure = exposure
        self.observer = observer
        self.filter = filt

    def to_dict(self):
        return {
            "target": self.target,
            "exposure": self.exposure,
            "observer": self.observer,
            "filter": self.filter
        }


# ============================================================
# Database Class
# ============================================================

class Database:

    def __init__(self, database_name="observer_log.db"):
        self.database_name = database_name
        self.create_table()

    def connect(self):
        return sqlite3.connect(self.database_name)

    def create_table(self):
        connection = self.connect()

        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS observations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                target TEXT NOT NULL,
                exposure REAL NOT NULL,
                observer TEXT NOT NULL,
                filter TEXT NOT NULL
            )
        """)

        connection.commit()
        connection.close()

    def add_observation(self, observation):

        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO observations
            (target, exposure, observer, filter)
            VALUES (?, ?, ?, ?)
        """, (
            observation.target,
            observation.exposure,
            observation.observer,
            observation.filter
        ))

        connection.commit()
        connection.close()

    def get_all_observations(self):

        connection = self.connect()

        cursor = connection.cursor()

        cursor.execute("""
            SELECT target, exposure, observer, filter
            FROM observations
        """)

        rows = cursor.fetchall()

        connection.close()

        observations = []

        for row in rows:

            observation = Observation(
                row[0],
                row[1],
                row[2],
                row[3]
            )

            observations.append(observation)

        return observations

    def delete_all(self):

        connection = self.connect()

        cursor = connection.cursor()

        cursor.execute("DELETE FROM observations")

        connection.commit()
        connection.close()


# ============================================================
# Observer Log Class
# ============================================================

class ObserverLog:

    def __init__(self):

        self.observations = []

        self.database = Database()

        self.load_from_database()

    # --------------------------------------------------------
    # Load observations from database
    # --------------------------------------------------------

    def load_from_database(self):

        self.observations = self.database.get_all_observations()

    # --------------------------------------------------------
    # Add observation
    # --------------------------------------------------------

    def add_observation(self):

        target = input("Target: ")

        while True:

            try:

                exposure = float(
                    input("Exposure time (Second): ")
                )

                if exposure < 0:
                    print("Exposure cannot be negative.")
                    continue

                break

            except ValueError:

                print(
                    "Exposure time should be an int or float."
                )

        observer = input("Name of observer: ")

        filt = input("Filter name: ")

        observation = Observation(
            target,
            exposure,
            observer,
            filt
        )

        self.observations.append(observation)

        self.database.add_observation(observation)

        print("Observation added successfully.")

    # --------------------------------------------------------
    # Show observations
    # --------------------------------------------------------

    def show_observations(self):

        if len(self.observations) == 0:

            print("No observations found.")

            return

        print()

        for i, observation in enumerate(
            self.observations,
            start=1
        ):

            print(f"Observation >>> {i}")

            print(
                f"Target: {observation.target}"
            )

            print(
                f"Exposure: {observation.exposure}"
            )

            print(
                f"Observer: {observation.observer}"
            )

            print(
                f"Filter: {observation.filter}"
            )

            print("-" * 40)

    # --------------------------------------------------------
    # Search observation
    # --------------------------------------------------------

    def search_observation(self):

        target = input("Target: ")

        found = False

        for observation in self.observations:

            if target.lower() == observation.target.lower():

                print()

                print("Observation found.")

                print(
                    f"Target: {observation.target}"
                )

                print(
                    f"Exposure: {observation.exposure}"
                )

                print(
                    f"Observer: {observation.observer}"
                )

                print(
                    f"Filter: {observation.filter}"
                )

                print("-" * 40)

                found = True

        if not found:

            print("No target name found.")

    # --------------------------------------------------------
    # Convert observations to Pandas DataFrame
    # --------------------------------------------------------

    def to_dataframe(self):

        data = []

        for observation in self.observations:

            data.append({
                "Target": observation.target,
                "Exposure": observation.exposure,
                "Observer": observation.observer,
                "Filter": observation.filter
            })

        return pd.DataFrame(data)

    # --------------------------------------------------------
    # Data analysis
    # --------------------------------------------------------

    def analyze_data(self):

        if len(self.observations) == 0:

            print("No data available for analysis.")

            return

        df = self.to_dataframe()

        print()
        print("=" * 60)
        print("DATA ANALYSIS")
        print("=" * 60)

        print(
            f"Number of observations: {len(df)}"
        )

        print(
            f"Average exposure: "
            f"{df['Exposure'].mean():.2f} sec"
        )

        print(
            f"Maximum exposure: "
            f"{df['Exposure'].max()} sec"
        )

        print(
            f"Minimum exposure: "
            f"{df['Exposure'].min()} sec"
        )

        print(
            f"Total exposure: "
            f"{df['Exposure'].sum()} sec"
        )

        print()

        print("Exposure statistics:")

        print(
            df["Exposure"].describe()
        )

        print()

        print("Observations by target:")

        print(
            df["Target"].value_counts()
        )

        print()

        print("Average exposure by target:")

        print(
            df.groupby("Target")["Exposure"].mean()
        )

        print()

        print("Observations by filter:")

        print(
            df["Filter"].value_counts()
        )

        print()

        print("Average exposure by filter:")

        print(
            df.groupby("Filter")["Exposure"].mean()
        )

        print()

        print("Observations by observer:")

        print(
            df["Observer"].value_counts()
        )

        print()

        print("Total exposure by observer:")

        print(
            df.groupby("Observer")["Exposure"].sum()
        )

        print("=" * 60)

    # --------------------------------------------------------
    # Save to CSV
    # --------------------------------------------------------

    def save_to_csv(self):

        if len(self.observations) == 0:

            print("No observations to save.")

            return

        filename = input(
            "Your file name: "
        )

        with open(
            f"{filename}.csv",
            "w",
            newline=""
        ) as csvfile:

            fieldnames = [
                "target",
                "exposure",
                "observer",
                "filter"
            ]

            writer = csv.DictWriter(
                csvfile,
                fieldnames=fieldnames
            )

            writer.writeheader()

            for observation in self.observations:

                writer.writerow(
                    observation.to_dict()
                )

        print(
            "Observations saved successfully."
        )

    # --------------------------------------------------------
    # Chart 1: Exposure by target
    # --------------------------------------------------------

    def chart_exposure_by_target(self):

        if len(self.observations) == 0:

            print("No data available.")

            return

        df = self.to_dataframe()

        data = (
            df.groupby("Target")["Exposure"]
            .sum()
            .sort_values(ascending=False)
        )

        plt.figure(figsize=(10, 6))

        data.plot(kind="bar")

        plt.title(
            "Total Exposure Time by Target"
        )

        plt.xlabel("Target")

        plt.ylabel(
            "Total Exposure Time (sec)"
        )

        plt.xticks(rotation=45)

        plt.tight_layout()

        plt.show()

    # --------------------------------------------------------
    # Chart 2: Exposure distribution
    # --------------------------------------------------------

    def chart_exposure_distribution(self):

        if len(self.observations) == 0:

            print("No data available.")

            return

        df = self.to_dataframe()

        plt.figure(figsize=(10, 6))

        df["Exposure"].plot(
            kind="hist",
            bins=10
        )

        plt.title(
            "Exposure Time Distribution"
        )

        plt.xlabel(
            "Exposure Time (sec)"
        )

        plt.ylabel(
            "Number of Observations"
        )

        plt.tight_layout()

        plt.show()

    # --------------------------------------------------------
    # Chart 3: Average exposure by filter
    # --------------------------------------------------------

    def chart_exposure_by_filter(self):

        if len(self.observations) == 0:

            print("No data available.")

            return

        df = self.to_dataframe()

        data = (
            df.groupby("Filter")["Exposure"]
            .mean()
            .sort_values(ascending=False)
        )

        plt.figure(figsize=(10, 6))

        data.plot(
            kind="bar"
        )

        plt.title(
            "Average Exposure Time by Filter"
        )

        plt.xlabel("Filter")

        plt.ylabel(
            "Average Exposure Time (sec)"
        )

        plt.xticks(rotation=45)

        plt.tight_layout()

        plt.show()

    # --------------------------------------------------------
    # Chart 4: Exposure for each observation
    # --------------------------------------------------------

    def chart_observation_exposure(self):

        if len(self.observations) == 0:

            print("No data available.")

            return

        df = self.to_dataframe()

        plt.figure(figsize=(10, 6))

        plt.plot(
            range(1, len(df) + 1),
            df["Exposure"],
            marker="o"
        )

        plt.title(
            "Exposure Time per Observation"
        )

        plt.xlabel(
            "Observation Number"
        )

        plt.ylabel(
            "Exposure Time (sec)"
        )

        plt.grid(True)

        plt.tight_layout()

        plt.show()

    # --------------------------------------------------------
    # Chart menu
    # --------------------------------------------------------

    def show_charts(self):

        if len(self.observations) == 0:

            print("No data available for charts.")

            return

        while True:

            print()
            print("=" * 40)
            print("CHARTS")
            print("=" * 40)

            print("1. Exposure by Target")
            print("2. Exposure Distribution")
            print("3. Average Exposure by Filter")
            print("4. Exposure per Observation")
            print("5. Back")

            choice = input("Choose: ")

            if choice == "1":

                self.chart_exposure_by_target()

            elif choice == "2":

                self.chart_exposure_distribution()

            elif choice == "3":

                self.chart_exposure_by_filter()

            elif choice == "4":

                self.chart_observation_exposure()

            elif choice == "5":

                break

            else:

                print(
                    "Please select 1 to 5."
                )


# ============================================================
# Main Program
# ============================================================

def main():

    log = ObserverLog()

    while True:

        print()
        print("=" * 50)
        print(
            "Welcome to Observer Log".center(50)
        )
        print("=" * 50)

        print("1. Add Observation")
        print("2. Show Observations")
        print("3. Search Observation")
        print("4. Average Exposure")
        print("5. Maximum Exposure")
        print("6. Minimum Exposure")
        print("7. Total Exposure")
        print("8. Data Analysis")
        print("9. Save to CSV")
        print("10. Show Charts")
        print("11. Reload from Database")
        print("12. Exit")

        print("=" * 50)

        choice = input("Choose: ")

        # Add
        if choice == "1":

            log.add_observation()

        # Show
        elif choice == "2":

            log.show_observations()

        # Search
        elif choice == "3":

            log.search_observation()

        # Average
        elif choice == "4":

            if len(log.observations) == 0:

                print("No observations found.")

            else:

                df = log.to_dataframe()

                print(
                    f"Average exposure: "
                    f"{df['Exposure'].mean():.2f} sec"
                )

        # Maximum
        elif choice == "5":

            if len(log.observations) == 0:

                print("No observations found.")

            else:

                df = log.to_dataframe()

                print(
                    f"Maximum exposure: "
                    f"{df['Exposure'].max()} sec"
                )

        # Minimum
        elif choice == "6":

            if len(log.observations) == 0:

                print("No observations found.")

            else:

                df = log.to_dataframe()

                print(
                    f"Minimum exposure: "
                    f"{df['Exposure'].min()} sec"
                )

        # Total
        elif choice == "7":

            if len(log.observations) == 0:

                print("No observations found.")

            else:

                df = log.to_dataframe()

                print(
                    f"Total exposure: "
                    f"{df['Exposure'].sum()} sec"
                )

        # Data analysis
        elif choice == "8":

            log.analyze_data()

        # CSV
        elif choice == "9":

            log.save_to_csv()

        # Charts
        elif choice == "10":

            log.show_charts()

        # Reload database
        elif choice == "11":

            log.load_from_database()

            print(
                "Data loaded from database successfully."
            )

        # Exit
        elif choice == "12":

            print("Goodbye!")

            break

        else:

            print(
                "Please select a valid option."
            )


# ============================================================
# Program Entry Point
# ============================================================

if __name__ == "__main__":

    main()

