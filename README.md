# Terms Creator :muscle:

## Overview
This is the **Terms Creator** cross platform app project repository handled by **Zuri-Training** and built by **Team 72** written with HTML5, CSS3/SCSS/Tailwind CSS, Bootstrap, Vanilla JavaScript and Python.
<br />
<br />
This project uses Django Templating.<br />
Our project name is termscreator, while our apps name is userauth.

## Project Description
Terms Creator is a web application built to help individuals and businesses easily generate free policy documents that guide their websites, software applications and user information handling. 
<br />
<br />
Terms Creator provides sample templates between clients and their users in setting the rules and guidelines to be adhered to and followed in order to access information on their websites or web applications.

## Features
***Some key features that would be present in the web application.***
- Terms and Conditions Generator
- Terms of Use Generator
- Privacy Policy Generator
- Return Policy Generator
- File Exports
- File Website Embed
- File Download and Share

## Project Requirements
User: Unauthenticated
<br />
- Visit the platform to view basic information about it
- View and Interact with the documentation
- Register to view more details
- No access to use until registered
<br />

User: Authenticated
<br />
- Full access to the platform
- Allow users enter basic information
- Generate selected files with the right data and information
- Allow export, download, share and website embed
- Allow user save data and come back to download

## User Requirements
User: Unathenticated
<br/>
- New users want to be able to view basic information
- New users want to be able to view a fixed nav-bar with relevant information in form of links and buttons
- New users want to be able to see available services offered 
- New users want to be able to see available features
- Users want to be reminded to easily sign-up at any point they are on the webapp
- New users want to be able to view relevant footer information and links
- Users want to be able to click on links and be directed to a new page
- Users want to be able to click on buttons
- Users want to be able to hover over objects
- Users want to be able to view animations
- Users want to be able to be convinced with good content to sign up
- User wants to register by email
- User wants to be able to input password
- User wants to be able to view and hide password information from showing on the client-side
- Users want to be able to get validated (email and password)
- Users want to be able to click on the submit button and have their information saved in the database
- Users want to be able to be redirected to their user dashboard
- Users want to be able to view their names
- Users who click on “Learn More” CTAs need to sign up before the make use of the functionalities within the app

User: Authenticated
<br/>
- Users should be able to login with their correct usernames and passwords
- Users should be able to change their password
- Users should be able to re-verify their account when they forget their password.
- Users should be able to delete their account if need be
- Users should be able to enter basic information about their profile type
- Users should be able to edit or change profile type
- Users should be able to enter basic information needed to generate T&C's
- Users should be able to import required files
- Users should be able to export or download generated T&C's in PDF & HTML formats
- Users should be able to share generated T&C from webapp
- User should be able to save data and continue at a later time.
- Users should be able to view file history
<br />

## Github Project For Issue Tracking
Our github project for issue tracking for all designers and developers can be found [here](https://github.com/orgs/zuri-training/projects/468)


## Design
The figma design that will be implemented for this project can be found [here](https://www.figma.com/file/G2u5xC78DgSOoHznZhwQbA/Terms-Creator---Project-72-Team-Zuri-team-library?node-id=838%3A1849)


## Contribution Guide
**Steps to collaborate on the repository for team members.**
<br/>
Forking and Creating A Pull Request(PR)
- Fork the file
- Git clone to local computer
- We will then follow the instructions placed [here](https://dev.to/codesphere/how-to-start-contributing-to-open-source-projects-on-github-534n)


## Collaborators
Find all team_72's collaborators [here](https://github.com/zuri-training/t_c_gen_team_72/graphs/contributors)

## Running The Project With A Windows System
```
-- Fork into project folder
-- git clone the project to your local computer
-- Open the project using VScode and carry out the following instructions:
-- Create a virtual environment using "python -m venv [name of VE]"
-- If you do not have a virtual environment, install one like this: pip install virtualenv_
-- Activate your Virtual Environment using this command "[name of VE]\Scripts\activate
-- Install django - pip install django
-- Install Dependencies - pip install-r requirements.txt
-- Update DB - py manage.py makemigrations
-- Next step - py manage.py migrate
-- Create Your Super User - py manage.py create superuser
-- Run our Django Project: py manage.py runserver
-- You get to view our entire work on our local server
```

## Once A Change Is Made To Our Project
```
-- Update DB - py manage.py makemigrations
-- Next step - py manage.py migrate
-- Run our Django Project: py manage.py runserver
```

















