# manaGym
Full stack project with Flask and PostgreSQL.

manaGym is a gym management web app that allows a gym's staff to store client/gym classes data, as well as track bookings.


| This project was created using: |
| :------------------------------ |
| Python 3 |
| Flask |
| PosgreSQL |
| HTML |
| CSS |

## To use this program, from the project's root folder run in the terminal the following:

- Create and seed an SQL database called managym:
```
psql createdb managym
psql -d managym -f db/managym.sql
```

- Populate with data using the console:
```
python3 console.py
```

- Run on the browser using Flask (assuming that Flask is installed on your computer):
```
flask run
```

# Project brief:

Build an app allowing a local gym manage memberships and register members for courses.

## MVP

- The app should allow the gym to create and edit `Member`s.
- The app should allow the gym to create and edit `Course`s.
- The app should allow the gym to book `Member`s on specific `Course`s.
- The app should show a list of all upcoming `Course`s.
- The app should show all `Member`s that are booked in for a particular course.

## Extensions

- `Course`s could have a maximum capacity, and users can only be added while there is space remaining.
- The gym could be able to give its `Member`s Premium or Standard membership. Standard `Member`s can only be signed up for `Course`s during off-peak hours.
- The Gym could mark `Member`s and `Course`s as active/deactivated. Deactivated `Member`s/`Course`s will not appear when creating bookings.
- Duplicated bookings are not alowed.
