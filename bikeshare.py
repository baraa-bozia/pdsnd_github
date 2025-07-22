import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    this update in refactoring
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Would you like to see data for Chicago, New York, or Washington? ").lower()
        if city in CITY_DATA:
            break
        else:
            print("Invalid input. Please enter Chicago, New York, or Washington.")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        filter_type = input("Would you like to filter by month, day,both-month and day or not at all? Type 'none' for no filter: ").lower()
        if filter_type in ['month', 'day','both', 'none']:
            break
        else:
            print("Invalid input. Please enter 'month', 'day',both or 'none'.")

    month, day = 'all', 'all'
    
    if filter_type in ['month', 'both']:
          months = ['january','february','march','april','may','june']
          while True:
            month = input('Which month? January–June: ').strip().lower()
            if month in months:
                break
            print('Invalid month.')

    if filter_type in ['day', 'both']:
        days = ['saturday','sunday''monday','tuesday','wednesday','thursday','friday']
        while True:
            day = input('Which day? saturday–friday: ').strip().lower()
            if day in days:
                break
            print('Invalid day.')

    print(f'\nFilters selected — City: {city.title()}, Month: {month.title() if month != "all" else "All"}, Day: {day.title() if day != "all" else "All"}')
    
    return city, month, day

    print('-'*40)
    return city, month, day


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

    # Convert Start Time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month_name().str.lower()
    df['day_of_week'] = df['Start Time'].dt.day_name().str.lower()

    # Filter by month
    if month != 'all':
        df = df[df['month'] == month]

    # Filter by day
    if day != 'all':
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("Most common month:", df['month'].mode()[0].title())


    # TO DO: display the most common day of week
    print("Most common day of week:", df['day_of_week'].mode()[0].title())


    # TO DO: display the most common start hour
    print("Most common start hour:", df['Start Time'].dt.hour.mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    if 'Start Station' in df.columns:
        print('Most commonly used start station:', df['Start Station'].mode()[0])


    # TO DO: display most commonly used end station
    if 'End Station' in df.columns:
        print('Most commonly used end station:', df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    if 'Start Station' in df.columns and 'End Station' in df.columns:
        df['Trip Combination'] = df['Start Station'] + " → " + df['End Station']
        print('Most frequent combination of start and end station trip:', df['Trip Combination'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration = df['Trip Duration'].sum()
    print(f'Total travel time: {total_duration} seconds ({total_duration/3600:.2f} hours)')

    # TO DO: display mean travel time
    mean_duration = df['Trip Duration'].mean()
    print(f'Mean travel time: {mean_duration:.2f} seconds ({mean_duration/60:.2f} minutes)')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    if 'User Type' in df.columns:
        print('User Types:')
        print(df['User Type'].value_counts(), "\n")

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print('Gender Breakdown:')
        print(df['Gender'].value_counts(), "\n")
    else:
        print('No gender data available for this city.\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('Birth Year Stats:')
        print('Earliest birth year:', int(df['Birth Year'].min()))
        print('Most recent birth year:', int(df['Birth Year'].max()))
        print('Most common birth year:', int(df['Birth Year'].mode()[0]))
    else:
        print('No birth year data available for this city.')

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
def display_raw_data(df):
    row = 0
    while True:
        show = input('\nShow 5 rows of raw data? Enter yes or no: ').lower()
        if show == 'yes':
            print(df.iloc[row:row+5])
            row += 5
            if row >= len(df):
                print('End of data reached.')
                break
        elif show == 'no':
            break
        else:
            print('Invalid input; please enter yes or no.')

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
