# Neighborhood Preference Prediction
Predict whether a traveler will enjoy a location based on neighborhood features using Foursquare API and clustering analysis

## Table of Contents
- [Project Background](#project-background)
- [Project Goal](#project-goal)
- [File Structure](#file-structure)
- [Instructions](#instructions)
- [Future Improvements](#future-improvements)
- [License](#license)

## Project Background
Travelers often rate destinations based on their surrounding neighborhoods: vibrant areas with restaurants and shops are praised, while places lacking essential services are criticized. This project analyzes how neighborhood features influence visitor satisfaction and explores whether preferences across locations reveal common patterns. By clustering neighborhood data, this project aims to predict whether a traveler is likely to enjoy a destination, providing insights for personalized recommendations and travel planning.

## Project Goal
This project aims to analyze neighborhood characteristics using **Python** and the [*Foursquare API*](https://foursquare.com), identifying patterns that influence traveler preferences. By clustering venue and amenities data, it predicts how likely a visitor is to enjoy a given location, enabling scalable, data-driven insights for personalized travel recommendations.

## File Structure
Configuration & Metadata:
- `README.md` – project overview
- `LICENSE.txt` – license information
- `.gitignore` – git ignore config
- `.gitattributes` – git attributes config

Core Logic:
- `toronto_venue_clustering.ipynb` – notebook for clustering Toronto venues

## Instructions

### Problem
It is assumed that the factors that affect a person’s favor to a place is the neighborhood features. This capstone project will use myself as an object to find out the neighborhood features of the places I have stayed. In addition, I will try to predict my like or dislike to a random place I have never been to.

### Interest
The tourist agencies will be extremely interested in clustering tourists’ favor to different places. Also, it is quite valuable for them to recommend the similar sightseeing spots to a tourist once they find out his love or hate to a certain kind of places.

## Data Acquisition and Cleaning

### Data Sources
I will use myself as an object. Therefore, I create a table of places and rating. All the places I have been to are put in the left column and my rating of each place (1-10; the higher, the better) are put in the right column. Below is an example:

| Places  | Rating |
| ------------- | ------------- |
| Baltimore, the United States | 6 |
| Beijing, China | 3 |
| Boston, the United States | 5 |
| Cambridge, the United Kingdom | 8 |
| Chengdu, China | 5 |

This table will be uploaded to the Jupyter Notebook as a data frame. I will use this data frame as the original data to test the influence of neighbors on my rating of places. In reality, more samples of people’s rating of places could be attained, much more than the test one of thirty. The more data for machine learning, the more comprehensive the model will be.

### Data Cleaning
Since the original data is created by me, the data cleaning process will be very simple. However, in reality, special processes will be needed to clean up the data in these two columns, for example, the format of place and rating.

### Feature Selection
Only two features are original features: places and ratings. One’s rating of a place is indispensable in this model. In addition, as the analysis continues, more feature will be attained: latitude and longitude of the place, venues of that place, latitude and longitude of venues and category of venues.

## Future Improvements

## License
This project is licensed under the MIT License - see the [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/leopengningchuan/Coursera_Capstone?tab=MIT-1-ov-file) file for details.
