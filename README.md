# INFO SEC MODEL

# Password Strength Checker using XGBoost

## Description

This is a machine-learning model that checks the strength of passwords using the XGBoost algorithm. It classifies passwords into three categories: Weak, Moderate, and Strong based on their complexity and security. You can use this model to evaluate the strength of passwords and enhance security for your applications.

## Dataset 
The passwords used in our analysis are from 000webhost leak that is available online. And it has more than 66 lakhs of unique passwords.

## Installation

To run this password strength checker on your local machine, follow these steps:

### Cloning the repository

* Clone the repository using the command below :
```bash
git clone https://github.com/manan152003/info-sec_project.git

```

* Move into the directory where we have the project files : 
```bash
cd info-sec_project

```

* Create a virtual environment :
```bash
# Let's install virtualenv first
pip install virtualenv

# Then we create our virtual environment
virtualenv envname

```

* Activate the virtual environment :
```bash
source envname\scripts\activate

```

* Install the requirements :
```bash
pip install -r requirements.txt

```

#

### Running the App

To run the App, we use :
```bash
python3 app.py 

```
