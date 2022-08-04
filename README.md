# API SET UP and USAGE

REST API to track bank account transactions

Built with Python 3.8 and SQLite Database

### Installation

1. Create and activate a virtual environment and Clone the project.

2. Move into the project folder
   ```
   $ cd transfx
   ```

3. Install dependencies 
   ```
   $ pip install -r requirements.txt
   ```

4. Create a `.env` file from the `.env.sample` file.  Replace the variables in the sample file with the actual variables.

5. Run migrations
   ```
   python manage.py migrate
   ```

6. Start server
   ```
   python manage.py runserver
   ```

7.  The application can be accessed here http://127.0.0.1:8000/

8. Run tests
   ```
   python manage.py test
   ```

9. Populate customers
   ```
   python manage.py loaddata customers.json
   ```

### Endpoints

Request    | Endpoints                                      |       Functionality 
-----------|------------------------------------------------|--------------------------------
POST       |  `/api/v1/accounts/`                           | Create Account for customer  {"customer": customer_id, "balance": 19000.00}
POST       |  `/api/v1/transfers/`                          | Transfer btn accounts  {"customer": customer_id, "sender_account": account_id, "recipient_account": account_id, "amount": 100.00}.
GET        |  `/api/v1/account-balance/account_id/`         | Retrieve account balance
GET        |  `/api/v1/account-transactions/account_id/`    | Retrieve account transactions
