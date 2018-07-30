#this file serves to initially populate the Company and Employee models
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'database_editing.settings')

import django
django.setup()

import random
from app1.models import Company, Employee
from faker import Faker


def populate(companies = 5, employees = 5):
    fakegen = Faker()
    # choice of industriez
    industries = ["Energy", "Consulting", "Software", "Telecommunications", "Marketing", "Healthcare", "Fintech", "Entertainment"]

    for i in range(companies):


        cname = fakegen.company()
        hq = fakegen.city() + ', ' + fakegen.country()
        ind = random.choice(industries)
        fyear = fakegen.year()

        c = Company.objects.get_or_create(name = cname, headquarters = hq, industry = ind, founding_year = fyear)[0]

        for i in range(employees):
            ename = fakegen.name()
            epos = fakegen.job()
            locat = fakegen.city() + ', ' + fakegen.country()

            #since company is a foreign key, have to give it a value of a whole Company model object instance
            e = Employee.objects.get_or_create(name = ename, position = epos, location = locat, company = c)[0]

if __name__ == '__main__':
    print('populating...')
    populate(25,20)
    print('populating complete')