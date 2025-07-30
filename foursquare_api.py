# import packages
import pandas as pd
import json, requests


# write the function of getting venues from Foursquare
def fetch_foursquare_raw(api_key, lat, long, radius, limit):
    
    # define the url, header, parameters
    url = "https://api.foursquare.com/v3/places/search"
    headers = {"Accept": "application/json", "Authorization": f"Bearer {api_key}"}
    params = {"ll": f"{lat},{long}", "radius": radius, "limit": limit, "sort": "DISTANCE"}
    
    # get the response
    response = requests.get(url, headers = headers, params = params)
    
    # raise status
    response.raise_for_status()
    
    # return the result 
    return response.json()['results']


def fetch_foursquare_venues(api_key, df, lat_col, lon_col, radius = 1000, limit = 50):
    
    # create an empty venue list
    venues_list = []

    # loop all the latitudes and longitudes in the df
    for lat, lon in zip(df[lat_col], df[lon_col]):

        # get the raw data from the Foursquare API
        raw_data = fetch_foursquare_raw(api_key, lat, lon, radius, limit)

        # get the useful venue data
        for v in raw_data:
            venues_list.append({
                lat_col: lat,
                lon_col: lon,
                "venue_fsq_id": v.get('fsq_id', None),
                "venue_name": v.get('name', None),
                "venue_main_lat": v['geocodes']['main']['latitude'] if 'geocodes' in v else None,
                "venue_main_lon": v['geocodes']['main']['longitude'] if 'geocodes' in v else None,
                "venue_distance": v.get('distance', None),
                "venue_category": [c['name'] for c in v.get('categories', [])] if v.get('categories') else [],
                "venue_location_address": v['location'].get('address', None),
                "venue_location_locality": v['location'].get('locality', None),
                "venue_location_region": v['location'].get('region', None),
                "venue_location_postcode": v['location'].get('postcode', None),
                "venue_location_country": v['location'].get('country', None),
                "venue_location_formatted_address": v['location'].get('formatted_address', None),
                "venue_timezone": v.get('timezone', None),
                "venue_likely_open": v.get('closed_bucket', None)
            })

    # combine the data to the original df
    venue_data = pd.merge(df, pd.DataFrame(venues_list), on = [lat_col, lon_col], how = 'left')

    # return the final data
    return venue_data