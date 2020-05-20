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

while (i < 50):

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

  # employee's avatar
  avatars = [
    "https://i.imgur.com/LpaY82x.png", 
    "https://i.imgur.com/Nmx0Qxo.png", 
    "https://i.imgur.com/T2WwVfS.png", 
    "https://i.imgur.com/FK8V841.jpg", 
    "https://i.imgur.com/twYrpay.jpg", 
    "http://icons.iconarchive.com/icons/dapino/people/48/black-man-icon.png", 
    "http://icons.iconarchive.com/icons/dapino/office-men/48/Man-Black-icon.png", 
    "http://icons.iconarchive.com/icons/dapino/office-men/48/Man-Grey-icon.png", 
    "http://icons.iconarchive.com/icons/dapino/office-men/48/Man-Grey-icon.png", 
    "http://icons.iconarchive.com/icons/dapino/people/48/grey-woman-icon.png", 
    "http://icons.iconarchive.com/icons/designbolts/free-male-avatars/48/Male-Avatar-Emo-Haircut-icon.png", 
    "http://icons.iconarchive.com/icons/designbolts/free-male-avatars/48/Male-Avatar-Bow-Tie-icon.png", 
    "http://icons.iconarchive.com/icons/designbolts/free-male-avatars/48/Male-Avatar-Goatee-Beard-icon.png", 
    "http://icons.iconarchive.com/icons/designbolts/free-male-avatars/48/Male-Avatar-Hair-icon.png", 
    "http://icons.iconarchive.com/icons/google/noto-emoji-people-profession/48/10233-man-judge-light-skin-tone-icon.png", 
    "http://icons.iconarchive.com/icons/google/noto-emoji-people-profession/48/10239-man-judge-medium-dark-skin-tone-icon.png", 
    "http://icons.iconarchive.com/icons/google/noto-emoji-people-profession/48/10303-man-office-worker-light-skin-tone-icon.png", 
    "http://icons.iconarchive.com/icons/google/noto-emoji-people-profession/48/10309-woman-office-worker-light-skin-tone-icon.png", 
    "http://icons.iconarchive.com/icons/dapino/office-women/48/eyes-office-women-glasses-icon.png", 
    "http://icons.iconarchive.com/icons/google/noto-emoji-people-profession/48/10312-woman-office-worker-medium-dark-skin-tone-icon.png", 
    "http://icons.iconarchive.com/icons/diversity-avatars/avatars/48/barack-obama-icon.png", 
    "http://icons.iconarchive.com/icons/diversity-avatars/avatars/48/donald-trump-icon.png", 
    "http://icons.iconarchive.com/icons/diversity-avatars/avatars/48/cristiano-ronaldo-icon.png", 
    "http://icons.iconarchive.com/icons/diversity-avatars/avatars/48/vladimir-lenin-icon.png", 
    "http://icons.iconarchive.com/icons/diversity-avatars/avatars/48/girl-in-ballcap-icon.png", 
    "http://icons.iconarchive.com/icons/diversity-avatars/avatars/48/dave-grohl-icon.png",
    "http://icons.iconarchive.com/icons/diversity-avatars/avatars/48/malcolm-x-icon.png",
    "http://icons.iconarchive.com/icons/diversity-avatars/avatars/48/andy-warhol-icon.png",
    "http://icons.iconarchive.com/icons/dapino/teenage-girl/48/girl-chuckle-icon.png",
    "http://icons.iconarchive.com/icons/iconshock/trendy-guys/48/andrew-icon.png"
  ]

  avatar = avatars[randrange(30)]

  # employees table SQL statement
  insert_employee = 'INSERT INTO employees (name, avatar, job_title, email, username, password, isAdmin) VALUES '
  insert_employee += "('{}', '{}', '{}', '{}', '{}', {}, '{}');\n".format(name, avatar, job, email, username, password, isAdmin)
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
virtue_buckets = [
  {"virtueName": "Execution", "img": "https://raw.githubusercontent.com/icncsx/teamric-client/8ab74201d314b719932d24569488f986d36e2e3b/public/execution.svg"},
  {"virtueName": "Knowledge", "img": "https://raw.githubusercontent.com/icncsx/teamric-client/8ab74201d314b719932d24569488f986d36e2e3b/public/knowledge.svg"}, 
  {"virtueName": "Courage", "img": "https://image.flaticon.com/icons/svg/1454/1454657.svg"}, 
  {"virtueName": "Humanity", "img": "https://raw.githubusercontent.com/icncsx/teamric-client/8ab74201d314b719932d24569488f986d36e2e3b/public/humanity.svg"}, 
  {"virtueName": "Justice", "img": "https://raw.githubusercontent.com/icncsx/teamric-client/8ab74201d314b719932d24569488f986d36e2e3b/public/justice.svg"}, 
  {"virtueName": "Transcendence", "img": "https://raw.githubusercontent.com/icncsx/teamric-client/8ab74201d314b719932d24569488f986d36e2e3b/public/transcendence.svg"}, 
  {"virtueName": "Temperance", "img": "https://raw.githubusercontent.com/icncsx/teamric-client/8ab74201d314b719932d24569488f986d36e2e3b/public/temperance.svg"}
]

for x in virtue_buckets:
  insert_virtue_bucket = 'INSERT INTO virtue_buckets (name, img) VALUES '
  insert_virtue_bucket += "('{}', '{}');\n".format(x["virtueName"], x["img"])
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
