# kyma
Kyma is an audio and image generation tool to help those with anxiety, depression, ptsd, or simply looking to expand their consciousness.

Kyma 🎶
Kyma is an interactive web application that allows users to generate personalized binaural beats accompanied by cymatic visualizations. The app is built using Streamlit and offers a user-friendly interface for exploring solfeggio frequencies, brainwave patterns, and emotional intentions through sound and visuals.

Table of Contents
Features
Demo
Installation
Usage
Available Frequencies and Intentions
Screenshots
Scientific Validation
Contributing
License
Acknowledgements
Features
Binaural Beats Generation: Create binaural beats using solfeggio frequencies, brainwave patterns, custom frequencies, or emotional intentions.
Cymatic Visualizations: Enjoy real-time cymatic patterns that correspond to the generated audio frequencies.
Emotional Intentions: Select from predefined emotional intentions that influence both the audio and visual outputs.
Waveform Selection: Choose from sine, square, sawtooth, or triangle waveforms for audio generation.
Audio Controls: Adjust volume, panning, and duration of the generated audio.
Download Options: Download the generated audio and cymatic visualizations as files.
Educational Content: Learn about binaural beats, brainwave entrainment, and cymatics through integrated educational resources.
Scientific References: Access a curated list of research studies related to the app's core concepts.
Demo
Check out the live demo of Kyma here (Link to the deployed app).

Installation
Prerequisites
Python 3.7 or higher
pip package manager
Clone the Repository
bash
Copy code
git clone https://github.com/yourusername/kyma.git
cd kyma
Create a Virtual Environment
bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies
bash
Copy code
pip install --upgrade pip
pip install -r requirements.txt
If requirements.txt is not available, install dependencies manually:

bash
Copy code
pip install streamlit numpy soundfile pillow scipy
Usage
Run the App Locally
bash
Copy code
streamlit run kyma_app.py
kyma_app.py: The main application script.
The app will be accessible at http://localhost:8501 in your web browser.
Navigating the App
Logo and Title: The Kyma logo and app title are displayed at the top.
Audio Controls: Use the sidebar to select frequency types, adjust audio settings, and generate binaural beats.
Cymatic Visualization: View the real-time cymatic patterns that correspond to your audio selections.
Downloads: Download the generated audio and cymatic still frames.
Educational Content: Explore scientific studies and educational resources related to binaural beats and cymatics.
Available Frequencies and Intentions
Solfeggio Frequencies
174 Hz - Foundation and Stability
285 Hz - Healing Tissues and Organs
396 Hz - Liberating Guilt and Fear
417 Hz - Facilitating Change
528 Hz - Transformation and DNA Repair
639 Hz - Harmonizing Relationships
741 Hz - Expression and Solutions
852 Hz - Awakening Intuition
963 Hz - Spiritual Connection
Brainwave Patterns
Delta (0.5 - 4 Hz)
Theta (4 - 8 Hz)
Alpha (8 - 14 Hz)
Beta (14 - 30 Hz)
Gamma (30 - 100 Hz)
Emotional Intentions
Love
Calm
Healing
Gratitude
Courage
Screenshots
Home Screen

Audio Controls

Cymatic Visualization

Note: Replace the placeholders with actual screenshots of your app.

Scientific Validation
Kyma is committed to providing an evidence-based approach to binaural beats, brainwave entrainment, and cymatics. Here are some key research studies:

Binaural Beats and Brainwave Entrainment
Lane et al. (1998)

Binaural auditory beats affect vigilance performance and mood.
Journal: Physiology & Behavior, 63(2), 249-252.
DOI: 10.1016/S0031-9384(97)00436-8
Wahbeh et al. (2007)

Binaural beat technology in humans: a pilot study to assess psychologic and physiologic effects.
Journal: The Journal of Alternative and Complementary Medicine, 13(1), 25-32.
DOI: 10.1089/acm.2006.6196
Goodin et al. (2012)

The effect of binaural beat audio on cognitive processing: a pilot study.
Journal: Current Psychology, 31(1), 125-135.
DOI: 10.1007/s12144-012-9136-5
Cymatics
Jenny (2001)
Cymatics: A Study of Wave Phenomena & Vibration.
Publisher: MACROmedia Publishing.
Disclaimer: The studies referenced are for informational purposes. Individual results may vary. Please consult a healthcare professional for personalized advice.

Contributing
Contributions are welcome! Please follow these steps:

Fork the Repository

Click the "Fork" button at the top right of the repository page.
Clone Your Fork

bash
Copy code
git clone https://github.com/yourusername/kyma.git
cd kyma
Create a Branch

bash
Copy code
git checkout -b feature/your-feature-name
Make Changes

Commit Changes

bash
Copy code
git add .
git commit -m "Add your commit message"
Push to Your Fork

bash
Copy code
git push origin feature/your-feature-name
Create a Pull Request

Navigate to the original repository and click "New Pull Request."
License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
Streamlit: For providing an amazing framework for creating interactive web apps with Python.
Community Contributors: Thank you to everyone who has contributed to the development of Kyma.
Scientific Researchers: For advancing our understanding of binaural beats and cymatics.
Enjoy your journey with sound and visuals!

Kyma © 2023. All rights reserved.
