# Neighborhood Preference Prediction
Predict whether a traveler will enjoy a location based on neighborhood venue categories using Foursquare API and clustering analysis

## Table of Contents
- [Project Background](#project-background)
- [Project Goal](#project-goal)
- [File Structure](#file-structure)
- [Instructions](#instructions)
  - [1. Packages Used](#1-packages-used)
  - [2. Toronto Venue Clustering](#2-toronto-venue-clustering)
    - [2.1 Datasets Used](#21-datasets-used)
    - [2.2 Foursquare Data Retrieval](#22-foursquare-data-retrieval)
    - [2.3 Clustering](#23-clustering)
  - [3. Location Rating Prediction](#3-location-rating-prediction)
    - [3.1 Datasets Used](#31-datasets-used)
    - [3.2 Geological Data Retrieval](#32-geological-data-retrieval)
    - [3.3 Foursquare Data Retrieval](#33-foursquare-data-retrieval)
    - [3.4 Model Building](#34-model-building)
    - [3.5 Testing Data Prediction](#35-testing-data-prediction)
- [Future Improvements](#future-improvements)
- [Acknowledgements](#acknowledgements)
- [License](#license)

## Project Background
Travelers often rate destinations based on their surrounding neighborhood venue categories: vibrant areas with restaurants and shops are praised, while places lacking essential services are criticized. This project analyzes how neighborhood venue categories influence visitor satisfaction and explores whether preferences across locations reveal common patterns. By clustering neighborhood venue data, this project aims to predict whether a traveler is likely to enjoy a destination, providing insights for personalized recommendations and travel planning.

## Project Goal
This project aims to analyze neighborhood characteristics using **Python Jupyter Notebook** and the [*Foursquare API*](https://foursquare.com), identifying patterns that influence traveler preferences. By clustering venue data, it predicts how likely a visitor is to enjoy a given location, enabling scalable, data-driven insights for personalized travel recommendations.

## File Structure
Configuration & Metadata:
- `README.md` – project overview
- `LICENSE.txt` – license information
- `.gitignore` – git ignore config
- `.gitattributes` – git attributes config

Core Logic:
- `foursquare_api.py` – python script for getting venue data from [*Foursquare API*](https://foursquare.com)
- `location_rating.csv` – personal rating of locations CSV file
- `toronto_venue_clustering.ipynb` – notebook for clustering Toronto venues
- `location_rating_prediction.ipynb` – notebook for clustering Toronto venues

## Instructions

### 1. Packages Used
- `pandas`, `np`, `re`: for data manipulation
- `requests`, `os`: for basic system operations
- `dotenv`: for loading environment variables from a `.env` file
- `matplotlib`: for data visualization
- `folium`: for interactive map creation
- `geopy`: for getting the geological data
- `sklearn`: for modeling

### 2. Toronto Venue Clustering
Location data for Toronto, Canada is retrieved from Wikipedia. Neighborhoods are clustered based on nearby venue types using the [*Foursquare API*](https://foursquare.com). After converting venue categories to dummy variables, KMeans clustering is applied to group similar neighborhoods. Results are visualized on an interactive map.

#### 2.1 Datasets Used
The dataset of Toronto's postal codes and boroughs is scraped from Wikipedia. After removing unassigned rows, neighborhoods belonging to the same postal code are combined. Duplicate rows are also dropped to ensure clean data.

To obtain the geographical coordinates (latitude and longitude) of each postal code, a separate dataset is loaded from a provided CSV URL. The two datasets are merged to form a new DataFrame with the following structure:
- `postcode`: The postal code
- `borough`: The administrative division
- `neighbourhood`: One or more neighborhoods associated with the postal code
- `latitude` and `longitude`: The geographic coordinates of the postal code

#### 2.2 Foursquare Data Retrieval
Foursquare venue data is retrieved using the [*Foursquare API*](https://foursquare.com) for each postal code's latitude and longitude. The API returns up to 50 nearby venues sorted by distance from the given coordinates.

Each venue's category information is extracted and transformed into dummy variables. These dummy variables are then grouped by postal code and averaged to represent the neighborhood profile for each area. The final dataset is a combination of geographic and categorical features, with each row representing a unique postal code and its surrounding venue composition.

#### 2.3 Clustering
KMeans clustering is applied to the venue dummy variables to identify similar neighborhoods in Toronto. Each postal code is assigned to a cluster based on its surrounding venue composition. The results are visualized on an interactive map, where each neighborhood is colored according to its cluster membership.

### 3.Location Rating Prediction
It is assumed that the factors that affect a person’s favor to a place is the neighborhood features. This section will use myself as an object to find out the neighborhood features of the places I have stayed. In addition, I will try to predict my like or dislike to a random place I have never been to.

#### 3.1 Datasets Used
As the subject of this study, a simple dataset is created consisting of places I’ve stayed and my personal ratings (on a scale from 1 to 10, where 10 is the highest). An example of the dataset is shown below:

| Location                                  | Rating |
|-------------------------------------------|--------|
| Baltimore, Maryland, the United States    | 6      |
| Beijing, China                            | 3      |
| Boston, Massachusetts, the United States  | 5      |
| Cambridge, United Kingdom                 | 8      |
| Chengdu, China                            | 5      |

This table is uploaded as `location_rating.csv`. It is read as a DataFrame and serves as the foundation for testing how neighborhood attributes correlate with my personal ratings.

### 3.2 Geolocation Data Retrieval
To support further analysis, geographic coordinates are retrieved for each location in the dataset. These coordinates are then visualized on a Folium map, with markers indicating each location and its corresponding rating.

#### 3.3 Foursquare Data Retrieval
The same method described in Section 2.2 is applied here to retrieve venue data based on each location's latitude and longitude. Venue categories are transformed into dummy variables, then aggregated to represent the venue profile for each rated location.

#### 3.4 Model Building
For each location, these dummy variables are aggregated to represent the neighborhood features, forming the input features for the predictive model.

Then, a linear regression model is constructed using the aggregated venue features as independent variables and the location rating as the dependent variable.

#### 3.5 Testing Data Prediction
A test city is used as input, and its latitude, longitude, and venue data are retrieved as features. Venue categories are converted into dummy variables to align with the training format, and these features are fed into the trained model to predict the location rating.

## Future Improvements
- **Data Expansion**: Incorporate more rated locations and user data to improve model generalization and reduce bias from personal preferences.
- **Venue Data Optimization**: Implement multi-radius [*Foursquare API*](https://foursquare.com) queries or pagination to retrieve a more comprehensive set of nearby venues for each location to avoid the 50 venues limit.
- **Enhanced Feature Engineering**: Include additional contextual features such as population density, average income, or urban development index to enrich neighborhood profiles.
- **Advanced Modeling Techniques**: Apply non-linear models such as Random Forest, XGBoost, or Neural Networks to better capture complex patterns in the data.

## Acknowledgements
- This project was inspired by the [*IBM Data Science Professional Certificate*](https://www.coursera.org/professional-certificates/ibm-data-science?utm_medium=sem&utm_source=gg&utm_campaign=b2c_namer_ibm-data-science_ibm_ftcof_professional-certificates_px_dr_bau_gg_pmax_pr_us-ca_en_m_hyb_23-04_nonNRL-within-14d&campaignid=19995348162&adgroupid=&device=c&keyword=&matchtype=&network=x&devicemodel=&creativeid=&assetgroupid=6490614053&targetid=&extensionid=&placement=&gad_source=1&gad_campaignid=19995375522&gbraid=0AAAAADdKX6YnCN4VNzyhe_JVqK6VgRwNM&gclid=CjwKCAjwv5zEBhBwEiwAOg2YKGmhLxKP-AF1b0s6mmCWTGecU0-5V39rjF-q_dJLRxBG1ph3PZ-7_BoCmfMQAvD_BwE) Capstone on [*Coursera*](https://www.coursera.org/).
- Thanks to [*Foursquare*](https://foursquare.com) for providing the venue data access API.
- Thanks to [*Wikipedia*](https://en.wikipedia.org/wiki/Main_Page) for providing the postal code and neighborhood data for Toronto in [*List of postal codes of Canada: M*](https://en.wikipedia.org/w/index.php?title=List_of_postal_codes_of_Canada:_M&oldid=926306543).
- Thanks to [`geopy`](https://pypi.org/project/geopy/) for providing location geocoding services.
- Thanks to [`folium`](https://pypi.org/project/folium/) for enabling interactive map visualization.

## License
This project is licensed under the MIT License - see the [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/leopengningchuan/Coursera_Capstone?tab=MIT-1-ov-file) file for details.
