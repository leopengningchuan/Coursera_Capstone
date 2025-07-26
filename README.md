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
- `foursquare_api.py` – python script for getting Foursquare API data
- `location_rating.csv` – personal rating of locations CSV file
- `toronto_venue_clustering.ipynb` – notebook for clustering Toronto venues
- `location_rating_prediction.ipynb` – notebook for clustering Toronto venues

## Instructions

### 1. Packages Used
- `pandas`, `np`, `re`: for data manipulation
- `requests`, `os`: for basic system operations
- `dotenv`: for loading environment variables from a `.env` file
- `matplotlib`, `folium`: for data visualization and map creating
- `geopy`: for getting the geological data
- `sklearn`: for modeling

### 2.Toronto Venue Clustering


### 3.Location Rating Prediction
It is assumed that the factors that affect a person’s favor to a place is the neighborhood features. This section will use myself as an object to find out the neighborhood features of the places I have stayed. In addition, I will try to predict my like or dislike to a random place I have never been to.

#### 3.1 Datasets Used
As the subject of this study, I created a simple dataset consisting of places I’ve stayed and my personal ratings (on a scale from 1 to 10, where 10 is the highest). An example of the dataset is shown below:

| Place                      | Rating |
|----------------------------|--------|
| Baltimore, United States   | 6      |
| Beijing, China             | 3      |
| Boston, United States      | 5      |
| Cambridge, United Kingdom  | 8      |
| Chengdu, China             | 5      |

This table is uploaded as `location_rating.csv`. It is read as a DataFrame and serves as the foundation for testing how neighborhood attributes correlate with my personal ratings.

#### 3.2 Geological Data Getting

#### 3.3 Foursquare Data getting

#### 3.4 Model Building

#### 3.5 Testing Data




### 3. Location Rating Prediction

This section assumes that neighborhood features significantly influence a person's preference for a place. In this capstone project, I use myself as the subject to identify the neighborhood characteristics of places I have lived in, and explore whether those features can help predict my preference for a new, unfamiliar location.

#### 3.1 Datasets Used


















## Future Improvements

## License
This project is licensed under the MIT License - see the [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/leopengningchuan/Coursera_Capstone?tab=MIT-1-ov-file) file for details.
