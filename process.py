import pandas as pd

def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print("Error: File not found.")
        return pd.DataFrame()

def view_reviews_by_branch(data):
    branch = input("Enter branch: ")
    filtered_data = data[data['Branch'] == branch]
    print(filtered_data.head())

def count_reviews_by_location(data):
    location_counts = data['Reviewer_Location'].value_counts()
    print(location_counts)

def average_score_by_year_month(data, branch, year_month):
    if 'Branch' in data.columns and 'Year_Month' in data.columns:
        filtered_data = data[(data['Branch'] == branch) & (data['Year_Month'] == year_month)]
        if not filtered_data.empty:
            average_score = filtered_data['Rating'].mean()
            print(f"Average score for {branch} in {year_month}: {average_score:.2f}")
        else:
            print(f"No data found for {branch} in {year_month}.")
    else:
        print("Error: The necessary columns are not present in the dataset.")

def average_score_by_location(data):
    location_scores = data.groupby('Reviewer_Location')['Rating'].mean()
    print(location_scores)
