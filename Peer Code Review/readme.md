# Peer Code Review.
# Testing @Bowenislandsong's API
For this part of assignment I had to review a classmate's code. A copy of his repository can be found at [Bowenislandsong's Reposity](https://github.com/Bowenislandsong/SoftwareDesigns)

 - Classmate's code is having syntax error due to which I was unable to run the code. Error was "NameError: name 'Imager' is not defined". I found the the cause of the problem and resolved it. Below results are based upon the corrected code.

## Testing
 Testing the codes using a python script was not possible as the codes don't take output from user. To download images for different twitter profile you have to edit the python code. So it was impossible to run a script and perform test cases. So I tested code manually by entering different user handles.
 After manually testing code worked the way it supposed to be. It downloades images, analyze them and create video of the images.

## Code Review
The code review has been finished. All review comments regarding the API are under the 'Issues' section. I found several issues in the code while reviewing it.
 1. Number of Tweets, twitter username for twitter is hard-fixed. It would be better to provide an option to user to set the number of tweets and twitter username change.
 2. Code can be commented better so it will help user to understand it easily.
 3. With each run code download images in the code folder only. An option to choose desired folder should be provided.
 4. On testing with different twitter accounts, I found that images are not deleted in the download folder, due to this issue I ended up getting wrong labels from Vision API for the particular twitter account.
 5. It expect a "GoogleAPISecretes.json" file. No where in readme file or in code it's written where to put Google authentication file and what should be the name for it. 
 6. Code formatting is can be done better. Spacing and commenting are not proper.
 7. Code are written in seperate files with small function which is a good coding practice. 
 
Program performance is synchronous. All correctly labelled descriptions are written to terminal and file after the images are downloaded and the video has been made. 

## Website
Although I created website to embed the classmate's code but turned out that everything is hard-fixed and I have to edit his code each time for different operation which didn't allow me to use his code in the website. To run the app open terminal and run the main.py file also follow instruction to run the run.py as it will need authentication and twitter logins. Check the link:- https://github.com/gvikram31/EC500/tree/master/Assignment1
