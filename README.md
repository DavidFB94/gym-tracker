# [GYM TRACKER](https://gym-tracker-db-a73c4dc55708.herokuapp.com)

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/DavidFB94/gym-tracker)](https://github.com/DavidFB94/gym-tracker/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/DavidFB94/gym-tracker)](https://github.com/DavidFB94/gym-tracker/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/DavidFB94/gym-tracker)](https://github.com/DavidFB94/gym-tracker)

## Overview
GymTracker is a website where users can find a simple tool for tracking and logging their gym workouts.

GymTracker allows the user to create workouts, where they can freely add exercises, and leave a note for workout reminders. A workout name and date can be added, so the workout can be easily identified if it needs to be accessed at a later time.

This website was built as a project for the Diploma in Full Stack Software Development at Code Institute.

## Mock-up

![screenshot](documentation/mockup.png)

## UX

I started out with Wireframes for both desktop and mobile.

After creating the basic structure for the page according to the wireframes, I realized that I was trying to create too much functionality using only one html page using modals. I decided to shift things around, so I put the forms in separate html-files. This also helped in keeping the home page less cluttered with information, especially on smaller screens.

After this shift, my focus was on keeping the user experience smooth, reducing the amount of actions needed, and keep important information visible. For this reason, I decided to add the list of exercises to the "add exercises" page, so it would be easier for the user to keep track of what they have already added to their workout. I also adjusted the back button to bring the user back to the "add exercises" page (instead of going back to the home page) after editing an exercise, in case the user wants to keep editing different exercises.

### Color Scheme

I wanted the site to have a simple look, while keeping the information easily readable. For that reason, I had to adjust my color theme towards the end of the project.

- `#212529` used for primary text.
- `#fff` used for secondary text.
- `#AD1A26` used for highlights + links.

I used [coolors.co](https://coolors.co/212529-ad1a26-9c1c27-ffe600-ffffff) to generate my color palette.

![screenshot](documentation/color-palette.png)

### Typography

Font was applied automatically by Bootstrap, which selects the best `font-family` for each OS and device.

- [Bootstraps native font stack](https://getbootstrap.com/docs/5.0/content/reboot/#native-font-stack) was used for all text content.

- [Font Awesome](https://fontawesome.com/icons/rectangle-list?f=sharp&s=regular) icon was used for the favicon.

- [GitHub](https://github.com/logos) icon was used for the GitHub link.

## User Stories

### Site Users

- As a site user I can register an account so that I can log in, and use the site in an authorized and secure way.
- As a site user I can log in with my account information so that I can use the sites features.
- As a site user I can log out from my account so that I can avoid unauthorized access to my data.
- As a site user I can create a workout so that I can plan/track my workout schedule.
- As a site user I can view saved workouts so that I can access the saved information.
- As a site user I can delete saved workouts so that I can remove workouts that I no longer wish to track.
- As a site user I can create exercises so that I can make add them to my workout.
- As a site user I can view my exercises in a workout so that I can plan/track my workout.
- As a site user I can update my exercises so that I make can make changes if required.
- As a site user I can delete saved exercises so that I can remove exercises that I no longer wish to track.
- As a site user I can filter saved workouts so that I can find the workout I'm looking for more easily.
- As a site user I can create a workout plan so that I can re-use workouts more easily.
- As a site user I can add my personal profile so that I can add additional information.
- As a site user I can create a workout calendar so that I can plan my workout activity.
- As a site user I can receive reminders from the app so that I can achieve better adherence to my workout plan.
- As a site user I can view my saved data so that I can get an overview of my activity/progress.
- As a site user I can fill in a feedback form so that I can submit development requests to the site administrator.

### Site Admin

- As a site admin I can moderate users and their data so that I can make changes when required.
- As a site admin I can store feedback messages in the database so that I can review them.
- As a site admin I can I can mark feedback messages as "read" so that I can keep track on which messages I have reviewed.

## Wireframes

Wireframes were developed for mobile and desktop.
I've used [Balsamiq](https://balsamiq.com/wireframes) to design my site wireframes.

### Mobile Wireframes

<details>
<summary> Click here to see the Mobile Wireframes </summary>

Home
  - ![screenshot](documentation/wireframes/mobile-home.png)

Add/edit workout
  - ![screenshot](documentation/wireframes/mobile-add-workout.png)

</details>

### Desktop Wireframes

<details>
<summary> Click here to see the Desktop Wireframes </summary>

Home
  - ![screenshot](documentation/wireframes/desktop-home.png)

Add/edit workout
  - ![screenshot](documentation/wireframes/desktop-add-workout.png)

</details>

## Tools & Technologies Used

- [![Markdown Builder](https://img.shields.io/badge/Markdown_Builder-grey?logo=markdown&logoColor=000000)](https://tim.2bn.dev/markdown-builder) used to generate README and TESTING templates.
- [![Git](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [![GitHub](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) used for secure online code storage.
- [![Gitpod](https://img.shields.io/badge/Gitpod-grey?logo=gitpod&logoColor=FFAE33)](https://gitpod.io) used as a cloud-based IDE for development.
- [![HTML](https://img.shields.io/badge/HTML-grey?logo=html5&logoColor=E34F26)](https://en.wikipedia.org/wiki/HTML) used for the main site content.
- [![CSS](https://img.shields.io/badge/CSS-grey?logo=css3&logoColor=1572B6)](https://en.wikipedia.org/wiki/CSS) used for the main site design and layout.
- [![JavaScript](https://img.shields.io/badge/JavaScript-grey?logo=javascript&logoColor=F7DF1E)](https://www.javascript.com) used for user interaction on the site.
- [![Python](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) used as the back-end programming language.
- [![Heroku](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) used for hosting the deployed back-end site.
- [![Bootstrap](https://img.shields.io/badge/Bootstrap-grey?logo=bootstrap&logoColor=7952B3)](https://getbootstrap.com) used as the front-end CSS framework for modern responsiveness and pre-built components.
- [![Django](https://img.shields.io/badge/Django-grey?logo=django&logoColor=092E20)](https://www.djangoproject.com) used as the Python framework for the site.
- [![PostgreSQL by Code Institute](https://img.shields.io/badge/PostgreSQL_by_Code_Institute-grey?logo=okta&logoColor=F05223)](https://dbs.ci-dbs.net) used as the Postgres database from Code Institute.
- [![WhiteNoise](https://img.shields.io/badge/WhiteNoise-grey?logo=python&logoColor=FFFFFF)](https://whitenoise.readthedocs.io) used for serving static files with Heroku.
- [![Balsamiq](https://img.shields.io/badge/Balsamiq-grey?logo=barmenia&logoColor=CE0908)](https://balsamiq.com/wireframes) used for creating wireframes.
- [![Font Awesome](https://img.shields.io/badge/Font_Awesome-grey?logo=fontawesome&logoColor=528DD7)](https://fontawesome.com) used for the favicon.
- [![ChatGPT](https://img.shields.io/badge/ChatGPT-grey?logo=chromatic&logoColor=75A99C)](https://chat.openai.com) used to help debug, troubleshoot, and explain things.

## Database Design

Entity Relationship Diagrams (ERD) help to visualize database architecture before creating models.
Understanding the relationships between different tables can save time later in the project.

```python
class Workout:
	user = ForeignKey(User, on_delete=models.CASCADE)
	name = CharField(max_length=100, null=False, blank=False)
	note = TextField(null=True, blank=True)
	date = DateField(null=False, blank=False)
```

```python
class Exercise:
	workout = ForeignKey(
		Workout,on_delete=models.CASCADE,related_name="exercises")
	name = CharField(max_length=50, null=False, blank=False)
	weight = CharField(max_length=30, null=False, blank=False)
	sets = PositiveIntegerField(null=False, blank=False)
	reps = CharField(max_length=20, null=False, blank=False)
```

