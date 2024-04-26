# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| home | add_exercise.html | ![screenshot](documentation/validation/add_exercise.html.png) | No errors |
| home | add_workout.html | ![screenshot](documentation/validation/add_workout.html.png) | No errors |
| home | edit_exercise.html | ![screenshot](documentation/validation/edit_exercise.html.png) | Missing divs (fixed) |
| home | edit_workout.html | ![screenshot](documentation/validation/edit_workout.html.png) | Missing divs (fixed) |
| home | home.html | ![screenshot](documentation/validation/home.html.png) | No errors |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| static | style.css | ![screenshot](documentation/validation/static-css.png) | |

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| home | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidFB94/gym-tracker/main/home/admin.py) | ![screenshot](documentation/validation/admin.py.png) | |
| home | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidFB94/gym-tracker/main/home/forms.py) | ![screenshot](documentation/validation/forms.py.png) | |
| home | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidFB94/gym-tracker/main/home/models.py) | ![screenshot](documentation/validation/models.py.png) | |
| home | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidFB94/gym-tracker/main/home/urls.py) | ![screenshot](documentation/validation/urls.py.png) | |
| home | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidFB94/gym-tracker/main/home/views.py) | ![screenshot](documentation/validation/views.py.png) | |
| home | tests.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidFB94/gym-tracker/main/home/views.py) | ![screenshot](documentation/validation/tests.py.png) | |
| home | apps.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidFB94/gym-tracker/main/home/views.py) | ![screenshot](documentation/validation/apps.py.png) | |
|  | manage.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidFB94/gym-tracker/main/manage.py) | ![screenshot](documentation/validation/manage.py.png) | |
| my_project | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidFB94/gym-tracker/main/my_project/urls.py) | ![screenshot](documentation/validation/my_project-urls.py.png) | |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Home  | Add workout | Edit workout | Add exercise | Notes |
| --- | --- | --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/browsers/chrome-home.png) | ![screenshot](documentation/browsers/chrome-add-workout.png) | ![screenshot](documentation/browsers/chrome-edit-workout.png) | ![screenshot](documentation/browsers/chrome-add-exercise.png) |  Works as expected |
| Firefox | ![screenshot](documentation/browsers/firefox-home.png) | ![screenshot](documentation/browsers/firefox-add-workout.png) | ![screenshot](documentation/browsers/firefox-edit-workout.png) | ![screenshot](documentation/browsers/firefox-add-exercise.png) | Works as expected |
| Edge | ![screenshot](documentation/browsers/edge-home.png) | ![screenshot](documentation/browsers/edge-add-workout.png) | ![screenshot](documentation/browsers/edge-edit-workout.png) | ![screenshot](documentation/browsers/edge-add-exercise.png) | Works as expected |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | home | Add workout | Edit workout | Add exercise | Notes |
| --- | --- | --- | --- | --- |  --- |
| Mobile (DevTools) | ![screenshot](documentation/responsiveness/home-mobile.png) | ![screenshot](documentation/responsiveness/add-workout-mobile.png) | ![screenshot](documentation/responsiveness/edit-workout-mobile.png) | ![screenshot](documentation/responsiveness/add-exercise-mobile.png) | Works as expected.  |
| Tablet (DevTools) | ![screenshot](documentation/responsiveness/home-tablet.png) | ![screenshot](documentation/responsiveness/add-workout-tablet.png) | ![screenshot](documentation/responsiveness/edit-workout-tablet.png) | ![screenshot](documentation/responsiveness/add-exercise-tablet.png) | Works as expected |
| Desktop | ![screenshot](documentation/browsers/chrome-home.png) | ![screenshot](documentation/browsers/chrome-add-workout.png) | ![screenshot](documentation/browsers/chrome-edit-workout.png) | ![screenshot](documentation/browsers/chrome-add-exercise.png) | Works as expected |
| Sony Xperia 10 | ![screenshot](documentation/responsiveness/home-xperia.jpg) | ![screenshot](documentation/responsiveness/add-workout-xperia.jpg) | ![screenshot](documentation/responsiveness/edit-workout-xperia.jpg) | ![screenshot](documentation/responsiveness/add-exercise-xperia.jpg) | Works as expected |

