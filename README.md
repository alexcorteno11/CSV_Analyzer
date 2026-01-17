CSV Analyser
An interactive CSV Analyser built with **Python**, **Pandas**, **Seaborn**, **Streamlit**, **Matplotlib** and **FPDF**
This project allows you to upload a CSV file to the web page, visualize its data and generate statistic data and graphs easily.

## Characteristics
- CSV files uploading from the web app
- Preview of the rows of the dataframe
- General information : Number of rows, name and number of columns.
- Column Analysis:
    - Numeric : mean, maximum, minimum, histogram.
    - Categoric : most frequent values and bar graphs.
- Interactive Visualization
- Allows you to export your results to PDF format including graphs.

## Project Structure

- csv_analyzer\
    - app.py        #Main code
    - requirementes #Libraries required to run the code
    - readme.md     #Project Documentation
    - data          #CSV Files as example
        - estudiantes.csv

## Instalation

1. Clone this repo
    
    git clone https://github.com/youruser/csv_analyzer.git

2. Install requirements
    pip install -r requirements.txt

3. Run the app
    streamlit run app.py

<img width="772" height="236" alt="image" src="https://github.com/user-attachments/assets/45de1cee-27ed-4f51-bfc5-1c1dadfe24e5" />
once you run the app your browser will open this page

<img width="800" height="820" alt="image" src="https://github.com/user-attachments/assets/659bbd02-92af-444a-8a7e-7edfe2df560c" />
once you upload a CSV file, the app will deploy this basic information about the file

<img width="796" height="905" alt="image" src="https://github.com/user-attachments/assets/7ba0eed3-9ffb-4564-b42a-a1c42ee52b29" />
you can interact and select which column you want to analyse, and that will deploy you information about it, as well as a graphic

<img width="779" height="797" alt="image" src="https://github.com/user-attachments/assets/cd6f4239-5371-4baa-8001-4317a0eb3254" />
If you decide to click on generate PDF youll be able to download a PDF with the data that was analysed

<img width="791" height="893" alt="image" src="https://github.com/user-attachments/assets/da30aa5b-fb56-42d7-bc66-28db614aa26b" />
This will download the PDF on your computer so that you can easily have a way to access the data

## What i learnt
-During this project i learnt a lot of things that i think have helped me improving my, coding skills as well as problem solving and logical thinking skills.
  -I learnt how to use the pandas library to manipulate data frames
  -I learnt to use libraries to improve my coding skills and to achieve project ideas i want to develop
  -I learnt how to solve Syntax errors and many other problems i found along the way, which has made me more confident about my coding skills
  -I learnt how to export data in pdf
  -I learnt how to export my project and post it on github.
  -I learnt the organization and the workflow i have to follow in order to succesfully develop a project
  -I learnt to document, my approaches and the path to the solution i had at developing this project


