# Disneyland-Review-Analyzer
The artifact development involves data analysis, visualization, and user-friendly interaction, focusing on monthly ratings, location-based insights, and review trends.

# Overview
This project is designed to analyze Disneyland review data, providing insightful visualizations and detailed statistics about customer feedback. The program allows users to interact with the data through a menu-driven interface, offering options for viewing, analyzing, and visualizing the data.

# Features
View Data: View reviews by park, count reviews by location, and calculate average scores by year or location.
Visualize Data: Generate pie charts of reviews, bar charts of average scores, top locations, and monthly ratings.
User-Friendly Interface: Simple text-based menu for easy navigation through available options.
# Requirements
Before running the project, ensure you have the following libraries installed:

pandas - for data manipulation and analysis
matplotlib - for plotting visualizations

### pip install pandas matplotlib
# Dataset
The dataset contains the following columns:

Review_ID: Unique identifier for each review
Rating: Review rating (1-5 scale)
Year_Month: Date of the review (year and month)
Reviewer_Location: Location of the reviewer (e.g., country)
Branch: Disneyland branch (e.g., Disneyland Paris, Disneyland Hong Kong)

# Code Structure
main.py: The main program file that handles user input and calls the relevant functions from other modules.
process.py: Contains functions for processing the data, such as filtering by park, year, or location, and calculating average ratings.
visual.py: Contains functions for generating visualizations like pie charts and bar charts.
tui.py: Handles the text-based user interface (TUI) and menu options.
Example Output
Visualization Options:
Pie chart of reviews
Bar chart of average scores
Top locations bar chart
Monthly ratings bar chart
Example of Monthly Ratings Bar Chart:

# Contributing
Feel free to fork this repository, raise issues, or submit pull requests with improvements.

# License
This project is licensed under the MIT License.
