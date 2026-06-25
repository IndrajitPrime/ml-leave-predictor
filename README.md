ML Resource Leave Predictor

A desktop application that uses Random Forest machine learning to predict how many leave days a resource is likely to take in the current quarter, based on their historical planned vs actual leave patterns. Built with Python, scikit-learn, and Tkinter.

The Problem It Solves

Project managers consistently face budget overruns and missed deadlines caused by unplanned employee absences. Even when teams submit planned leave schedules, actual leave-taking often deviates significantly — especially during critical delivery phases. This tool learns each resource's individual leave behavior from historical data and predicts how much leave they are likely to actually take, giving managers an early warning to adjust staffing plans before the quarter begins.

How It Works

For each resource, the application collects:


Previous year's planned leave per quarter
Previous year's actual leave taken per quarter
Current quarter's planned leave


It trains a Random Forest Regressor on the four quarters of historical planned vs actual leave data and uses it to predict how much leave the resource will actually take in the current quarter. The model captures individual patterns — for example, a resource who consistently takes more leave than planned in Q3, or one who reliably under-uses their Q1 allocation.

Input

Entered manually through the UI for each resource:

FieldDescriptionResource NameName of the team memberQ1–Q4 PlannedPlanned leave days per quarter (previous year)Q1–Q4 TakenActual leave days taken per quarter (previous year)Current Quarter PlannedLeave days planned for the current quarter

Output

Predicted number of leave days the resource is likely to take in the current quarter, displayed directly in the application.

Tech Stack


Python 3.x
scikit-learn (Random Forest Regressor)
NumPy / Pandas
Tkinter (desktop UI)


How To Run


Install dependencies:


pip install scikit-learn pandas numpy


Run the application:


python P1.py


Enter the resource name, input the previous year's quarterly planned and actual leave data, enter the current quarter's planned leave, and click Predict Leaves.


Background

This tool was built independently as a practical solution to a recurring project planning problem. It was initially validated on one year of internal team data before being adopted more broadly. It reduces budget mismanagement caused by leave-related planning gaps.

License

Apache License 2.0
