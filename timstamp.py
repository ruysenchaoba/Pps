import datetime

def display_timestamp():
    # Get the current timestamp
    current_timestamp = datetime.datetime.now()
    # Format the timestamp as a string
    formatted_timestamp = current_timestamp.strftime('%Y-%m-%d %H:%M:%S')
    print(f"Current Timestamp: {formatted_timestamp}")

if __name__ == "__main__":
    display_timestamp()
