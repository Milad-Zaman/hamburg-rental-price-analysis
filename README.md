# hamburg-rental-price-analysis
Analysis of factors affecting WG and apartment rental prices in Hamburg using Web scraping
## Guidance of Codes and Data

## Web scraping
The **Scraper.py** is my codes for web scraping from the website of WG-gesucht. I wanted to collect data of price, size of the room(size), availability, apartment size and number of rooms(rooms) from ADs in Hamburg.I used Inspect in the website and found the specific address for each variables. With a function, my code can extract data of the variables from an Ad. Web scraping start from the first page of searching WGs and apartments in Hamburg and collect the data of all Ads in the page, then I repited this process page by page until page 24 because after 4 or 5 pages the website did not allowe me to scrap the data. Also I changed my source of the internt from my wifi to my cell phone several times in order to avoid this problem. Finally, I managed to collect the data from WG-gesucht and the *excel file of raw data* is **wg_gesucht_ads.xlsx**

## Data cleaning
At the first stage of data cleaning, the codes in **basic cleaning.py** remove some signs and extract the postal code of each Ads from its location.

Next, with codes in **dummy variables(location).py**, I created 4 lists of postal codes of Hamburg, for example I listed postal codes around the university of Hamburg *(near_to_uni)*. Each ad's postal code is compared to all four lists, if it appears on the list, it receives a 1, otherwise it receives a 0. Through this way I created 4 dummy variables for location.

In the final stage the codes of **converting availablity.py** convert all units of data of availablity to hours because that data are in date, day, hours and minutes. **Final_data.xlsx** is the final cleand data file for analysing.

## Analysis
In the **Data analysis.ipynb** with the data of **final_data.xlsx**, I use OLS regression model in two parts, part 1 for *Determinants of Apartment Prices* and part 2 for *Determinants of WG Listing Duration*. I explain the results in the Results.
