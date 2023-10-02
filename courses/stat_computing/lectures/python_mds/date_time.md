# Dates and times as a data type

Dates and time are not like natural numbers. There is no natural
0 point in time, certain regions have day-light savings, and
different regions have different time zones. All these peculiarities 
lead to the need for a special data type for handling dates and times.

Fortunately the built-in package, `datetime` has most of the functionalities
covered.
- `datetime.date` works with dates only (no hours, minutes, etc)
  ```python
  import datetime

  today = datetime.date.today()
  day2 = datetime.date(2011, 10, 23)
  days_passed = today - day2
  days_passed.days
  days_passed.total_seconds()
  ```
- `datetime.datetime` works with dates and times and can be parsed
  from string using [`datetime.datetime.strptime()` and the corresponding
  codes](https://docs.python.org/3.10/library/datetime.html#strftime-strptime-behavior).
  This should handle most cases of dates that are in non-standardized
  formats.
  ```python
  from datetime import datetime 
  
  today = datetime.today()
  past = datetime.strptime('2011 Feb 02; 11-10-00',
                           '%Y %b %d; %H-%M-%S')
  time_passed = today - past
  time_passed.total_seconds() # This is a float

  # Print out the relevant time information
  today.strftime('%Y_%m_%d')
  ```
- `datetime.timedelta` is a special class of data that works with time differences
  They are important because it's not obvious to a program that there are 24 hours
  in a day, 60 minutes in an hour, etc. 
  ```python
  from datetime import timedelta, datetime
  today = datetime.today()
  td = timedelta(days=4.5)
  four_days_and_a_half_later = today + td
  print(four_days_and_a_half_later)
  ```
- Dealing with time zones is well known to be painful. My recommmendation
  is to familiarize yourself with the "UTC offset" concept and add in the time zone
  information proactively whenever possible. The key is to assume that people outside
  of your time zone may work with your timestamps. Since I'm in New York,
  I created an example 
  ```python
  from datetime import datetime
  
  timestamp = "2017-03-12 02:43:00"
  odd_time = datetime.strptime(timestamp + " UTC-0500",
                               "%Y-%m-%d %H:%M:%S UTC%z")
  ```
- Often in data you'll see UNIX timestamps, i.e. the seconds since 1970, January 1st, 00:00:00.
  This looks like a 10 digit value like 1695965380. You can work with these using the 
  `datetime.datetime.timestamp()` method.

  ```python
  from datetime import datetime

  start_of_unix_time = datetime(year=1970, month=1, day=1, hour=0, minute=0, second=0)
  # Depending on your time zone, the following may not be 0
  start_of_unix_time.timestamp()
  ```
