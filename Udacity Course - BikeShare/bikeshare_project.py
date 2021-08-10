import time as time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['chicago', 'washington', 'new york']
    while True:
        city = input("Type the name of the city you would like to see data for :\n Chicago, New York, Washington\n").lower()
        if acity in cities:
            break
        else:
            print("Not a valid response.")

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while True:
        month = input("What month would you like to learn about? January', February, March, April, May, June, All?\n").lower()
        if amonth in months:
            break
        else:
            print("Incorrect input. Please enter a previously mentioned month to continue.")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']
    while True:
        day = input("Would you like to filter the information by the day of the week?\n").lower()
        if day == 'yes':
            day = input("Enter a day of the week you would like to learn about. If you dont have a preference type 'All'. \n All, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday\n").lower()
        else:
            break
        if day == week_days in days:
            break
        else:
            print('Not a valid response. Answer must be case sensitive. To exit program press "Enter"')

        print('-'*40)
    return city, month, day

    """
    Loads data for the specified city and filters by month and day if applicable.
        Args:
            (str) city - name of the city to analyze
            (str) month - name of the month to filter by, or "all" to apply no month filter
            (str) day - name of the day of week to filter by, or "all" to apply no day filter
        Returns:
            df - Pandas DataFrame containing city data filtered by month and day
        """
def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day
    df['hour'] = df['Start Time'].dt.hour
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day of week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    start_time = time.time()
    print('\nCalculating The Most Frequent Times of Travel...\n')

    # TO DO: display the most common month

    print("The most common month is: {}".format
    (str(df['month'].mode().values[0])))

    # TO DO: display the most common day of day_of_week
    print("The most common day of the week: {}".format
    (str(df['day_of_week'].mode().values[0])))

    # TO DO: display the most common start hour
    print("The most common start hour: {}".format
    (str(df['hour'].mode().values[0])))

    start_time = time.time()
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    start_time = time.time()
    print('\nCalculating The Most Popular Stations and Trip...\n')

    # TO DO: display most commonly used start station
    print("The most common start station is: {} ".format(df['Start Station'].mode().values[0]))

    # TO DO: display most commonly used end station
    print("The most common end station is: {}".format(df['End Station'].mode().values[0]))

    # TO DO: display most frequent combination of start station and end station trip
    df['routes'] = df['Start Station']+ " " + df['End Station']
    print("The most common route is: {}".format(df['routes'].mode().values[0]))

    start_time = time.time()
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day
    df['hour'] = df['Start Time'].dt.hour

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['duration'] = df['End Time'] - df['Start Time']
    print("The total travel time is: {}".format(str(df['duration'].sum())))

    # TO DO: display mean travel time
    print("The mean travel time is: {}".format(str(df['duration'].mean())))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df, city):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("These are the different types of users:")
    print(df['User Type'].value_counts())

    if CITY_DATA != 'washington.csv':
        # Display counts of gender
        print("Here is the gender mix:")
        print(df['Gender'].value_counts())
        # TO DO: Display earliest, most recent, and most common year of birth
        print("The earliest birthdate year: {}".format(str(int(df['Birth Year'].min()))))
        print("The latest birthdate year: {}".format(str(int(df['Birth Year'].max()))))
        print("The most common birth year is: {}".format(str(int(df['Birth Year'].mode().values[0]))))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    while True:
        choice = input('\nWould you like to view raw data? Enter Yes or No\n')
        if choice == "yes":
            start_loc = 0
            print(df.iloc[i:i+5])
            i += 5
        if choice == "no":
            break
        choice = input('Do you wish to continue? Enter yes or no').lower()
        if choice == 'yes':
            print(df.iloc[i:i+5])
            i += 5
        if choice == "no":
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
