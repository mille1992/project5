# Introduction to Yayberhood
Yayberhood is a webpage designed to enable neighberhoods to grow closer together. 
The Main functionalities consist of 
- a space to organize and fund projects in the neighberhood
- a space to organize help for ppl who need it
- a space to organize groups to perform hobbies together and exchange infos about the hobbies
- a space to rent / lent things to one another.


# Distinctiveness and Complexity
This paragraph describes why the webpage fulfills the required complexity and distinctiveness.
## Layout
### Inheritance
The main layout.html builds the foundation for the webpages design. Each of the other htmls incorporates this file as a base design and builds on top of it.
### Multi-layered design
In order to enable the exquisite design seen, multiple layers were used to display content on top of each other. Examples are the navbar on top of an image as well as the bubble containing the title on each page.
### Usage of external sources
Frameworks like Bootstrap as well as Icons are used throughout the webpage to enhance the design. The Column wise build up of the design, as used by Bootstrap as well, build the foundation of the design. 
### multiple css functionalities used
To enhance the appearance and user experience, multiple css functionalities were used, including selectors, margins, paddings, transitions,hovers, z-level etc.
### Animation designed via js
In order to further improve user experience javascript was used to enable dynamic design. When clicking on certain parts of the webpage, containers will enlarge or shrink fluently depending on the content that shall be displayed

## Data base model
The Data base model consists of multiple different models in order to store the varying information needed to enable the different core functionalities.
### Primary Keys
Lean and transparent database queries are enabled via clear and consistent variable names. Primary keys are used for most of the models as the relations are multiple, complex and connected. 
### adaptation of Django user to include more infos
Django User Model was extended in order to enable the webpage functionality. One of the reasons is to enable saving a profile picture for each user.

## Message System
A message system is part of the webpage to enable users to communicate with each other. This makes it possible to organize projects, groups, help or rentals. Messages are saved with a date, sender, recipient, message content as well as the message type value. Hence, it is clear which message was send concerning which core functionality. Sending a message is only possible if the user is logged in and is not the post creator.

## Donation system
A donation system enables the user to contribute financially to a project. This is only possible if the user is logged in.
### Live update of donation values via js
When sending a donation the value for current donations is updated automatically and instantly displayed on the webpage.
### Front end check of correct input values
When trying to contribute with a negative amount of money, the front end check will not enable it. Also the backend will check for  correct input values.

## Membership System
Each Hobby Group contains a list of admins and a list of members. When creating a new group the creating user is automatically added as an admin as well as a member. If a non creator looks at the group he/she can request membership as long as they are logged in as a user.

## Profile page to read out user specifics
The Profile page displays summarized infos about the user. The content displayed is the username and joining date, the profile picture, last sent messages, last received messages, main participations in the various core functionalities of the webpage.

## Filter functionality
Two different filter functionalities were implemented to make user handling of a larger database leaner.
### Filter for Hobby Groups
When entering the hobby group page the user may choose to reduce the displayed content of all hobby groups to a certain category of hobby groups. If the user is not content with the current selection the page contains a button to call back the filter view.
### Dynamic filter for Rentals/Help (Search / Offer)
When looking at rentals or help, the user may choose to display all: Searches as well as offers. Or the user may choose only one of them. Depending on the sequence the user clicks on the filter buttons, the webpage will behave differently in order to enable the right filter content.

# Files
## layout.html / css / js
Build the foundation and is included in all other html files. Its css / js files similarly build a foundation for the other htmls as well. The js is used in order to smoothly enlarge or shrink clicked items. The css styles the titles, navbars, pockets, create buttons and scrollviews. 

## register.html
Enables the user to register a new user account.

## login.html
Enables the user to log in. Is called when the user is logged out and clicks on the user icon in the top right webpage corner.

## profilePage.html / css
Summarizes infos about the user. Enables the user to log out. Is called when the user is logged in and clicks on the User Icon in the top right webpage corner.

## landingPage.html / css
First page the user sees when entering the webpage. Shall be used to introduce the four core functionalities to the user.

## borrowIt.html / css / js
Displays all items that are currently offered or searched for. Enables the user to create its own entry. Enables filtering to only display searches, offers or both. The items are displayed in a scroll view. This enables the user to quickly get access to the navbar / filters and creation of new content. Using javascript the webpage does not need to be reloaded for this. When clicking on the icon on top of the items box the view is smoothly enlarged in order to display more details about an item and to enable the user to contact the owner of the item via a message.
### createBorrowIt.html
Enables the user to create a rental search or offer. The user is requested to input a title, a short- and detailed description as well as the info whether this is a search or an offer. The front end check will make sure that the user inputs minimal information as title and detailed description of the item.

## littleProjects.html / css / js
Displays all projects that are currently available. Enables the user to create its own project. Projects are displayed in a scroll view. This enables the user to quickly get access to the navbar / filters and creation of new content. When clicking on the icon on top of the projects box the view is smoothly enlarged in order to display more details about a project and to enable the user to contribute to the project via a donation. When a donation was made the displayed total donation value is automatically updated via js.
### createLittleProject.html
Enables the user to create a new project. The user is requested to input a title, a short- and detailed description as well as the info whether donations are accepted or not. The front end check will make sure that the user inputs minimal information as title and detailed description of the item.

## littleHelpers.html / css / js
Displays all Helps that are currently available. Enables the user to create its own Help. Helps are displayed in a scroll view. This enables the user to quickly get access to the navbar / filters and creation of new content. The page enables filtering to only display searches, offers or both. Using javascript the webpage does not need to be reloaded for this. When clicking on the icon on top of the Helps box the view is smoothly enlarged in order to display more details about a Help and to enable the user to contact the owner of the Help via a message.
### createLittleHelpers.html
Enables the user to create a new project. The user is requested to input a title, a short- and detailed description as well as the info whether donations are accepted or not. The front end check will make sure that the user inputs minimal information as title and detailed description of the item.

## hobbies.html / css / js
Displays all Categories of Hobby Groups that are currently available. The user can choose whether to filter for one of them or to see all. Furthermore the page enables the user to create its own Hobby Group. Hobby Groups are displayed in a scroll view. This enables the user to quickly get access to the navbar / filters and creation of new content. The filtering for categories can be accessed by the user whenever needed on the top left corner. Using javascript the webpage does not need to be reloaded for this. When clicking on the icon on top of the Helps box the view is smoothly enlarged in order to display more details about a Hobby Group and to enable the user to Request Membership to a group.
### createHobbyGroup.html
Enables the user to create a new Hobby Group. The user is requested to input a title, a short- and detailed description as well as the info which category this Hobby Group belongs to. The front end check will make sure that the user inputs minimal information as title and detailed description of the item.

## admin.py
Used to register the main models to the admin page

## models.py
Includes the used models.

## views.py
Defines the functionality of the webpage. It handles the Post and Get requests, calls and modifies database data.