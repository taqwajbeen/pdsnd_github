# Necessary library imports used in the program
import time
import pandas as pd
from pprint import pprint

# Dict containing refrence to raw city files
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }  

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (int) day - name of the day of week to filter by, or "all" to apply no day filter
        df - Pandas DataFrame containing city data filtered by month and day
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # Get user input for city (chicago, new york city, washington) 
    while True:
        city=input("Would you like to see data for Chicago,New York or Washington?\n").lower()
        try:
           assert city=="chicago" or city=="new york" or city=="washington"
               
           # Get user input for month (all or january through june)
           time=input("Would you like to filter data by month,day,both or not at all? Type 'None' for no time filter!\n").lower()
           if time == "month":
                month=input("Which month? January,February,March,April,May or June?\n").lower()
                data = load_data(city,month,day="all")
           # Get user input for day (all or 0 through 6)     
           elif time == "day":
                day=str(input("Which day? Enter response as an integer for eg: Sunday=1\n"))
                month ="all"   
                data = load_data(city,month,int(day))
           # Get user input for both month and day     
           elif time == "both":
                month=input("Which month? January,February,March,April,May or June?\n").lower()
                day=input("Which day? Enter response as an integer for eg: Sunday=1\n")
                data = load_data(city,month,int(day))
           #  Get user input for no filters
           elif time =="none":
                month = "all"
                day = "all"
                data = load_data(city,month,day)
           else:
                data = None
                print("Invalid input")
                continue
           return(data)    
           print('-'*40)        
    # Let user know if the city provided is not valid or does not meet the input constraints
        except AssertionError as e:
            print(repr("Please Enter a Valid City"))


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.weekday
    df['city'] = city
    if month != 'all':
        df = df[df['month'] == month.title()]
    if day != 'all':
        # Filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]    
    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel.
    Args:
         df - Pandas DataFrame containing city data with or without filters
    Returns:
         None
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    popular_month = df['Start Time'].dt.month_name().mode()[0]
    print('Most popular month:', popular_month)
    
    # Display the most common day of week
    popular_day = df['Start Time'].dt.weekday.mode()[0]
    print('Most popular day of the week:', popular_day)
    

    # Display the most common start hour
    popular_hour = df['Start Time'].dt.hour.mode()[0]
    print('Most popular start hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """ Displays statistics on the most popular stations and trip.
    Args:
         df - Pandas DataFrame containing city data with or without filters
    Returns:
         None
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station:', popular_start_station)

    # Display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Popular End Station:', popular_end_station)

    # Display most frequent combination of start station and end station trip
    popular_station_combo = df.groupby(['Start Station','End Station']).size().sort_values(ascending=False).head(1).index[0]
    
    print ('Most Popular Station Combination:', (' and '.join(map(str, popular_station_combo))))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.
    Args:
         df - Pandas DataFrame containing city data with or without filters
    Returns:
         None
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print ('Total trip duration :', total_travel_time)


    # Display mean travel time
    mean_travel_time = df['Trip Duration'].describe()[1]
    print ('Mean trip duration :', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users.
    Args:
         df - Pandas DataFrame containing city data with or without filters
    Returns:
         None
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    df = df.loc[df['city'] != 'washington']
    
    if df.empty == False:

        # Display counts of gender
        gender_types = df['Gender'].value_counts()
        print(gender_types)
            
        # Display earliest year of birth
        earliest_yob = df['Birth Year'].astype('Int64').min()
        print("The earliest year of birth is :", earliest_yob)
        
        # Display most recent year of birth
        most_recent_yob = df['Birth Year'].astype('Int64').max()
        print("The most recent year of birth is :", most_recent_yob) 
        
        # Display most common year of birth
        most_common_yob = df['Birth Year'].astype('Int64').mode()[0]
        print("The most common year of birth is :", most_common_yob)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_prompt(df):
    """ Displays raw data for user.
    Args:
         df - Pandas DataFrame containing city data with or without filters
    Returns:
         dict - five rows of raw data
    """
    
    # Get city from dataframe and pass it to City Data dict to get raw data
    dff = pd.read_csv(CITY_DATA[df['city'].iloc[0]])
    
    # Set chunk size for displaying data to user
    chunk_size = 5
    
    # Rename default column names 
    dff.rename(columns={'Unnamed: 0': ''},inplace=True)
    
    # Get total number of rows in raw data
    num_rows = dff.shape[0]
    current_row = 0
    
    # Iterate over the rows until user enters a word other than yes
    while current_row < num_rows:
        chunk = dff.iloc[current_row:current_row + chunk_size]
        chunk_dict = chunk.to_dict('records')
        
        for row_dict in chunk_dict:
            pprint(row_dict)
            
        user_input = input('\nWould you like to view individual trip data? Enter yes or no.\n')
        
        if user_input.lower() != "yes":
            break
        
        current_row += chunk_size




def main():
    while True:
        df = get_filters()
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        user_prompt(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

