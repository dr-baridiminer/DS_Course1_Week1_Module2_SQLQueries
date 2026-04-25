import pandas as pd
import sqlite3

# Create connections
conn1 = sqlite3.connect('planets.db')
conn2 = sqlite3.connect('dogs.db')
conn3 = sqlite3.connect('babe_ruth.db')

# Step 1: Return all columns for planets with 0 moons
df_no_moons = pd.read_sql("""SELECT * FROM planets WHERE num_of_moons = 0; """, conn1)

# Step 2: Return name and mass of planets with exactly 7-letter names
df_name_seven = pd.read_sql("""SELECT name, mass FROM planets WHERE LENGTH(name) = 7; """, conn1)

# Step 3: Return name and mass for planets with mass <= 1.00
df_mass = pd.read_sql("""SELECT name, mass FROM planets WHERE mass <= 1.00; """, conn1)

# Step 4: Return all columns for planets with at least one moon and mass < 1.00
df_mass_moon = pd.read_sql("""SELECT * FROM planets WHERE num_of_moons >= 1 AND mass < 1.00; """, conn1)

# Step 5: Return name and color of planets with "blue" in color
df_blue = pd.read_sql("""SELECT name, color FROM planets WHERE color LIKE '%blue%'; """, conn1)

# Step 6: Return name, age, breed of hungry dogs sorted by age (youngest to oldest)
df_hungry = pd.read_sql("""SELECT name, age, breed FROM dogs WHERE hungry = 1 ORDER BY age ASC; """, conn2)

# Step 7: Return name, age, hungry for hungry dogs aged 2-7, sorted alphabetically
df_hungry_ages = pd.read_sql("""SELECT name, age, hungry FROM dogs WHERE hungry = 1 AND age BETWEEN 2 AND 7 ORDER BY name ASC; """, conn2)

# Step 8: Return name, age, breed for 4 oldest dogs, sorted by breed alphabetically
df_4_oldest = pd.read_sql("SELECT name, age, breed FROM dogs ORDER BY age DESC LIMIT 4", conn2)

# Step 9: Return total number of years Babe Ruth played
df_ruth_years = pd.read_sql("""SELECT COUNT(*) as total_years FROM babe_ruth_stats; """, conn3)

# Step 10: Return total number of homeruns in career
df_hr_total = pd.read_sql("""SELECT SUM(hr) as total_homeruns FROM babe_ruth_stats; """, conn3)

# Step 11: Return team name and number of years for each team
df_teams_years = pd.read_sql("""SELECT team, COUNT(*) as number_years FROM babe_ruth_stats GROUP BY team; """, conn3)

# Step 12: Return team name and average at_bats for teams with average > 200
df_at_bats = pd.read_sql("""SELECT team, AVG(at_bats) as average_at_bats FROM babe_ruth_stats GROUP BY team HAVING AVG(at_bats) > 200; """, conn3)

# Close connections
conn1.close()
conn2.close()
conn3.close()
