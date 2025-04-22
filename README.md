# Create Flask App

A simple project to get started with your Flask App, inspired
by [Create React App](https://github.com/facebook/create-react-app).

## Overview

Create Flask App is designed to help you quickly set up a scalable Flask project. It comes with user authentication (
register, login, logout) and a basic admin page. Styling is done using [Bootstrap 5.3.3](https://getbootstrap.com/). By
default, it uses [SQLite3](https://www.sqlite.org), but you can easily configure it to use your preferred database.

## Features

- #### **More features to come this month!**
- User Registration
- User Login
- User Logout
- Protected Home Page
- Users Admin Page
- RESTful API
- Blueprint Architecture for Scalability

## Getting Started

### Prerequisites

Make sure you have the following installed on your system:

- Python 3.x
- pip (Python package installer)
- virtualenv (optional but recommended)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Gl0deanR/create-flask-app.git
    cd create-flask-app
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database:**

    ```bash
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade
    ```

5. **Run the application:**

    ```bash
    python app.py
    ```

6. **Access the application:**

   Open your browser and go to [http://localhost:5000/auth/register](http://localhost:5000/auth/register) to register a new user.
   After registration, you can log in at [http://localhost:5000/auth/login](http://localhost:5000/auth/login). The home page is
   protected and only accessible to logged-in users.

## Usage

### Running in Development Mode

For development, the app runs in debug mode by default. Make sure you activate your virtual environment and then run:

```bash
python app.py
```

### Applying Database Migrations

Whenever you make changes to your database models, apply the migrations with:

```bash
flask db migrate -m "Description of changes"
flask db upgrade
```

## Contributing

We welcome contributions! Here's how you can help:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature`).
3. Make your changes and commit them (git commit -m 'Add some feature').
4. Push the branch (`git push origin feature`).
5. Open a pull request.

### Contribution Guidelines

- Follow the coding style used in the project.
- Write clear, concise commit messages.
- Add tests for any new functionality.
- Update the documentation as needed.

### Feature Requests

If you have any feature requests or suggestions, please feel free to open an issue on GitHub or contact me directly
via [X](https://x.com/Gl0deanR).

## Todo

- [ ] **User Profile Management**
    - [x] Add user profile view and edit functionality
    - [x] Add password change feature
    - [ ] Implement profile picture upload

- [ ] **Role-Based Access Control**
    - [ ] Define roles (admin, user)
    - [ ] Implement role-based permissions
    - [x] Create admin dashboard for user management

- [ ] **Email Notifications**
    - [ ] Integrate Flask-Mail
    - [ ] Set up email templates for registration and password reset
    - [ ] Implement background job for sending emails

- [ ] **OAuth Integration**
    - [ ] Set up OAuth with Google, Facebook, and GitHub
    - [ ] Add login buttons and routes
    - [ ] Handle OAuth user registration

- [ ] **RESTful API Documentation**
    - [ ] Document all API endpoints
    - [ ] Provide examples and usage instructions

- [ ] **Docker Compose Setup**
    - [ ] Create a `docker-compose.yml` file
    - [ ] Define services for the app and database
    - [ ] Update documentation for Docker setup

- [ ] **Admin Dashboard Enhancements**
    - [ ] Add user analytics
    - [ ] Integrate system health monitoring
    - [ ] Implement activity logs

---

## License

This project is licensed under the MIT License - see the [LICENSE](license) file for details.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [Bootstrap](https://getbootstrap.com/)
- [SQLite](https://www.sqlite.org/)
- Inspired by [Create React App](https://create-react-app.dev/)

## About Us

This project is maintained by me, Raul, founder of [GLOBINARY](https://globinary.io/en), a
custom software solutions company. I specialize in creating web-based applications, mobile apps, and SaaS solutions.
Visit our website to learn more about our services.

Connect with me on X: [@Gl0deanR](https://x.com/Gl0deanR)

---

Thank you for using Create Flask App! If you encounter any issues or have any suggestions, please open an issue on GitHub.