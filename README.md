# Sentiment-Analysis-Project



Sentiment Analysis Project

Overview
This prototype application is designed to enhance customer support at BT PLC through sentiment analysis.
It allows users to upload customer reviews, analyze sentiment, and export results for further use.

How to Run:
To run application, open a new terminal and enter the command:
Streamlit run app/app.py

To run all tests, open a new terminal and run the command:
pytest tests/

User Guide
1. Login Page
- Enter your email and password to log in. 
- If you don’t have an account, sign up by providing an email and password.
- You may use a dummy account if you wish, the credentials for this are:
  username - tester@gmail.com
  password - 111111

2. Uploading Data
- Ensure your file is in CSV format with the following required columns: Rating, Title, Text, ASIN, User ID
- The format aligns with datasets from Hugging Face and will be compatible with BT’s system upon professional integration.
- Upload your CSV file via the Upload page, which is the first screen that loads after logging in.
- A template File (reviews_file.csv) populated with the dummy data in the required format is available in processing.data, 
  this will be used by default by the application if unchanged.

3. Dashboard
- Navigate to the Dashboard via the side navigation bar.
- A bar chart summarizing sentiment distribution will be displayed.
- This helps quickly assess overall customer feedback sentiment.

4. View Analysis
- Navigate to the View Analysis page via the side navigation bar.
- A table displaying sentiment scores for each review will be shown.
- This allows quick assessment of positive, neutral, and negative feedback.
- Below this table, an dropdown menu will allow the selection of a review,
- Once a review is selected, an automated response can be generated for that review.

5. Detailed Analysis
- Navigate to the Detailed Analysis page.
- A table with additional details, including sentiment classification, will be displayed.
- Search filters are provided below which are able to refine results based on ASIN or USER id.
- This will help users locate specific feedback easily.

6. Exporting Data
- Navigate to the Export page.
- Click the Download button to export sentiment analysis results.
- This allows for storage or integration with other systems for further use.