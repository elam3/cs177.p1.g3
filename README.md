# CS177 FALL 2016 PROJ1 GRP3

## Requirements
* Shall function on a mobile browser
* Administrative users are able to start quizes and collect responses
* Student users are able to submit answers and create identification code
* Answers must be collected and displayed

## Functional Specification
### iClicker Functional Specification
By Owen Goodwin
### Overview
iClicker is a service that allows students to take in class quizzes on the web.
### Scenarios
#### **Scenario 1: Sam**
Sam is a teacher that wants quick feedback in class to see how well students are following the lectures. He therefore decides to do quick in class polls that are graded in real time and let’s students see how well they are doing. He therefore uses the iClicker to do this.

Students go to the quiz page he provides them, while Sam goes to the admin page. Sam begins the quiz by posting a question in his powerpoint and starts the timer. The students make their selection on their devices. He sees that most of the class has responded by looking at the response counter. He then stops the timer. He then clicks on the visualization button and displays a chart of how the students have done. He then refreshes and starts the timer over again, this process repeats for about five more questions.

### Specification

####Administrative Page
* There will be a Start/Stop button and a timer. When the start button is pressed the timer will start counting up in seconds. When the start/stop button is pressed again the timer will stop.
* There will be a counter which displays the number of responses that are being submitted, so that the teacher knows when they can stop the timer.
* There will be a button that allows the teacher to display the information.
* If they choose to display the information as a bar chart, a bar chart graphic will be shown which displays the number of responses to each question.
* They can select via radio button which was the correct response.
Quiz Page
* Will display multiple choice radio buttons A-E. Student will be able to select one and there will be a submit button which is inactive until the teacher starts the timer.
* When the teacher starts the timer the page will refresh and students will be allowed to click the submit button. When the timer stops this button will be greyed out.

### Nice to haves:
* different options for visualizing the data
* a way to record the test and save for later.
* A way to author the questions and send to the students so they can visualize on their screens.
* Sending the correct response to the students, or notifying them the got it right.
