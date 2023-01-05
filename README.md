# Idea-Fetcher
This project uses PrettyTable, bs4, and selenium. This project fetches data from what-to-code.com and converts the data into a JSON format. 
That data is further used in the program to make a table.

Issues
- Sometimes a p tag can't be found. If that happens just rerun the python program

How The Program Works

The program works by importing bs4. That is used to create a driver and fetch the website from the url. 
After that, importing selenium allows us to get the exact data we need. Then, we convert the data to JSON format. After that, we import PrettyTable which is optional. 
we make a table with all the data and print it to the console.
