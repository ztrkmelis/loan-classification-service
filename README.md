Loan Classification Service
Loan Classification Service can be used to check customer eligibility for a loan.

Given a user key, service provides the possible reply of a loan application of the related user. This wayi it would be useful for the speeding up the decision making process.

Project Setup
To set up the project environment, follow these steps:

Clone the repository:

            https://github.com/ztrkmelis/loan-classification-service.git
Install the required dependencies:

            pip install -r requirements.txt
Create virtual anvironment

            python3 -m venv venv
            source venv/bin/activate
Data
The data used in this includes various loan related information of a user.

Example Request Body
Service only needs a valid user key. If request doesn't provides any valid user key, it will show an exception as "please provide a valid user key".

Example request body (valid user key):

<img width="450" alt="image" src="https://github.com/ztrkmelis/loan-classification-service/assets/45657589/a6700816-7d17-4bf3-9f19-0c765594d5be">


Example Response

Service provides the loan status of a valid user key.

Example Response Body (valid user key):

<img width="251" alt="image" src="https://github.com/ztrkmelis/loan-classification-service/assets/45657589/8728a795-e0f6-41a0-89db-72008ec262e9">


Example Response Body (non-valid user key):

<img width="406" alt="image" src="https://github.com/ztrkmelis/loan-classification-service/assets/45657589/a1d3986f-0efd-4b82-ac87-a1eaca4ca27b">
