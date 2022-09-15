<br/>

# manaGym - Full-Stack Flask/PostgreSQL App

**Project:** Solo Project built in the 5th week of the CodeClan Course.

<p>manaGym is a gym management web app that allows User/Gym Staff to store Members/Gym Classes data, as well as track bookings.</p>

<p>It's a Full-Stack App build with Flask and PostgreSQL, using CRUD actions and many to many relationship data model.</p>

<br/>

## App Running:

![screen-gif](./static/manaGym.gif)

<br/>

## Project brief:

<h3>Gym Management App</h3>

Build an app allowing a local gym manage memberships and register members for courses.

<h3>MVP:</h3>

- The app should allow the gym to create and edit Member's.
- The app should allow the gym to create and edit Course's.
- The app should allow the gym to book Member's on specific Course's.
- The app should show a list of all upcoming Course's.
- The app should show all Member's that are booked in for a particular course.

<h3>Extensions:</h3>

- Course's could have a maximum capacity, and users can only be added while there is space remaining.
- The gym could be able to give its Member's Premium or Standard membership. Standard Member's can only be signed up for Course's during off-peak hours.
- The Gym could mark Member's and Course's as active/deactivated. Deactivated Member's/Course's will not appear when creating bookings.
- Duplicated bookings are not alowed.

<h3>Further Extensions:</h3>

- Search box functionality across Members, Courses and Bookings

<br/>

## Languages and Tools:

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-plain.svg" title="Python3" alt="Python logo" width="50" height="50"/>&nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg" title="Flask" alt="Flask logo" width="50" height="50"/>&nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-plain.svg" title="PostgreSQL" alt="PostgreSQL logo" width="50" height="50"/>&nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-plain.svg" title="HTML5" alt="HTML5 logo" width="50" height="50"/>&nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-plain.svg"  title="CSS3" alt="CSS3 logo" width="50" height="50"/>&nbsp;

<br/>

## To run the app follow the steps below:

Clone the repository

Create and seed an SQL database called managym:
```
psql createdb managym
psql -d managym -f db/managym.sql
```

Populate with data using the console:
```
python3 console.py
```

Run on the browser using Flask (assuming that Flask is installed on your computer):
```
flask run
```
<br/>