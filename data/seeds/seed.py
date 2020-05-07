import os
from random import randrange
import random
import names


# Create and open seed file

path = 'data/seeds/00_seed.sql'
if os.path.exists(path):
  os.remove(path)
f = open(path, 'w+')


# Hardcode truncate clauses

string = ''
truncates = 'TRUNCATE employees CASCADE;\n'
truncates += 'TRUNCATE person_assessments CASCADE;\n'
truncates += 'TRUNCATE virtue_buckets CASCADE;\n'
truncates += 'TRUNCATE virtues CASCADE;\n\n'
f.write(truncates)


# Seed employees table

i = 0

jobs = ['Junior Front-End Developer', 'Senior Front-End Developer', 'Seo Consultant', 'Web Analytics Developer', 'Digital Marketing Manager', 'Social Media Manager', 'Junior Designer', 'Senior Designer', 'Information Architect', 'UX Designer', 'Lead Developer', 'UI Designer', 'Accessibility Specialist', 'Interaction Designer', 'Junior Backend Developer', 'Senior Backend Developer', 'Mobile Developer', 'Junior Full-Stack Developer', 'Senior Full-Stack Developer', 'Social Media Specialist', 'Digital Marketing Specialist', 'Business Systems Analyst', 'Systems Engineer', 'Systems Administrator', 'Systems Manager', 'Database Administrator', 'Database Manager', 'Data Architect']

while (i < 100):

  # employees.name
  name = names.get_full_name()

  job = jobs[randrange(28)]

  # employees.email
  email = name.replace(" ", "").lower()
  email += '@email.com'

  random_number = str(random.randint(1, 100156))
  username = name.lower().split(" ", 1) 
  username = username[0] + random_number

  # employees.password
  password = random_number

  isAdmin = 'false'

  # employees table SQL statement
  insert_employee = 'INSERT INTO employees (name, job_title, email, username, password, isAdmin) VALUES '
  insert_employee += "('{}', '{}', '{}', '{}', {}, '{}');\n".format(name, job, email, username, password, isAdmin)
  f.write(insert_employee)

  # next employee
  i += 1

f.write('\n')

# Seed person_assessments
i = 1
while (i < 50):
  employee_id = random.randint(1, 100)
  target_employee_id = random.randint(1, 100)
  survey_id = random.randint(1, 10000)

  insert_person_assessment = 'INSERT INTO person_assessments (employee_id, survey_id, target_employee_id) VALUES '
  insert_person_assessment += "({}, {}, {});\n".format(employee_id, survey_id, target_employee_id)

  f.write(insert_person_assessment)

  i += 1

f.write('\n') 

# Seed virtue buckets table
virtue_buckets = ['Execution', 'Knowledge', 'Courage', 'Humanity', 'Justice', 'Transcendence', 'Temperance']

for x in virtue_buckets:
  insert_virtue_bucket = 'INSERT INTO virtue_buckets (name) VALUES '
  insert_virtue_bucket += "('{}');\n".format(x)
  f.write(insert_virtue_bucket)

f.write('\n')

# Seed virtues table
virtues = {
  1: ['Fearless agility', 'Time conscious', 'Pushing through', 'Defiance', 'motivating others', 'Assertive', 'Perceiving the problem', 'Goal oriented', 'Clear vision', 'Practical', 'Prioritizing'],
  2: ['Curiosity', 'Analytical', 'Detail oriented', 'Strategic', 'Research', 'probing', 'Precise'],
  3: ['Bravery', 'Persistence', 'Persevering', 'Vitality', 'Critique'],
  4: ['Social intelligence', 'Delegating', 'Conflict resolving', 'Trustworthy', 'Cultural intelligence', 'Good listener'],
  5: ['Authenticity', 'Fairness', 'Responsible', 'Honesty', 'Objective', 'Integrity', 'Radically transparent', 'Believable'],
  6: ['Creativity', 'Appreciation', 'Optimism', 'Determinism', 'Motivating', 'Visionary'],
  7: ['Merciful', 'Humble', 'Prudence', 'Self-regulating', 'Self-aware', 'Steadiness', 'Composed', 'Reflective', 'Stable mind']
}

for key in virtues:
  for x in virtues[key]:
    virtue_bucket_id = key
    insert_virtues = 'INSERT INTO virtues (virtue_bucket_id, name) VALUES '
    insert_virtues += "({}, '{}');\n".format(virtue_bucket_id, x)
    f.write(insert_virtues)

f.close()
