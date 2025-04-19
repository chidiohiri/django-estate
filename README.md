# Django Estate

Django Estate is a full-featured web application designed to streamline the property rental process by connecting tenants with landlords in an intuitive and transparent way. The platform offers a centralized experience where users can browse listed properties, schedule inspection appointments, submit rental applications, and interact with other relevant features tailored to the rental lifecycle.

Whether you're a tenant searching for the perfect space or a landlord looking to manage rental applications efficiently, Django Estate aims to provide a seamless solution for both parties.

### Getting Started

These instructions will guide you through setting up Django Estate on your local machine for development and testing purposes. This guide assumes you are working on a Windows environment. Mac and Linux users can adapt the commands accordingly.

### Prerequisites

Below are the dependencies for the project. For quicker installation, please refer to the [requirements.txt](requirements.txt) file.
- [Python](https://www.python.org/downloads/) - The programming language used to build the backend of the application.
- [Django](https://www.djangoproject.com/download/) - The web framework that powers the server-side logic, database models, and URL routing.
- [Visual Studio Code](https://code.visualstudio.com/) -  A lightweight, flexible code editor recommended for writing and managing the project code.
- [Django Widget Tweaks](https://pypi.org/project/django-widget-tweaks/) - A Django template tag library used to customize form fields directly in templates.
- [Django Filter](https://pypi.org/project/django-filter/) - Adds filtering capabilities to Django views, making it easy to implement search and filter functionality.

### Installing

Create and initialize a virtual environment (optional)

    pip install virtualenv
    virtualenv estate_env
    cd estate_env
    Scripts\activate

Clone the Repository

    clone https://github.com/chidiohiri/django-estate.git
    cd django-estate

Move the project into the virtual environment, then install dependencies. The project dependencies can found in [requirements.txt](requirements.txt)

    pip install -r requirements.txt

Migrate all tables to the Sqlite3 DB

    python manage.py makemigrations
    python manage.py migrate

Create a super user. This account will be used to access the admin dashboard and verify listed properties.

    python manage.py createsuperuser

Run server on your terminal (cmd or powershell). Open your browser and navigate to http://127.0.0.1:8000/ to access the application.

    python manage.py runserver

### Core Features

 - Property Listings: Browse through an up-to-date catalog of available properties with filtering capabilities by price, location, availability, and more.

- Tenant and Landlord Roles: Users can register as either tenants or landlords, unlocking role-specific functionality.

- Application Management: Streamlined workflow for submitting, reviewing, and managing rental applications.

- Admin Verification: A superuser (admin) account can verify properties, manage user accounts, and moderate content.

- User Authentication: Secure registration and login functionality with session management.

- Responsive Design: Frontend styled with Bootstrap to ensure compatibility across various screen sizes.

### Deployment

For production deployment, you will need to configure your application with a production-grade database (such as PostgreSQL), static file handling, and secure hosting. You may refer to the official [Django Documentation](https://docs.djangoproject.com/en/5.1/howto/deployment/) on deployment

### Authors

  - **Chidi Ohiri** - *For updates, networking, or feedback, feel free to connect:* -
    [Linkedin](https://www.linkedin.com/in/chidiebere-ohiri/)

### License

This project is licensed under the [MIT LICENSE](LICENSE.md), which permits reuse, modification, and distribution with proper attribution.

### Acknowledgments

  - Guido van Rossum, the creator of Python
  - The Django core team and community for building and maintaining such a robust framework
  - Developers and open-source contributors whose work inspired or supported the development of this project

