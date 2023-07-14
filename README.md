# PostFlikr

PostFlikr is a website designed to help users create custom portfolios. It provides a user-friendly interface with essential features like a Get Started page, Login page, Registration page, and a Dashboard. Users can enter their personal details, project details, and work experiences in the Dashboard section. Once they are satisfied with their portfolio content, they can click on "Create Portfolio" to generate a unique Portfolio page.

![alt](https://github.com/AltoTenor/PortFlikr/blob/master/Github%20Portflik.png)
## Table of Contents

- [Features](#features)
- [Tech Stacks](#tech-stacks)
- [Setup Instructions](#setup-instructions)
- [Contributing](#contributing)
- [License](#license)

## Features

PostFlikr offers the following features:

- **Get Started Page:** Introduces users to the platform and guides them on how to create their custom portfolios.
- **Login Page:** Allows registered users to securely log into their accounts.
- **Registration Page:** Enables new users to create an account on PostFlikr.
- **Dashboard:** Provides a user-friendly interface for users to enter personal details like pictures,email,occupation,skill,hobbies, project details, and work experiences.
- **Portfolio:** Generates a unique Portfolio page for users based on the content entered in the Dashboard.


## Tech Stacks

PostFlikr is built using the following technologies:

- **Python:** Used with Django to develop the backend functionality of the website.
- **Django:** A powerful and popular Python web framework used for building web applications. Django is responsible for handling the backend logic and templating of pages such as Get Started, Login, Registration, and Dashboard.
- **SQLite:** A lightweight and easy-to-use database management system used by Django for storing and retrieving data. SQLite is the default database backend for Django projects and provides a convenient storage solution.
- **HTML/CSS/JS:** These technologies are used for frontend development, providing the structure, style, and interactivity of the pages.
- **React JS:** Employed to create the final Portfolio page, utilizing its component-based architecture for efficient development.
- **Axios:** A JavaScript library used to make API requests and handle communication between the frontend and backend.

Please note that SQLite is used as the default database system in the Django framework. It is suitable for development and small-scale deployments. For larger-scale applications or production environments, you may consider using a more robust database system such as PostgreSQL or MySQL with Django.

## Setup Instructions

To access and use PostFlikr, you can visit the live website hosted at [https://altotenor2002.pythonanywhere.com](https://altotenor2002.pythonanywhere.com). The website is already set up and running, so you can create an account, log in, and start building your custom portfolio immediately.

If you wish to set up a local development environment for PostFlikr, follow these steps:

1. Ensure that you have Python and Node.js installed on your machine.
2. Clone the PostFlikr repository from GitHub: `git clone https://github.com/your-username/PostFlikr.git`
3. Navigate to the project directory: `cd PostFlikr`
4. Install the required Python packages: `pip install -r requirements.txt`
5. Install the necessary frontend dependencies: `npm install`
6. Start the Django server: `python manage.py runserver`
7. In a separate terminal, start the frontend server: `npm start`
8. Open your web browser and visit `http://localhost:3000` to access PostFlikr locally.

Please note that the local development environment is meant for testing and development purposes. For a fully functional version of PostFlikr, it is recommended to use the live website hosted at [https://altotenor2002.pythonanywhere.com](https://altotenor2002.pythonanywhere.com).

## Contributing

Contributions to PostFlikr are welcome! If you would like to contribute, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bug fix: `git checkout -b my-feature`.
3. Make the necessary changes and commit your code.
4. Push your changes to your forked repository: `git push origin my-feature`.
5. Submit a pull request to the main repository.

## License

The code for PostFlikr is released under the [MIT License](https://opensource.org/licenses/MIT). You are free to modify and distribute the code as per the terms and conditions of the license.
