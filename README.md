# Web Scraper
The goal of this project is to create a script that will accept a web site to scrape and
display the top words used within the site, then plot the results within a nicely formatted
bar plot, making it easier to understand for those looking at the data.

## Libraries/Modules Used
This project made use of the requests module, Beautiful Soup and matplotlib libraries

## Step by step Analysis

- The program will continually ask the users if they’d like to scrape a web site <br/>
- Accept the users’ input for the site they’d like to analyze.
- After that, filter out all information that isn’t useful like
  - All non-text elements, such as scripts, comments, etc.
  - All common article words and useless characters like newlines characters, empty spaces and tabs
    - *check utils module in for list of common words and feel free to add to*
- Finally, create the bar plot. The program output should look like the following:

```bash

>>> Would you like to scrape a website (y/n)? y
>>> Enter a website to analyze: https://www.python.org
>>> The top word is: python
>>> *** show bar plot ***
>>> Would you like to scrape a website (y/n)? n
>>> Thanks for analyzing! Come back again!

```
