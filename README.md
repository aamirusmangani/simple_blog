# Simple Blog Application

Create a simple personal blog platform where users can read posts, and the admin can add or delete posts.


## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python
- Pip
- Virtualenv (optional but recommended)

### Installation


1. Clone the repository:
   ```bash
   git clone https://github.com/aamirusmangani/simple_blog/
   cd simple_blog


2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`


3. Install dependencies:
   ```bash
   pip install -r requirements.txt


Before migration configure the mysql database in settengs.py


4. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate

5. Create Super User:
   ```bash
   python manage.py createsuperuser


6. Run the development server:
   ```bash
   python manage.py runserver




The application should now be running at http://localhost:8000


Access Admin Pannel at http://localhost:8000/admin


