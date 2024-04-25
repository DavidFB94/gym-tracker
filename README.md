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
