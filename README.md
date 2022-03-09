# SAS

## Role-based Activity Interview/Presentation  

# Interview Prompt:  

A customer is asking for a script / program they can give out to their HR department to help speed up business operations. You have been given the following acceptance criteria:  

Given I have an array of employee records that include their birthday  
When I execute this script/program with the array of employees  
Then I am returned an array of employees who's birthday is in the current month  

# Guidelines:

Build a runnable script/program that meets the above acceptance criteria  
Use the language and development tools of your choice  
The interface with this script or program is up to you  
Should be tested  
Be prepared to:  
Present your script/program and walk through how you have met the acceptance criteria  
Talk about how you have tested it  
Discuss any challenges you may have encountered  

==================================================================  

# Unit Tests:  

To run: python -m unittest employees.py  

Test cases:  
1) Basic success case  
2) Null month  
3) Null employee list  
4) Bad month type  
5) Bad employee list type  
6) Empty employee list  
7) Negative month  


# Server:  
set FLASK_APP=app.py  
set FLASK_ENV=development  
flask run  
