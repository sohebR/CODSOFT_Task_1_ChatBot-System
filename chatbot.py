import datetime
import wikipedia
import webbrowser
import re

# Function to greet the user based on the time of the day
def greeting():
    hr = int(datetime.datetime.now().hour)
    if hr >= 0 and hr < 12:
        print("Good Morning, Soheb!")
    elif hr >= 12 and hr < 17:
        print("Good Afternoon, Soheb!")
    else:
        print("Good Evening, Soheb!")
    print("I am Sam, your Personal Chatbot. How can I assist you today?")

# Main chatbot functionality
if __name__ == "__main__":
    greeting()
    while True:
        print("\nYou can ask me things like 'search Wikipedia,' 'open YouTube,' 'play Spotify,' or 'exit.'")
        query = input("You: ").lower()

        # Rule-based responses
        if re.search(r'\bhello\b|\bhi\b|\bhey\b', query):
            print("Sam: Hello! How can I help you?")
        elif 'how are you' in query:
            print("Sam: I'm just a chatbot, but I'm doing great! Thanks for asking.")
        elif 'wikipedia' in query:
            try:
                print("Sam: Searching Wikipedia for you...")
                query = query.replace("wikipedia", "").strip()
                answer = wikipedia.summary(query, sentences=10)
                print(f"Sam: According to Wikipedia:\n{answer}")
            except wikipedia.exceptions.DisambiguationError as e:
                print(f"Sam: Your query is too broad. Try specifying one of these options: {e.options}")
            except wikipedia.exceptions.PageError:
                print("Sam: Sorry, I couldn't find any information on that topic.")
            except Exception as e:
                print(f"Sam: Something went wrong: {e}")
        elif 'open youtube' in query:
            print("Sam: Opening YouTube...")
            webbrowser.open('https://www.youtube.com/')
        elif 'open gmail' in query:
            print("Sam: Opening Gmail...")
            webbrowser.open('https://www.gmail.com/')
        elif 'search google' in query:
            print("Sam: What would you like to search for?")
            search_query = input("Enter your search query: ")
            print("Sam: Searching Google...")
            webbrowser.open(f'https://www.google.com/search?q={search_query}')
        elif 'play spotify' in query:
            print("Sam: Opening Spotify...")
            webbrowser.open('https://open.spotify.com/')
        elif 'current time' in query or 'time now' in query:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sam: The current time is {current_time}.")
        elif 'open facebook' in query:
            print("Sam: Opening Facebook...")
            webbrowser.open('https://www.facebook.com/')
        elif 'open instagram' in query:
            print("Sam: Opening Instagram...")
            webbrowser.open('https://www.instagram.com/')
        elif 'weather' in query:
            print("Sam: Redirecting you to weather updates...")
            webbrowser.open('https://www.weather.com/')
        elif 'news' in query:
            print("Sam: Opening the latest news for you...")
            webbrowser.open('https://news.google.com/')
        elif 'bye' in query or 'exit' in query:
            print("Sam: Goodbye, Soheb! Have a great day!")
            break
        else:
            print("Sam: I'm sorry, I don't understand that. Can you rephrase?")

