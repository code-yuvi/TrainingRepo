
import mysql.connector

import csv



# ---------------- Database Connection ----------------

def get_connection():

    return mysql.connector.connect(

        host="localhost",

        user="root", # change if needed

        password="pass@word1", # change if needed

        database="tournament_db"

    )



# ---------------- CRUD Functions ----------------

def add_team():

    name = input("Enter team name: ")

    city = input("Enter city: ")



    conn = get_connection()

    cursor = conn.cursor()

    query = "INSERT INTO teams (name, city) VALUES (%s, %s)"

    cursor.execute(query, (name, city))

    conn.commit()

    conn.close()

    print("✅ Team added successfully!")



def view_teams():

    conn = get_connection()

    cursor = conn.cursor()

    query = "SELECT * FROM teams"

    cursor.execute(query)

    rows = cursor.fetchall()

    conn.close()



    print("\n--- Teams List ---")

    if rows:

        for row in rows:

            print(f"ID: {row[0]}, Name: {row[1]}, City: {row[2]}")

    else:

        print("No teams found.")



def add_match():

    team1 = int(input("Enter Team 1 ID: "))

    team2 = int(input("Enter Team 2 ID: "))

    date = input("Enter match date (YYYY-MM-DD): ")



    conn = get_connection()

    cursor = conn.cursor()

    query = "INSERT INTO matches (team1_id, team2_id, match_date, score1, score2) VALUES (%s, %s, %s, %s, %s)"

    cursor.execute(query, (team1, team2, date, 0, 0))

    conn.commit()

    conn.close()

    print("✅ Match scheduled successfully!")



def view_matches():

    conn = get_connection()

    cursor = conn.cursor()

    query = """SELECT m.id, t1.name, t2.name, m.match_date, m.score1, m.score2

               FROM matches m

               JOIN teams t1 ON m.team1_id = t1.id

               JOIN teams t2 ON m.team2_id = t2.id"""

    cursor.execute(query)

    rows = cursor.fetchall()

    conn.close()



    print("\n--- Matches List ---")

    if rows:

        for row in rows:

            print(f"Match ID: {row[0]}, {row[1]} vs {row[2]}, Date: {row[3]}, Score: {row[4]} - {row[5]}")

    else:

        print("No matches found.")



def update_match_result():

    match_id = int(input("Enter Match ID to update: "))

    score1 = int(input("Enter Team 1 score: "))

    score2 = int(input("Enter Team 2 score: "))



    conn = get_connection()

    cursor = conn.cursor()

    query = "UPDATE matches SET score1 = %s, score2 = %s WHERE id = %s"

    cursor.execute(query, (score1, score2, match_id))

    conn.commit()

    conn.close()

    print("✅ Match result updated successfully!")



def delete_match():

    match_id = int(input("Enter Match ID to delete: "))



    conn = get_connection()

    cursor = conn.cursor()

    query = "DELETE FROM matches WHERE id = %s"

    cursor.execute(query, (match_id,))

    conn.commit()

    conn.close()

    print("✅ Match deleted successfully!")



# ---------------- CSV Export Functions ----------------

def export_teams_csv():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM teams")

    rows = cursor.fetchall()

    conn.close()



    with open("C:\\Users\\Administrator\\Desktop\\teams.csv", "w", newline="") as f:

        writer = csv.writer(f)

        writer.writerow(["ID", "Name", "City"])

        writer.writerows(rows)

    print("📁 Teams exported to teams.csv")



def export_matches_csv():

    conn = get_connection()

    cursor = conn.cursor()

    query = """SELECT m.id, t1.name, t2.name, m.match_date, m.score1, m.score2

               FROM matches m

               JOIN teams t1 ON m.team1_id = t1.id

               JOIN teams t2 ON m.team2_id = t2.id"""

    cursor.execute(query)

    rows = cursor.fetchall()

    conn.close()



    with open("C:\\Users\\Administrator\\Desktop\\matches.csv", "w", newline="") as f:

        writer = csv.writer(f)

        writer.writerow(["Match ID", "Team 1", "Team 2", "Date", "Score1", "Score2"])

        writer.writerows(rows)

    print("📁 Matches exported to matches.csv")



# ---------------- Main Menu ----------------

def main_menu():

    while True:

        print("\n===== Local Tournament Manager =====")

        print("1. Add Team")

        print("2. View Teams")

        print("3. Add Match")

        print("4. View Matches")

        print("5. Update Match Result")

        print("6. Delete Match")

        print("7. Export Teams to CSV")

        print("8. Export Matches to CSV")

        print("9. Exit")



        choice = input("Enter your choice: ")



        if choice == "1":

            add_team()

        elif choice == "2":

            view_teams()

        elif choice == "3":

            add_match()

        elif choice == "4":

            view_matches()

        elif choice == "5":

            update_match_result()

        elif choice == "6":

            delete_match()

        elif choice == "7":

            export_teams_csv()

        elif choice == "8":

            export_matches_csv()

        elif choice == "9":

            print("👋 Exiting... Goodbye!")

            break

        else:

            print("❌ Invalid choice! Try again.")



if __name__ == "__main__":

    main_menu()
