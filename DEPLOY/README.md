### Library use

After downloading and configuring the library, we can start using it.  

First let's import the library into the project.  

```python
from pyGitInfo import *
```  

### Notes/Standardization  

**Date:** The default format for passing dates is "month-day-year" Ex: "06-07-2023" is equivalent to June 07, 2023  

### Functions and Returns  

- **get_commits_by_user()**  
  Allows you to search for commits by user, passing 3 strings as a parameter, the user's name (str), a start date and an end date.  

  ```python
  get_commits_by_user('name_user','date_init','date_end')
  ```  
  
  This function returns _DataFrame_ from the _Pandas_ library or an error message  

- **get_commits_users()**  
  Allows you to search for commits from all contributors, passing as a parameter 2 strings that define the time range, a start date and an end date.  

  ```python
  get_commits_users('date_init','date_end')
  ```  

  This function returns _DataFrame_ from the _Pandas_ library  

- **get_coAuthor()**  
  Search all commits with Coauthor, passing as parameters 2 strings that define the time range, a start date and an end date.  

  ```python
  get_coAuthor('date_init','date_end')
  ```  

  This function returns a _DataFrame_ from the _Pandas_ library or an error message  

- **issues_month()**  
  This function verifies how many Issues were closed per month, within the stipulated period. The function receives 2 date strings as a parameter, the start and end date.

  ```python
  issues_month('date_init','date_end')
  ```  

  The function returns _DataFrame_ from the _Pandas_ library and also generates a png graphic

- **calculate_commit_average()**  
  Calculates the average commits across all contributors and shows who is above or below that average. You must pass the analysis period as a parameter with 2 strings representing the dates

  ```python
  calculate_commit_average('date_init','date_end')
  ```  

  The function returns _DataFrame_ from the _Pandas_ library and also generates a png graphic

- **commit_data()**  
  Searches for all commits on a specific day, the function receives a string with the desired date as a parameter.

  ```python
  commit_data('date')
  ```  

  The function generates a markdown file with the information

- **commit_palavra()**  
  Searches for all commits (within a time range) that have the desired word in their description. This function receives 3 strings as a parameter, the first with the 'word' to be searched for, and the 2 'dates' referring to the time interval

  ```python
  commit_palavra('palavra','date_init','date_end')
  ```  

  The function returns a _DataFrame_ from the _Pandas_ library or an error message  

- **check_extension()**  
  It does a search for the files that are being committed by each contributor and classifies them according to their extension. You must pass the time interval for the analysis (2 strings of 'date')

  ```python
  check_extension('date_init','date_end')
  ```  

  The function returns a variable with the content written in markdown format

- **title_commits()**  
  Searches all commit titles, by user, thus facilitating the visualization of what each contributor has done (Requires a time interval) 2 strings 'data'

  ```python
  title_commits('date_init','date_end')
  ```  

  The function returns a variable with the content written in markdown format  

- **gerenate_report()**  
  Combines the functions of commit with coauthor and overall average to generate a more complete report. The function receives as parameter 2 date strings with the time interval to be analyzed ('initial_date','final_date')

  ```python
  gerenate_report('date_init','date_end')
  ```  

  Generates a "gitInfo_report.md" markdown with information about commits with coauthor and the number of commits per user

- **issues_open()**  
  Searches all Issues that are open but have not yet been signed by anyone. It takes nothing as a parameter.

  ```python
  issues_open()
  ```  

  The function returns a variable with the content written in markdown format  