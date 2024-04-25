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
