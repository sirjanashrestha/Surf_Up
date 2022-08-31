# Surf_Up

## Overview of the Analysis
Investor W. Avy who has equal passion for surfing is concerned about weather before investing in a surf and shake shop in Hawaii. So, the purpose of this analysis is to analyze and run analytics on weather dataset of Oahu island. For that, we will analyze the data for two months i.e. of June and December which is stored in SQLite database.

- The dependencies imported for the analysis are SQLALchemy,numpy, panda and datetime.

- Tools used for the analysis are Python, Jupyter Panda, Flask and VS Code.

- Dataset used: hawaii.sqlite

## Results
When we extracted the data from weather stations to look at the temperature in the month of June and December, we found that the average temperature of June is 74.94F which can range upto maximum 85F and minimum 64F.

<img width="164" alt="Screen Shot 2022-08-31 at 12 55 53 PM" src="https://user-images.githubusercontent.com/107566776/187736111-517b5d21-50bb-4a8c-a3ca-1f857b4aee2a.png">
<img width="511" alt="Screen Shot 2022-08-31 at 2 29 28 PM" src="https://user-images.githubusercontent.com/107566776/187753195-bcb1318d-8956-4f17-95ae-b8e75ba976b4.png">

Similarly, for the month of December the average temperature of December is 71.04F which can range upto maximum 83F and minimum 56.

<img width="144" alt="Screen Shot 2022-08-31 at 12 57 21 PM" src="https://user-images.githubusercontent.com/107566776/187736490-1124daef-7f6d-48a7-b6f4-8e2f16cff0c9.png">
<img width="529" alt="Screen Shot 2022-08-31 at 2 28 17 PM" src="https://user-images.githubusercontent.com/107566776/187753268-b89fe9fd-8de0-440b-8145-708d5c30777a.png">

Thus the result showed that;
- The average temperature throughout the year is 72.5 F.
- The temperature of June and December is similar in Oahu island.
- Temperature doesnot have much fuctuation throughout the year as standard deviation in both month is similar.

## Summary
From the results above, we can conclude that the weather of Oahu island is similar around the years making it viable to launch Surf and Shake shop in Hawaii. However, we will confirm our finding by running additional queries on weather data for June and December.For that, we have added precipitation to the results for June and December.

<img width="204" alt="Screen Shot 2022-08-31 at 2 23 17 PM" src="https://user-images.githubusercontent.com/107566776/187751959-fdd0fe0f-5fce-493a-980a-0acaa1b6b314.png"><img width="419" alt="Screen Shot 2022-08-31 at 2 23 46 PM" src="https://user-images.githubusercontent.com/107566776/187752014-d7bef950-3495-4b6f-b240-195d31de3e79.png">

<img width="260" alt="Screen Shot 2022-08-31 at 2 22 40 PM" src="https://user-images.githubusercontent.com/107566776/187752233-a7f66895-683d-4dcd-b920-99a7c4909f42.png"><img width="442" alt="Screen Shot 2022-08-31 at 2 22 11 PM" src="https://user-images.githubusercontent.com/107566776/187752258-4ad62e7e-4ac1-468a-ad0f-d68cf94d048e.png">

The average precipitation in June is 13% and in December is 21%. From this we can assume that, Ohau is usually sunny with less rainfall throughout the year and with less fluctuation in temperature. Thus, looking at the precipitation and temperature data, we can conclude that Ohau,Hawai is an ideal location to start Surf and Shake business.



