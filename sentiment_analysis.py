import pandas as pd
import ollama

# Assuming LLAMA_PROMPT is defined in CONFIG
from CONFIG import LLAMA_PROMPT

def group_comments(data_path, data_stop):
    """
    Analyzes the comments data from a CSV file.
    
    Parameters:
    - data_path: str, path to the CSV file containing the data.
    - data_stop: str, the cutoff date (inclusive) for filtering the data in 'YYYY-MM-DD' format.
    
    The CSV file must contain the following columns:
    - "user": str, user ID
    - "comment": str, the comment text
    - "created_utc": date, the date of the comment in 'YYYY-MM-DD' format
    - "score": int, the score of the comment
    
    Returns:
    - A DataFrame with the comments grouped by user.
    """
    try:
        # Reading the dataframe from the CSV file
        data = pd.read_csv(data_path)
    except Exception as e:
        print("Invalid datapath:", e)
        return None

    # Convert 'created_utc' to datetime and extract only the date
    try:
        data['created_utc'] = pd.to_datetime(data['created_utc']).dt.date
    except Exception as e:
        print("Error converting 'created_utc' to date:", e)
        return None

    # Convert 'data_stop' to date
    try:
        data_stop = pd.to_datetime(data_stop).date()
    except Exception as e:
        print("Invalid data_stop format:", e)
        return None

    # Filter based on data_stop
    try:
        filtered_data = data[data['created_utc'] <= data_stop]
    except Exception as e:
        print("Error filtering data:", e)
        return None

    # Group by user and make a list of comments for each user
    try:
        grouped_data = filtered_data.groupby("user").agg({"comment": list}).reset_index()
    except Exception as e:
        print("Error grouping data:", e)
        return None

    return grouped_data

def sentiment_analysis(data_path, data_stop):
    """
    Analyzes the comments data from a CSV file.
    
    Parameters:
    - data_path: str, path to the CSV file containing the data.
    - data_stop: str, the cutoff date (inclusive) for filtering the data in 'YYYY-MM-DD' format.
    
    The CSV file must contain the following columns:
    - "user": str, user ID
    - "comment": str, the comment text
    - "created_utc": date, the date of the comment in 'YYYY-MM-DD' format
    - "score": int, the score of the comment
    
    Returns:
    - A DataFrame with the sentiment analysis labels.
    """
    eval = {}

    grouped_data = group_comments(data_path, data_stop)
    if grouped_data is None:
        print("Error in grouping comments.")
        return None
    
    comments_dict = {user: comments for user, comments in zip(grouped_data["user"], grouped_data["comment"])}

    for user in list(comments_dict.keys())[:2]:
        print(f"Running sentiment analysis for user:{user}")
        eval[user] = []   
        for comment in comments_dict[user]:
            
            try:
                response = ollama.chat(
                    model="llama3",
                    messages=[
                        {"role": "system", "content": LLAMA_PROMPT},
                        {"role": "user", "content": comment}
                    ]
                )
                label = response["message"]["content"]
                eval[user].append(label)
            except Exception as e:
                print(f"Error processing comment for user {user}: {e}")
                eval[user].append("Error processing comment")

    return eval

# Example usage:
data_path = "data/filtered_comments.csv"
data_stop = "2024-03-22"
result = sentiment_analysis(data_path, data_stop)
print(result)