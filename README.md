# Movie Recommendation System

## Overview

This project is a Movie Recommendation System built using Python and Streamlit, designed to provide personalized movie recommendations based on content-based filtering. By leveraging the TMDB (The Movie Database) dataset from Kaggle, the system recommends the top 5 movies similar to a user-selected movie, utilizing cosine similarity scores derived from movie metadata. The application also fetches movie poster images via the TMDB API for an engaging user experience, displaying recommendations with titles and posters in a sleek Streamlit interface.

This project showcases skills in data preprocessing, natural language processing (NLP), machine learning (cosine similarity), API integration, and web app development, making it a robust demonstration of end-to-end data science and software engineering capabilities.

## Features

- User-Friendly Interface: Built with Streamlit, the app allows users to select a movie from a dropdown menu and instantly view the top 5 recommended movies.
- Content-Based Filtering: Recommendations are generated using cosine similarity scores computed from movie metadata (title, overview, cast, crew, and genres).
- Poster Integration: Fetches and displays movie posters dynamically via the TMDB API for a visually appealing experience.
- Efficient Data Handling: Utilizes preprocessed data stored in pickle files for fast loading and recommendation generation.
- NLP Preprocessing: Applies Snowball Stemming to standardize text data, ensuring accurate vectorization for similarity computation.

## Dataset
The dataset used in this project is sourced from the TMDB dataset on Kaggle. The raw data was cleaned and processed to extract relevant columns, including:

Title: Movie title.
Keywords: Movie related keywords
Overview: A brief description of the movie.
Cast: Key actors in the movie.
Crew: Key crew members (e.g., director).
Genres: Movie genres.

## Data Preprocessing

- Data Cleaning: Removed irrelevant columns, handled missing values, and standardized text data to ensure consistency.
- Feature Engineering: Combined the title, overview, cast, crew, and genres columns into a single text field for each movie to create a comprehensive feature set.
- Text Preprocessing:
Applied Snowball Stemming (using the NLTK library) to reduce words to their root form (e.g., "running" → "run"), improving the quality of text vectorization.
- Cosine Similarity: Computed cosine similarity scores between all pairs of movies based on their TF-IDF vectors, generating a similarity matrix.
- Data Export: Saved the processed movie data and cosine similarity matrix as pickle files (movies.pkl and similarity.pkl) for efficient loading in the Streamlit app.

Note: Due to the large size of the pickle files, they are not included in the GitHub repository. Users must download them from the provided Google Drive link and place them in the artifacts folder.

## Recommendation Logic
The recommendation system operates as follows:

- The user selects a movie from a dropdown menu in the Streamlit app.
- The app retrieves the cosine similarity scores for the selected movie from the similarity.pkl file.
- The top 5 movies with the highest similarity scores are identified.
- For each recommended movie, the app uses the movie's TMDB ID (stored in movies.pkl) to make an API call to the TMDB database and fetch the poster image.
- The recommendations are displayed with the movie titles and their corresponding posters.

## Streamlit App
The Streamlit app provides an intuitive interface for users to interact with the recommendation system:

- Movie Selection: A dropdown menu lists all movies from the dataset.
- Recommendation Display: Shows the top 5 recommended movies with their titles and posters.
- API Integration: Dynamically fetches movie posters using the TMDB API, enhancing the visual -appeal.

## TMDB API Integration
To display movie posters, the app makes API calls to the TMDB API using the movie ID stored in the movies.pkl file. Users must provide their own TMDB API key by:

Creating a .env file in the project root directory.
Adding the following line to the .env file:TMDB_API_KEY=your_api_key_here


The app uses the python-dotenv library to load the API key securely and make authenticated requests to the TMDB API.

To obtain a TMDB API key, visit https://www.themoviedb.org/ and follow the instructions to create an account and generate an API key.

##Installation and Setup

###Prerequisites
- Python 3.8+
- A TMDB API key (see above for instructions).
- The movies.pkl and similarity.pkl files downloaded from the Google Drive link.

###Steps
```bash
Clone the Repository:git clone https://github.com/Nivakaran-S/Movie-Recommendation.git
cd movie-recommendation-system
```

##Download Pickle Files:
Download movies.pkl and similarity.pkl from the provided GoogleDrive link.
Place both files in the artifacts folder within the project directory.


###Install Dependencies:
```bash
pip install -r requirements.txt
```

### Set Up the TMDB API Key:
- Create a .env file in the project root directory.
- Add your TMDB API key as described above.
- Run the Streamlit App:streamlit run app.py

This will launch the app in your default web browser.

## Project Structure
```
movie-recommendation-system/
├── artifacts/
│   ├── movies.pkl          # Processed movie data
│   ├── similarity.pkl      # Cosine similarity matrix
├── .env                    # File containing TMDB API key
├── app.py                  # Streamlit app script
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

## Technologies Used

- Python: Core programming language for data processing and app development.
- Pandas: Data manipulation and cleaning.
- NLTK: Snowball Stemming for text preprocessing.
- Scikit-learn: Cosine similarity computation.
- Streamlit: Web app framework for the user interface.
- Requests: Handling TMDB API calls.
- Python-dotenv: Securely loading environment variables.
- TMDB API: Fetching movie poster images.

## Future Improvements

- Hybrid Recommendations: Incorporate collaborative filtering to combine content-based and user-based recommendations.
- Advanced NLP: Use more sophisticated techniques like BERT embeddings for better text representation.
- Caching API Calls: Implement caching to reduce API calls and improve performance.
- User Feedback: Add a feedback mechanism to allow users to rate recommendations and improve the system over time.

