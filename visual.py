import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Pie chart of reviews per branch
def plot_reviews_pie_chart(data):
    branch_counts = data['Branch'].value_counts()
    plt.figure(figsize=(8, 8))
    branch_counts.plot.pie(autopct='%1.1f%%', startangle=90, colors=sns.color_palette('Set3', len(branch_counts)))
    plt.title("Reviews Distribution per Branch")
    plt.ylabel('')
    plt.show()

# Bar chart of average scores for each branch
def plot_average_scores_bar_chart(data):
    avg_scores = data.groupby('Branch')['Rating'].mean()
    plt.figure(figsize=(10, 6))
    avg_scores.plot(kind='bar', color=sns.color_palette("muted", len(avg_scores)))
    plt.title("Average Ratings per Branch")
    plt.xlabel("Branch")
    plt.ylabel("Average Rating")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

# Bar chart of top reviewer locations
def plot_top_locations_bar_chart(data):
    location_counts = data['Reviewer_Location'].value_counts().head(10)
    plt.figure(figsize=(10, 6))
    location_counts.plot(kind='bar', color=sns.color_palette("viridis", len(location_counts)))
    plt.title("Top 10 Reviewer Locations")
    plt.xlabel("Location")
    plt.ylabel("Number of Reviews")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def plot_monthly_ratings_bar_chart(data):
    # Clean the 'Year_Month' column by converting it to datetime, handling errors as 'NaT'
    data['Year_Month'] = pd.to_datetime(data['Year_Month'], format='%Y-%m', errors='coerce')

    # Remove rows with 'NaT' (invalid or missing dates)
    data = data.dropna(subset=['Year_Month'])

    # Group by 'Year_Month' and calculate average rating for each month
    monthly_avg = data.groupby('Year_Month')['Rating'].mean()

    # Sort the average ratings in descending order and take the top 10 months
    top_10_months = monthly_avg.sort_values(ascending=False).head(10)

    # Plotting the bar chart for top 10 months
    plt.figure(figsize=(10, 6))
    top_10_months.plot(kind='bar', color='skyblue')
    plt.title('Top 10 Monthly Average Ratings')
    plt.xlabel('Month')
    plt.ylabel('Average Rating')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Display the plot
    plt.show()
