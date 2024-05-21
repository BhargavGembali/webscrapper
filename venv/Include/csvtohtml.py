import pandas as pd

def csv_to_html(csv_file, html_file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file)
    
    # Convert the DataFrame to an HTML table
    html_table = df.to_html(index=False, classes='table table-striped')

    # Define a basic HTML structure
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Restaurants Ratings</title>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
    </head>
    <body>
        <div class="container">
            <h1 class="mt-5"Restaurants Ratings</h1>
            {html_table}
        </div>
    </body>
    </html>
    """

    # Write the HTML content to a file
    with open(html_file, 'w') as file:
        file.write(html_content)

# Example usage
if __name__ == '__main__':
    csv_file = 'restaurants.csv'  # Replace with your CSV file name
    html_file = 'restaurant_rating.html'  # Output HTML file name
    csv_to_html(csv_file, html_file)
    print(f"HTML file '{html_file}' has been generated.")
