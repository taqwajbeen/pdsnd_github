

### Date created
07/05/2023.

### Title: Bikeshare Data Analysis
This program allows users to explore and analyze bikeshare data for three cities: Chicago, New York, and 
Washington. It provides various statistics and insights about the data based on user input for city, month, 
and day.

### Prerequisites

- Python 3.9.6
- Pandas library

### Getting Started

1. Clone the repository or download the Python script.
2. Make sure you have Python 3.9.6 installed on your machine.
3. Install the Pandas library if you don't have it already. You can install it using pip:

pip install pandas

4. Run the script using the following command:

python bikeshare.py


### Description
. Upon running the program, you will be prompted to choose a city: 
Chicago, New York, or Washington.
2. Next, you can specify if you want to filter the data by month, day, 
both, or not at all.
- If you choose to filter by month, you need to enter the name of the 
month (e.g., January, February).
- If you choose to filter by day, you need to enter the day of the week as 
an integer (e.g., Sunday=1, Monday=2).
- If you choose to filter by both, you need to provide both the month and 
the day.
- If you choose not to apply any filters, enter "None".
3. The program will load the data for the specified city and apply the 
filters if any.
4. It will then display various statistics and insights based on the 
filtered data:
- The most frequent times of travel (e.g., popular month, popular day of 
the week, popular start hour).
- The most popular stations and trip (e.g., most commonly used start 
station, most commonly used end station, most frequent combination of 
start and end stations).
- Trip duration statistics (e.g., total travel time, mean travel time).
- User statistics (e.g., counts of user types, counts of gender, earliest 
and most recent year of birth, most common year of birth).
5. After displaying the statistics, you will have the option to view 
individual trip data.
- The program will display the raw data in chunks of five rows at a time.
- You can choose to view more chunks or exit the raw data view.
6. Finally, you will be asked if you want to restart the program. Enter 
"yes" to restart or any other input to exit.
7.To view the analysis of Chicago Bikeshare data,open the Tableau 
workbook.




### Files used
bikeshare.py
chicago.csv
newyork.csv
washington.csv
Citibike.twb

.

