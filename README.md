# Lunchbox Project

## Inspiration
Imagine a dining experience where every detail is at your fingertips. Our platform revolutionizes how users interact with their favorite restaurants by offering real-time order tracking. From the moment your meal starts its journey in the kitchen, through the delivery process, to secure payment completion, every update is seamlessly integrated into one user-friendly interface. We’ve crafted this feature to enhance trust, convenience, and satisfaction, ensuring that every culinary journey is as smooth as it is delicious.

## How We Built It
We leveraged Python with Flask to build robust backends for both real-time order tracking and secure payment processing. WebSockets were integrated to enable live updates, and the Stripe API was used for secure transactions. The frontend was crafted using Next.js, ensuring a dynamic and seamless user experience. Our primary focus was on the Lunchbox track for the Headstarter Hackathon, where we aimed to deliver a comprehensive solution.

## Tech Stack:

Backend: Python with Flask, WebSockets, Stripe API
Frontend: Next.js
Database: MySQL

## What’s Next
Expanding real-time tracking to include detailed analytics for users and restaurants.
Exploring additional payment gateways to broaden the platform's versatility.
Enhancing the user interface with more personalized features and insights.

### Running the Project
**Backend Setup**
**Install virtualenv**

``bash
pip install virtualenv``

**Create a virtual environment**

``bash
python -m venv .venv``

**Activate the virtual environment**

On Windows:

``bash
.\.venv\Scripts\activate``
On macOS/Linux:

``bash
source .venv/bin/activate``

Install dependencies:

``bash
pip install -r requirements.txt``

To see a list of installed packages:

``bash
pip list``

To save the list of dependencies to requirements.txt:

``bash
pip freeze > requirements.txt``

To install a specific package:

``bash
pip install package-name``

To uninstall a package:

``bash
pip uninstall package-name``

Deactivate the virtual environment:

``bash
deactivate``

**Frontend Setup**

**Install dependencies**

``bash
npm install``
**Run the development server**

``bash
npm run dev``


### Note ⚠️
### API credentials have been revoked. If you want to run the same on your local, use your own credentials.

## Architecture Sketch

Backend Architecture:

Flask Application:

Order Tracking Service: Manages real-time updates using WebSockets.
Payment Service: Handles secure transactions using Stripe API.
Database: MySQL for storing order and payment data.
Frontend Application:

Next.js: Provides a dynamic and responsive user interface.
Interactions:

Client (Frontend) ↔ Flask API (Backend)
Flask API ↔ WebSockets (Real-time Updates)
Flask API ↔ Stripe API (Payment Processing)
Flask API ↔ MySQL (Data Storage)
