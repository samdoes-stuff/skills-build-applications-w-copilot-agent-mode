# OctoFit Tracker

## Overview
The OctoFit Tracker is a fitness application designed to help users track their activities, manage their fitness goals, and connect with others in a competitive environment. The app includes features such as user authentication, activity logging, team management, a competitive leaderboard, and personalized workout suggestions.

## Project Structure
The project is structured as follows:

```
octofit-tracker/
├── backend/
│   ├── venv/                     # Python virtual environment
│   ├── requirements.txt           # Required Python packages
│   ├── manage.py                  # Command-line utility for Django
│   ├── octofit_tracker/           # Main Django application
│   │   ├── __init__.py
│   │   ├── settings.py            # Django settings and configuration
│   │   ├── urls.py                # URL patterns for the application
│   │   ├── wsgi.py                # WSGI entry point
│   │   └── asgi.py                # ASGI entry point
│   └── apps/                      # Django apps for modular functionality
│       ├── users/                 # User management app
│       │   ├── __init__.py
│       │   ├── models.py          # User models
│       │   ├── views.py           # User views
│       │   ├── serializers.py      # User serializers
│       │   └── urls.py            # User URL patterns
│       └── activities/             # Activity tracking app
│           ├── __init__.py
│           ├── models.py          # Activity models
│           ├── views.py           # Activity views
│           ├── serializers.py      # Activity serializers
│           └── urls.py            # Activity URL patterns
├── frontend/                      # Frontend application
│   ├── package.json               # Frontend dependencies and scripts
│   └── src/                       # Source files for the frontend
│       ├── App.jsx                # Main entry point for the frontend
│       └── components/            # Additional frontend components
└── README.md                      # Project documentation
```

## Setup Instructions

### Backend Setup
1. **Create a Python Virtual Environment:**
   Navigate to the `backend` directory and create a virtual environment:
   ```bash
   python3 -m venv venv
   ```

2. **Activate the Virtual Environment:**
   ```bash
   source venv/bin/activate
   ```

3. **Install Required Packages:**
   Install the necessary Python packages listed in `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations:**
   Apply database migrations:
   ```bash
   python manage.py migrate
   ```

5. **Start the Development Server:**
   Run the Django development server:
   ```bash
   python manage.py runserver
   ```

### Frontend Setup
1. **Install Frontend Dependencies:**
   Navigate to the `frontend` directory and install the dependencies:
   ```bash
   npm install
   ```

2. **Start the Frontend Development Server:**
   Run the frontend application:
   ```bash
   npm start
   ```

## Usage
- Users can create profiles, log activities, and join teams.
- The app provides a leaderboard to encourage competition among users.
- Personalized workout suggestions are available based on user activity and preferences.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License.