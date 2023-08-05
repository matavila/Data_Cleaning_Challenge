"""
    <=============== Day 2 of the 5-Day Data Challenge! ===============>
    Today, we're going work with dates

"""

# First of all, we need to set up our environment
import pandas as pd
import matplotlib.pyplot as plt

# With our environment ready, we need to bring our dataset to the project
Dataframe = pd.read_csv("Datasets/catalog.csv")

# So with our dateset ready, we must look what´s happening with the dates
print(Dataframe['date'].head(10))

"""
    Checking the firsts 10 rows of the column Date, we can see that those values are dates, but in the button
    of the output of head(), we can see that is showing that the data type of this column is "object" (python
    recognizes this as string type".
    
    If you check the pandas dtype documentation, you'll notice that there's also a specific datetime64 
    dtypes. Because the dtype of our column is object rather than datetime64, we can tell that Python doesn't
    know that this column contains dates.
    
"""

# For this point we will convert our date column to datetime
"""
    -> This is called "parsing dates" because we're taking in a string and identifying its component parts.
    The basic idea is that you need to point out which parts of the date are where and what punctuation is 
    between them. There are lots of possible parts of a date, but the most common are %d for day, %m for month,
    %y for a two-digit year and %Y for a four digit year.
"""

Dataframe['Date_Parsed'] = pd.to_datetime(Dataframe['date'], format="%m/%d/%y")
print(Dataframe['Date_Parsed'].head(10))

# Checking the result
"""
    One of the biggest dangers in parsing dates is mixing up the months and days. So in order to check the results
    let´s build some histograms
      -> We expect it to have values between 1 and 31
      
"""
# Getting to a new dataframe the day of the month of the date_persed column
Dataframe02 = Dataframe['Date_Parsed'].dt.day

# Removing the Null values
Dataframe02 = Dataframe02.dropna()

# Entering data
Dataframe02.hist()

# Adding titles and labels
plt.title("Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")

# Showing the histogram
plt.show()


