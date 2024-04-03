# Assignment

The Assignment project is a web application designed to streamline the assignment management process for learners, teachers, and administrators. It leverages modern technologies like Django for the backend, Next.js for the frontend, and PostgreSQL for data management, ensuring a robust and scalable solution for educational institutions.

## Overview

This project employs Django as its backend framework, which provides a structured approach to server-side operations, including user authentication, data manipulation, and API responses. Next.js is utilized for the frontend to offer a seamless and interactive user experience. PostgreSQL serves as the database management system, ensuring data integrity and efficient data querying. The application adopts a modular architecture, facilitating ease of maintenance and scalability.

## Features

- **User Authentication**: Simplified login for learners and managed accounts for teachers and administrators.
- **Assignment Creation and Management**: Enables teachers to create and manage assignments with deadlines, resources, and instructions.
- **Assignment Submission**: Allows learners to submit their work and track submission status.
- **Grading and Feedback**: Teachers can grade assignments and provide feedback, accessible by learners.
- **Dashboard**: Personalized dashboards for users to view assignments, deadlines, and grades.
- **Admin Panel**: Comprehensive management console for administrators.
- **PDF Report Generation**: Facilitates the creation of detailed PDF reports on assignment performance.

## Getting started

### Requirements

- Python 3.8 or newer
- Django 4.2.7
- PostgreSQL
- Node.js and npm (for Next.js)

### Quickstart

1. Clone the repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt` and `npm install`.
3. Set up the PostgreSQL database and update the connection string in the `assignment/settings.py` file.
4. Execute Django migrations with `python manage.py migrate`.
5. Start the Django server using `python manage.py runserver`.
6. In another terminal, navigate to the frontend directory and start the Next.js server with `npm run dev`.

### License

Copyright (c) 2024.