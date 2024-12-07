
Preview Image

![image](https://github.com/user-attachments/assets/3d12122d-dafd-40cb-8a16-1f752646d4b1)

 
 
 
 
 
 


 
 🌟 Attentions-AI: One-Day Tour Planning Application 🌍

A dynamic, AI-powered Streamlit application designed to help users plan the perfect one-day trip. This tool combines the power of **Generative AI (Gemini model)**, **OpenWeather API**, and a **graph-based memory system** to deliver personalized itineraries and optimize trip planning.

---

Features 🚀

1. **User Interaction**  
   - Gather user preferences such as city, budget, interests, and starting point.

2. **AI-Generated Itinerary**  
   - Use the Gemini Generative AI model to craft detailed, personalized one-day trip plans.

3. **Itinerary Optimization**  
   - Enhance itineraries to meet constraints like budget and minimize travel time.

4. **Weather Forecast**  
   - Fetch real-time weather data for destinations using the OpenWeather API.

5. **Memory Management**  
   - Store and retrieve user preferences with a graph-based memory system for a seamless user experience.

---

## Requirements 📦

### Libraries
- **Streamlit**: For building the interactive user interface.
- **Requests**: For communicating with external APIs.
- **NetworkX**: For managing user preferences in a graph structure.
- **Google Generative AI SDK**: For utilizing the Gemini AI model.

### APIs
- **Gemini Generative AI**: To generate and optimize itineraries.
- **OpenWeather API**: For fetching live weather data.

---

## Installation 🛠️

1. **Clone this repository**:  
   ```bash
   git clone https://github.com/your-username/one-day-tour-planner.git
   cd one-day-tour-planner
   ```

2. **Install dependencies**:  
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up API keys**:  
   - Replace `genai.configure` in the code with your **Gemini API key**.
   - Update the `OPENWEATHER_API_KEY` constant with your **OpenWeather API key**.

4. **Run the application**:  
   ```bash
   streamlit run app.py
   ```

---

## How It Works 🌍

1. **Step 1: Provide Preferences**  
   - Enter details like city, budget, interests, and starting point.

2. **Step 2: Generate Initial Itinerary**  
   - Click "Generate Initial Itinerary" to receive a personalized one-day trip plan.

3. **Step 3: Optimize Itinerary**  
   - Click "Optimize Itinerary" to refine the plan based on time and budget constraints.

4. **Step 4: Fetch Weather**  
   - Click "Fetch Weather" to get real-time weather details for your destination.

5. **Step 5: View Memory**  
   - View saved preferences for reuse or further refinement.

---

## File Overview 📂

- **`app.py`**: Main application containing the core logic for interaction, itinerary generation, optimization, and weather fetching.
- **`requirements.txt`**: File listing project dependencies.

---

## Example Usage 🧑‍💻

### Inputs
- City: **Paris**  
- Budget: **$500**  
- Interests: **culture, food**

### Workflow
1. Generate an initial itinerary using AI.  
2. Optimize the itinerary for budget and time constraints.  
3. Fetch real-time weather for Paris.  
4. View stored preferences for refinement or reuse.

---

## Future Enhancements 🌟

- Add support for multi-day itineraries.  
- Integrate transportation options with real-time pricing.  
- Enhance memory management with detailed user insights.

---

## Contributing 🤝

Contributions are welcome! Fork this repository and submit a pull request with improvements or bug fixes.

---

## License 📜

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Contact 📧

For questions or feedback, feel free to reach out:  
**Email:** [your.email@example.com](mailto:your.email@example.com)
```









