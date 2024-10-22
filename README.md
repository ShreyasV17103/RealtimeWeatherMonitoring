# RealtimeWeatherMonitoring
This project is designed to retrieve real-time weather data from the OpenWeatherMap API and provide insightful summaries and alerts for various metropolitan cities in India. The system is capable of rolling up daily weather data, calculating key aggregates such as average, minimum, and maximum temperature, identifying dominant weather conditions, and alerting users if specific thresholds are breached. Additionally, it offers visualizations for historical trends and daily weather summaries.

Features
Real-time Data Retrieval:

Continuous retrieval of weather data from OpenWeatherMap API at configurable intervals (e.g., every 5 minutes).
Focuses on metros in India: Delhi, Mumbai, Chennai, Bangalore, Kolkata, Hyderabad.
Converts temperature data from Kelvin to Celsius or Fahrenheit (based on user preference).
Data Rollups and Aggregates:

Daily Weather Summary:
Calculates daily aggregates such as:
Average temperature
Maximum temperature
Minimum temperature
Dominant weather condition (based on most frequent weather condition or highest cumulative duration).
Stores daily summaries for historical analysis.
Alerting System:

Supports user-configurable alert thresholds for weather parameters (e.g., temperature > 35°C).
Monitors weather conditions in real time and triggers alerts when thresholds are breached.
Alerts are displayed on the console, with optional email notifications.
Visualization:

Displays visual summaries of daily weather conditions, historical weather trends, and triggered alerts.
Extensible Features:

Ability to include additional weather parameters like humidity, wind speed, etc., for more comprehensive insights.
Future support for weather forecasts and predictions.
