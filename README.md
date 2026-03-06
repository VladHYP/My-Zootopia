# My-Zootopia

My-Zootopia is a Python project that generates a simple animal website using data from the API Ninjas Animals API.

The program fetches information about animals and dynamically generates an HTML page displaying details such as diet, location, and type.

## Installation

Clone the repository and install the required dependencies:

pip install -r requirements.txt

## Usage

Run the program:

python animals_web_generator.py

Enter the name of an animal when prompted. The program will fetch data from the API and generate a webpage called animals.html.

## Project Structure

animals_web_generator.py – generates the HTML website  
data_fetcher.py – retrieves animal data from the API  
requirements.txt – project dependencies  
.env – stores the API key (not included in the repository)

## API

This project uses the API Ninjas Animals API to retrieve animal data.