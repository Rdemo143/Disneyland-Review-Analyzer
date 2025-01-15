from tui import display_menu
from process import load_data, view_reviews_by_branch, count_reviews_by_location, average_score_by_year_month, average_score_by_location
from visual import plot_reviews_pie_chart, plot_average_scores_bar_chart, plot_top_locations_bar_chart, plot_monthly_ratings_bar_chart

def main():
    data = load_data('D:/Data/disneyland_reviews.csv')
    while True:
        choice = display_menu()
        if choice == 'A':
            print("\nData View Options:")
            print("1. View reviews by branch")
            print("2. Count reviews by location")
            print("3. Average score by year and month")
            print("4. Average score by location")
            sub_choice = input("Choose a sub-option (1-4): ").strip()
            if sub_choice == '1':
                view_reviews_by_branch(data)
            elif sub_choice == '2':
                count_reviews_by_location(data)
            elif sub_choice == '3':
                branch = input("Enter branch: ")
                year_month = input("Enter year and month (YYYY-MM): ")
                average_score_by_year_month(data, branch, year_month)
            elif sub_choice == '4':
                average_score_by_location(data)
            else:
                print("Invalid sub-option. Please choose between 1 and 4.")
        elif choice == 'B':
            print("\nVisualization Options:")
            print("1. Pie chart of reviews")
            print("2. Bar chart of average scores")
            print("3. Top locations bar chart")
            print("4. Monthly ratings bar chart")
            sub_choice = input("Choose a sub-option (1-4): ").strip()
            if sub_choice == '1':
                plot_reviews_pie_chart(data)
            elif sub_choice == '2':
                plot_average_scores_bar_chart(data)
            elif sub_choice == '3':
                plot_top_locations_bar_chart(data)
            elif sub_choice == '4':
                plot_monthly_ratings_bar_chart(data)
            else:
                print("Invalid sub-option. Please choose between 1 and 4.")
        elif choice == 'X':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
