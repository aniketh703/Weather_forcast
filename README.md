# Weather_forecast
The project demonstrates a Python script that retrieves weather forecast data from the Weather API, formats and prints the forecast, and saves it to a file. It imports the necessary modules (json, os, datetime, timedelta, requests)
1. `get_weather_forecast(location)`: Retrieves the weather forecast data for a specified location from the Weather API. It takes a location parameter and returns a list of tuples, each containing the forecast data for a specific day.

2. `print_forecast_table(forecast_data)`: Prints the weather forecast table for the given forecast data. It takes the forecast data as input and displays the forecast information in a table format.

3. `save_forecast_data(forecast_data, location)`: Saves the weather forecast data to a file. It takes the forecast data and the location as parameters, writes the forecast data to a text file, and prints the filename indicating where the data is saved.

The main program prompts the user to enter a location, retrieves the weather forecast data using the `get_weather_forecast()` function, prints the forecast table using `print_forecast_table()`, and saves the forecast data to a file using `save_forecast_data()`.

Note: The API key used in the code is a placeholder. You should replace it with your actual API key to ensure successful API requests.

This was my first Intership project
