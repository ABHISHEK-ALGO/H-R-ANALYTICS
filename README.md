# H R Analytics - Employee Turnover Prediction

HR Tech marks to be a 22 Billion USD market size & is highly invested in Cognitive Neuroscience with AI. The current challenge is a huge research initiative in the field of Neuroscience which leverages AI to compute human behavior markers for success. This is widely worked in the HR Industry to assess work & talent management. AI-based reports have been deployed in Manufacturing, Communications, Retail Hiring & job suitability. 
Dashboard pic or video
***
## Table of Contents
<a id='table_of_contents'></a><br>
[Project Summary](#section0)<br>
[Part 1: Targeted Insights](#section1)<br>
[Part 2: Visualizations (Tableau)](#section2)<br>
[Part 3: Perform EDA](#section3)<br>
[Part 4: Perform Machine Learning](#section4)<br>
[Part 5: Deploy the Model](#section5)<br>
[Application and Recommendations](#section6)<br>
[Assumptions Taken if Any](#section7)<br>

<a id='section0'></a>
## Project Summary
**Project Statement:**
Portobello Tech is an app innovator that has devised an intelligent way of predicting employee turnover within the company. It periodically evaluates employees' work details including the number of projects they worked upon, average monthly working hours, time spent in the company, promotions in the last 5 years, and salary level.

Data from prior evaluations show the employee’s satisfaction at the workplace. The data could be used to identify patterns in work style and their interest to continue to work in the company. 

HR Department owns the data and uses it to predict employee turnover. Employee turnover refers to the total number of workers who leave a company over a certain time period.

As the ML developer assigned to the HR Department, I have been asked to find
*** 
<a id='section1'></a>
<b>**Part 1: Targeted Insights**</b>

- What was the average satisfaction level of employees who left the company?
- Is lack of promotion related to employees leaving the company?
- How balanced is the gender distribution across departments?
- Which job roles have the highest attrition rates?
- How many high performers (last evaluation > 0.8) left the company?
  Link [Visit File](https://github.com/ABHISHEK-ALGO/H-R-ANALYTICS/blob/main/Hr%20targeted%20insights.sql)

<a id='section2'></a>
<b>**Part 2: Visualize Employee Turnover and Potential groups of Employees in the Company**</b>
The interactive dashboard provides valuable insights into employee turnover and potential employee segments by allowing users to filter data based on Department and Educational Background. It presents comprehensive metrics, including overall employee counts, turnover count, turnover rate, and distribution across various age groups. The dashboard visualizes turnover trends across departments, age groups, genders, and educational backgrounds. By using different combinations of filters, users can derive meaningful insights to better understand turnover patterns within the company.</b> 
![Image](https://github.com/user-attachments/assets/c4ac8bb5-75bf-4535-a075-09237b504a2b)
[Story Board video Link] https://github.com/user-attachments/assets/b501a8b0-8996-4107-be01-03ea34b17560</b>

<b>**Findings:**</b>

 - The company has a total of 14,999 employees, with an average age of 42 years.
 - The overall turnover rate is 24%, considering employees from all educational backgrounds.
 - The majority of employees fall within the 30–40 age group, with a nearly equal distribution of male and female employees.
 - Turnover is higher among younger employees, while it is significantly lower in the 40–60 age group for both genders.
 - Over half of the workforce comprises graduates, who also exhibit a higher turnover rate.
 - Employees with a PhD represent a very small portion of the workforce and have the lowest turnover rate.
 - The Sales department experiences the highest turnover among all departments.
 - Company has more than half employee count with graduation as educational background with high turnover while PHD are too less in numbers with lowest turnover. Sales department has the    highest turnover. More insights can be explore by interacting with the dashboard.

<a id='section3'></a>
<b>**Part 3: Perform EDA to get deeper insights for the turnover and find reasons of turnover**</b>

![Image](https://github.com/user-attachments/assets/43672dbe-c5dd-4579-8d8a-93b8800f467e)

![Image](https://github.com/user-attachments/assets/437cafdb-9ffb-422e-a583-6319f89ef04c)

<a id='section4'></a>
<b>**Part 4: Perform Machine Learing**</b>

  * To Cluster Employees who left based on their satisfaction and evaluation.
    
    ![Image](https://github.com/user-attachments/assets/13677812-7054-407c-b29d-98f0149642f0)

  * Gather important attributes or features responsible
    
    ![Image](https://github.com/user-attachments/assets/c21932f4-cd0a-40e8-93fd-ab7e82cb2b38)
    
  * Apply SMOTE to balance Target
    
    ![Image](https://github.com/user-attachments/assets/153316ca-7f25-463f-87eb-69da94ad5273)

  * Develop a model to predict employee will leave or stay.
    
    ![Image](https://github.com/user-attachments/assets/0bb62882-c66d-4f5a-86bd-b77e6df79b08)
</b>

<a id='section5'></a>
<b>**Part 5: Deploy a model**</b>

  * Build a prototype webpage which takes features responsible for turnover as input and predict whether employee will stay or leave.
    [App video Link]https://github.com/user-attachments/assets/930290bf-f754-4b83-b896-fb8135e0670a

<a id='section6'></a>
## Applications And Benefits:
- Turnover Forecast
- Resource Management 
- To plan perks and benefits
- Pre informed decision on critical aspects like promotions, merit increment, career growth plan
- Assertive measures as an employer for any kind of misconduct 
- Departmental Turnover Cost Analysis


