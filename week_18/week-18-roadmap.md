# Week 18 Roadmap

---

### Technologies
- Today: dependency management & unittesting
- Tuesday: creating a simple web server, templating, and forms
- Wednesday: interacting with a database via an ORM
- Thursday: migrating data
- Friday: review, practice assessment walkthrough, and Kahoot!


---

### Flask (Tuesday)
- [Flask](https://flask.palletsprojects.com/)
    - Web server (like Express, but for Python)
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
    - Templating language (like Pug)
- [Psycopg2](https://www.psycopg.org/docs/index.html#)
    - Database adapter for Python, allows Flask to communicate with Postgres database
- [WTForms](https://wtforms.readthedocs.io) & [Flask-WTF](https://flask-wtf.readthedocs.io)
    - WTForms is a form validation library
    - Flask-WTF integrates WTForms with Flask

---

### SQLAlchemy & Flask-SQLAlchemy (Wednesday)
- [SQLAlchemy](https://docs.sqlalchemy.org/en/14/index.html)
    - Object-relational mapping tool (ORM) that makes it easier to interact with our database (like Sequelize)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com) 
    - Integrates SQLAlchemy with Flask


---

### Alembic & Flask-Migrate (Thursday)
- [Alembic](https://alembic.sqlalchemy.org)
    - Database migration tool that works with SQLAlchemy
- [Flask-Migrate](https://flask-migrate.readthedocs.io)
    - Integrates Alembic with Flask

---

### Review day (Friday)
- Independent study time
- Practice assessment walkthrough
- Kahoot

---

### Today

- This morning
    - Career stuff
        - Reading: Presentation skills (20 min)
        - Exercise: Interview practice (40 min)
        - *Skip Instructor Led Project*
- After lunch
    - Lecture: Python environment management & unit testing
        - NOTE: we installed pipenv last week. If you have not done so, please follow [these instructions](https://github.com/appacademy/unified-setup/blob/main/python-setup.md). You can check your install with `pipenv --version`. If it comes back with a version, you're all set!
    - Python Unit Testing project