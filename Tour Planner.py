import streamlit as st
import os
import requests
import google.generativeai as genai
import networkx as nx

# Configure the Gemini model
genai.configure(api_key='AIzaSyAAF1cFQJy_zDZKIx8NhZuHKBExZ7mHYLM')
gemini_model = genai.GenerativeModel("gemini-1.5-flash")

# Weather API key
OPENWEATHER_API_KEY = "0ae4bf4c7bd39f11cabfb5d7d0a219ff"

# Hardcoded login credentials (for simplicity)
VALID_CREDENTIALS = {"admin": "password123", "user123": "pass123", "nikita": "nikita"}

# Helper Function
def query_model(prompt):
    response = gemini_model.generate_content(prompt)
    return response.text.strip()

# Agents
class UserInteractionAgent:
    def collect_preferences(self):
        with st.form(key="preferences_form"):
            st.subheader("Enter Your Preferences")
            city = st.text_input("City to Visit", key="city").strip()
            budget = st.text_input("Budget for the Trip", key="budget").strip()
            interests = st.text_input("Interests (e.g., culture, food, shopping)", key="interests").strip()
            starting_point = st.text_input("Starting Point (optional)", key="starting_point").strip()
            submitted = st.form_submit_button("Submit Preferences")
            if submitted:
                preferences = {
                    "city": city,
                    "budget": budget,
                    "interests": interests.split(", ") if interests else [],
                    "starting_point": starting_point or None,
                }
                st.success("Preferences submitted successfully!")
                st.session_state["preferences"] = preferences
                return preferences

class ItineraryGenerationAgent:
    @staticmethod
    def generate_itinerary(preferences):
        prompt = (
            f"Generate a detailed one-day itinerary for exploring {preferences['city']}. "
            f"Preferences: Interests include {preferences['interests']}. Budget: {preferences['budget']}. "
            f"Starting point: {preferences['starting_point'] or 'first attraction'}."
        )
        return query_model(prompt)

class OptimizationAgent:
    @staticmethod
    def optimize_itinerary(itinerary, preferences):
        prompt = (
            f"Here is the itinerary: {itinerary}. "
            f"Optimize it considering a budget of {preferences['budget']} and minimizing travel time. "
            f"Provide detailed improvements."
        )
        return query_model(prompt)

class WeatherAgent:
    @staticmethod
    def fetch_weather(city):
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                weather = data['weather'][0]['description'].capitalize()
                temperature = data['main']['temp']
                feels_like = data['main']['feels_like']
                humidity = data['main']['humidity']
                wind_speed = data['wind']['speed']

                return (
                    f"**Weather in {city.capitalize()}:**\n"
                    f"- Description: {weather}\n"
                    f"- Temperature: {temperature}°C (Feels like: {feels_like}°C)\n"
                    f"- Humidity: {humidity}%\n"
                    f"- Wind Speed: {wind_speed} m/s\n"
                )
            else:
                return f"Error fetching weather data: {response.json().get('message', 'Unknown error')}"
        except Exception as e:
            return f"An error occurred: {e}"

class MemoryAgent:
    def __init__(self):
        self.memory_graph = nx.DiGraph()

    def store_memory(self, user_id, preferences):
        if user_id not in self.memory_graph:
            self.memory_graph.add_node(user_id)
        for key, value in preferences.items():
            if value:
                self.memory_graph.add_edge(user_id, key, relation=value)

    def fetch_memory(self, user_id):
        if user_id not in self.memory_graph:
            return {}
        return {key: self.memory_graph[user_id][key]['relation'] for key in self.memory_graph.neighbors(user_id)}

# Streamlit Login Page
def login_page():
    """
    Renders the login page and validates credentials.
    """
    st.title("🔐 Login to Trip Planner Chatbot")
    st.write("Please log in to proceed.")

    username = st.text_input("Username", key="login_user").strip()
    password = st.text_input("Password", type="password", key="login_pass").strip()

    if st.button("Login"):
        # Ensure exact matching for credentials
        if username in VALID_CREDENTIALS and VALID_CREDENTIALS[username] == password:
            st.success(f"✅ Welcome, {username}!")
            st.session_state["logged_in"] = True
            st.session_state["user_id"] = username
            st.rerun()
        else:
            st.error("🚫 Invalid username or password. Please try again.")

# Main Streamlit Application
def main():
    st.sidebar.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", width=200)
    st.sidebar.title("Tour Planning App")
    
    if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
        login_page()
        return

    st.title("AI-Powered One-Day Tour Planner")
    st.markdown("Plan your perfect day trip with **AI assistance**! 🚀")

    # Initialize agents
    user_agent = UserInteractionAgent()
    itinerary_agent = ItineraryGenerationAgent()
    optimization_agent = OptimizationAgent()
    weather_agent = WeatherAgent()
    memory_agent = MemoryAgent()
    user_id = st.session_state.get("user_id", "default_user")

    preferences = user_agent.collect_preferences()

    if st.button("Generate Initial Itinerary"):
        if preferences:
            itinerary = itinerary_agent.generate_itinerary(preferences)
            st.session_state["itinerary"] = itinerary
            st.markdown("### Generated Itinerary:")
            st.info(itinerary)
        else:
            st.warning("Please provide preferences first.")

    if st.button("Optimize Itinerary"):
        itinerary = st.session_state.get("itinerary")
        if itinerary:
            optimized_itinerary = optimization_agent.optimize_itinerary(itinerary, preferences)
            st.markdown("### Optimized Itinerary:")
            st.success(optimized_itinerary)
        else:
            st.warning("Please generate the initial itinerary first.")

    if st.button("Fetch Weather"):
        if preferences and preferences.get("city"):
            weather_info = weather_agent.fetch_weather(preferences["city"])
            st.markdown("### Weather Information:")
            st.write(weather_info)
        else:
            st.warning("Please specify the city in your preferences.")

    if st.button("View Preferences"):
        memory = memory_agent.fetch_memory(user_id)
        st.markdown("### Saved Preferences:")
        st.write(memory)

if __name__ == "__main__":
    main()
