import json
import os
from datetime import datetime, timedelta

import requests


def get_weather_forecast(location):
    """
    Retrieves the weather forecast data for the specified location from the Weather API.

    Args:
        location (str): The location for which to retrieve the weather forecast.

    Returns:
        list: A list of tuples containing the forecast data for each day.
              Each tuple has the format (date, temperature, weather).
              If there is an error retrieving the forecast data, None is returned.
    """
    # API endpoint and API key
    api_endpoint = "https://api.weatherapi.com/v1/forecast.json"
    api_key = "ed98bb7703684dba8d6155527231206"  # Replace with your actual API key

    # Set up parameters for the API request
    params = {
        "key": api_key,
        "q": location,
        "days": 7,  # Get forecast for the next 7 days
    }

    try:
        # Send the API request
        response = requests.get(api_endpoint, params=params)
        response.raise_for_status()  # Raise an exception for any API errors

        # Parse the JSON response
        data = response.json()

        # Extract forecast data for each day
        forecast_data = []
        for forecast in data["forecast"]["forecastday"]:
            # Get the date of the forecast
            date = datetime.strptime(forecast["date"], "%Y-%m-%d")

            # Extract temperature and weather conditions
            temperature = forecast["day"]["avgtemp_c"]
            weather = forecast["day"]["condition"]["text"]

            # Append forecast data to the list
            forecast_data.append((date, temperature, weather))

        return forecast_data

    except requests.RequestException as e:
        print("API request error:", str(e))
    except json.JSONDecodeError as e:
        print("JSON decoding error:", str(e))
    except KeyError:
        print("Invalid API response format.")
    except Exception as e:
        print("An error occurred:", str(e))

    return None


def print_forecast_table(forecast_data):
    """
    Prints the weather forecast table for the given forecast data.

    Args:
        forecast_data (list): The forecast data to be printed.
    """
    if forecast_data is None:
        print("Failed to retrieve the forecast data.")
        return

    for forecast in forecast_data:
        date, temperature, weather = forecast
        formatted_date = date.strftime("%Y-%m-%d")
        print(
            f"Forecast for {formatted_date}: Temperature {temperature:.1f}°C, Weather: {weather}")


def save_forecast_data(forecast_data, location):
    """
    Saves the weather forecast data to a file.

    Args:
        forecast_data (list): The forecast data to be saved.
        location (str): The location for which the forecast data is saved.
    """
    if forecast_data is None:
        print("Failed to retrieve the forecast data.")
        return

    filename = f"forecast_{location}.txt"
    try:
        with open(filename, "w") as file:
            file.write("Date\t\t\tTemperature\t\t\tWeather\n")
            file.write(
                "-------------------------------------------------------------------------------\n")
            for forecast in forecast_data:
                date, temperature, weather = forecast
                formatted_date = date.strftime("%Y-%m-%d")
                file.write(
                    f"{formatted_date}\t|\t{temperature:.1f} degree celsius\t|\t{weather}\n")
        print(f"Forecast data saved to {filename}.")
    except IOError as e:
        print("IOError: An error occurred while saving the forecast data.")
        print("Error Details:", str(e))
    except Exception as e:
        print("An error occurred:", str(e))


# Main program
location = input("Enter a location: ")

forecast_data = get_weather_forecast(location)

print_forecast_table(forecast_data)

save_forecast_data(forecast_data, location)
