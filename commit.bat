@echo off
set /p com="Enter commit: "

git add . 
git commit -m "%com%"  
git push 
git push heroku main
heroku open

@pause