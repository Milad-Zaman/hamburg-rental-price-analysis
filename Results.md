# Analysis and Results
## Part 1: Determinants of Apartment Prices
The purpose of this analysis is to determine the factors affecting the rental prices of WG and apartments in Hamburg, Germany. As shown in the literature , there are studies that show that factors such as the size of the room or apartment and the location have an effect on the rental price (Ndegwa, 2018; Engerstam et al., 2020; Drafor Amenyah & Fletcher, 2013; Haider & Miller, 2000; Iacono & Levinson, 2011). For this purpose, the variables of size, number of rooms and location were selected from among the data collected from WG-gesucht scraping to examine their relationship with rental price. The data of these variables can be seen in the **final_data.xlsx**. OLS regression method has been used to examine this relationship, and its equation is as follows:

$$
Price = \beta_0 + \beta_1Size + \beta_2Rooms + \beta_3near-to-uni + \beta_4near-to-airport + \beta_5near-to-hbf + \beta_6near-to-city-center +  \epsilon
$$

where:
- Price: the rental price in €.
- Size : size of the room in m².
- Rooms: number of rooms
- near-to-uni: dummy variable if the location of apartment is near to the university of Hamburg 1, otherwise 0.
- near-to-airport: dummy variable if the location of apartment is near to the airport 1, otherwise 0.
- near-to-hbf: dummy variable if the location of apartment is near to the central train stiation of Hamburg 1, otherwise 0.
- near-to-city-center: dummy variable if the location of apartment is near to the city center of Hamburg 1, otherwise 0.

The results of the OLS can be seen in the first table in **Data analysis.ipynb**.

As can be seen in the table, the number of observations is 350 and it means the regression conducted with data of 350 Ads of WG and apartments in WG-gesucht in Hamburg. The intercept **(const =490.7953)** representing the baseline rental price when all other variables are zero. This is the price of an apartment that is not near any of the listed locations and has zero size and rooms, which is more of a statistical artifact rather than a practical scenario.

The **Size (2.9803)** shows that each additional square meter of the room size is associated with an increase in rent by approximately €2.98, holding other factors constant and it is significant statistically. **Rooms (18.7484)** means each additional room is associated with an increase in rent by approximately €18.75, holding other factors constant. This is also significant statistically.

Apartments near the university **(near_to_uni=50.2030)** are associated with an increase in rent by approximately €50.20, significant at the 5% level. Proximity to the airport **(near_to_airport =-0.7245)**  has a negligible and statistically insignificant effect on rent (p = 0.986). Proximity to the central train station **(near_to_hbf =11.9299)** has a positive but statistically insignificant effect on rent (p = 0.719) and **near_to_city_center (5.4630)** has a small and statistically insignificant effect on rent (p = 0.849).

Based on these results larger apartments with more rooms have higher rents, as they offer more living space and possibly more amenities. This is consistent with the economic principle that more desirable and larger housing units have higher prices. In addition apartments near the university are significantly more expensive, likely due to high demand from students and university staff. This area may have additional amenities and services catering to the university community, increasing its attractiveness and rental prices.

In conclusion, the size of the apartment, the number of rooms, and how close it is to the university are key factors in setting rental prices in Hamburg. But it also suggests that being close to the airport, the centeral train station, or the city center doesn't significantly affect rent prices. This might mean that more research or different factors need to be considered to understand their impact better.


## Part 2: Determinants of WG Listing Duration

What are the most influential variables that affect the duration a WG listing remains online? As mentioned in the literature, recent studies show that key determinants include price, size, and location, with proximity to amenities like schools and bakeries playing a significant role (Marcelo Del Cajias & Freudenreich, 2023).In this analysis I want to answer this question with the data collected from web scraping of WG-gesucht for searching WG and apartments in Hamburg. In the **final_data.xlsx**, the data of Availability-in-hours, Price, Size, Rooms and location are used for an OLS regression. The equation of regression is: 

$$
Availability-in-hours = \beta_0 + \beta_1Price + \beta_2Size + \beta_3near-to-uni + \beta_4near-to-airport + \beta_5near-to-hbf + \beta_6near-to-city-center + \beta_7Rooms +  \epsilon
$$

where:
- Availability-in-hours: the duration each Ad has been online on the WG-gesucht
- Price : the rental price in €.
- Size : size of the room in m².
- Rooms: number of rooms
- near-to-uni: dummy variable if the location of apartment is near to the university of Hamburg 1, otherwise 0.
- near-to-airport: dummy variable if the location of apartment is near to the airport 1, otherwise 0.
- near-to-hbf: dummy variable if the location of apartment is near to the central train stiation of Hamburg 1, otherwise 0.
- near-to-city-center: dummy variable if the location of apartment is near to the city center of Hamburg 1, otherwise 0.

The results of the OLS can be seen in the second table in **Data analysis.ipynb**.

The table of results of OLS shows that the intercept **(const =-86.7028)** represent the baseline availability in hours when all other variables are zero. The **(Price =-0.0708)** shows that each additional euro in rent is associated with a decrease in availability by approximately 0.07 hours, holding other factors constant and it is statistically significant. With **(Size =9.1430)**, each additional square meter of room size is associated with an increase in availability by approximately 9.14 hours, holding other factors constant. This is highly significant. The coefficient of **(Rooms=1.4313)** indicates each additional room is associated with an increase in availability by approximately 1.43 hours, but this effect is not statistically significant.

Apartments near the university **(near_to_uni =11.8292)** have an availability duration increased by approximately 11.83 hours, however, this effect is not statistically significant. Apartments near the airport **(near_to_airport =-10.9290)** have an availability duration decreased by approximately 10.93 hours, but this effect also is not statistically significant. Proximity to the central train station **(near_to_hbf =0.4044)** has a negligible and statistically insignificant effect on availability and 
proximity to the city center **(near_to_city_center =-4.2003)** has a small and statistically insignificant effect on availability.

It can be said according to the results, higher rental prices are associated with shorter availability durations. This could be because people think they are better or have nicer features. Bigger apartments stay on the market longer. This might be because they cost more overall, which makes them harder for many people to afford. Also, larger places might only appeal to a smaller group of people. The number of rooms in an apartment doesn't really change how long it takes to rent it out. This could mean that there's a good balance in what people want in terms of room count, or that the number of rooms doesn't strongly affect people's choices.

To sum up, the cost and size of the apartment are the main factors that determine how long a listing remains available online. Apartments with higher prices usually get rented more quickly, suggesting that people might think higher prices mean better quality or more features. Bigger apartments stay on the market longer because they are more expensive, which makes them harder for many people to afford. The number of rooms and proximity to various key locations (university, airport, central train station, city center) do not significantly affect the duration a listing remains available, indicating that these factors might be less critical to renters compared to the size and price of the apartment.
