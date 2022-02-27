# Billboard-Statistical-Study
Data collection and analysis tool that interfaces with Spotify's web APIs to determine if there is a statistically significant difference in the mean length of songs that make the Billboard Top 100, versus the songs that do not. 

This project was written in Python and created by Aidan Bowers, Abby Chan, and Matthew Kee for the University of Waterloo's SYDE 212 statistical study.

## Process
We began by exporting the song titles and artist names from the Billboard Hot 100 playlists from 2010-2019 into one large CSV, which constitutes a population of 1,000 songs. We then used the artist and song names to query Spotify for the song data, which includes the song's duration in milliseconds. Next, we filtered the list to eliminate duplicates, and used a random number generator to select a sample of 300 unique Billboard Hot 100 songs, which we wrote to a CSV. 

We then queried Spotify for **all** of the songs that were released by Hot 100 artists from 2010 to 2019, and eliminated duplicates between lists until we had our second population of interests: songs released by Hot 100 artists that did **not** make the Billboard Hot 100 list. We then used a random number generator to select a sample of 300 unique songs from this second population, which we wrote to a CSV.

Finally, we analyzed the data in our two samples, compared variance and standard deviation, and plotted the data into histograms and box and whisker plots. To make our conclusion, we calculated the mean song duration in both samples, then calculated a 95% confidence interval and conducted a hypothesis test to determine if there was a statistically significant difference between the mean length of songs that made the Billboard Hot 100 versus the songs that did not.

This project was the core of our larger statistical study, which followed the PPDAC statistical method and culminated in an 8-page report. 
