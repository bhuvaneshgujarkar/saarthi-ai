# SaarthiAI
<p align="center">
  <img src="https://raw.githubusercontent.com/bhuvaneshgujarkar/saarthi-ai/main/logo.jpg" alt="SaarthiAI Logo" width="200"/>
</p>

<h3 align="center">An AI-Powered Dropout Prediction and Counseling System</h3>

---

**SaarthiAI** is a web-based platform designed to address the critical issue of student dropouts in educational institutions. Leveraging predictive analytics, the system identifies students who are at-risk of dropping out by analyzing various factors such as academic performance, attendance, and engagement.

This prototype, developed for the **Smart India Hackathon (SIH)**, provides a comprehensive suite for mentors and counselors to monitor student progress, visualize risk trends, and engage with students through an integrated AI chatbot. The goal is to enable timely and effective intervention, providing students with the support they need to succeed.

### ✨ Key Features

* **Role-Based Access:** Separate, tailored user flows for Mentors/Counselors and Students.
* **Mentor Dashboard:** An overview of key metrics, including total students, at-risk students, and counseling sessions.
* **Student Risk Analysis:** A detailed list of students with color-coded risk levels (High, Medium, Low).
* **Prediction Page:** Visualize dropout risk distribution and key influencing factors through dynamic graphs.
* **Interactive AI Chatbot:** A conversational AI for students to seek guidance and support.
* **Modern UI:** A clean, responsive, and dark-mode interface built with Tailwind CSS.

---

## 🚀 Built With

This project was built using the following technologies:

* **Backend:**
    * ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
    * ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
* **Frontend:**
    * ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
    * ![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)
    * ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

---

## 🏁 Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

You need to have the following software installed on your machine:
* Python 3.x
* pip (Python package installer)
* npm (Node Package Manager, comes with Node.js)

### Installation

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/bhuvaneshgujarkar/saarthi-ai.git](https://github.com/bhuvaneshgujarkar/saarthi-ai.git)
    ```
2.  **Navigate to the project directory:**
    ```sh
    cd saarthi-ai
    ```
3.  **Create and activate a Python virtual environment:**
    * On Windows:
        ```sh
        python -m venv venv
        venv\Scripts\activate
        ```
    * On macOS/Linux:
        ```sh
        python3 -m venv venv
        source venv/bin/activate
        ```
4.  **Install Python packages:**
    ```sh
    pip install -r requirements.txt
    ```
5.  **Install Node.js packages (for Tailwind CSS):**
    ```sh
    npm install
    ```

---

## 🏃‍♀️ Usage

To run the application, you need to have two terminals open simultaneously.

1.  **Terminal 1: Start the Tailwind CSS Compiler**
    This command will watch for any changes in your HTML files and automatically rebuild your stylesheet.
    ```sh
    npx tailwindcss -i ./static/css/main.css -o ./static/dist/output.css --watch
    ```

2.  **Terminal 2: Start the Flask Server**
    This command will run your main Python application.
    ```sh
    python app.py
    ```

3.  **Open the Application:**
    Open your web browser and navigate to `http://127.0.0.1:5000`

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 📧 Contact

Bhuvanesh Gujarkar - gujarkarbhuvanesh@gmail.com

Project Link: [https://github.com/bhuvaneshgujarkar/saarthi-ai](https://github.com/bhuvaneshgujarkar/saarthi-ai)