import os
from random import randrange
import random
from datetime import date
import random
import pickle
import lorem

# Create and open seed file

path = 'data/surveys/surveys.js'
if os.path.exists(path):
  os.remove(path)
f = open(path, 'w+')

f.write('module.exports = [ ')
f.write('\n')

#Seed survey table
i = 0

while (i < 1000):
  reviewerId = randrange(1, 101)
  receiverId = randrange(1, 101)

  if reviewerId == receiverId:
    receiverId += 1

  f.write('{')
  f.write('reviewerId: ' + str(reviewerId) + ',')
  f.write('\n')
  f.write('receiverId:' + str(receiverId) + ',')
  f.write('\n')

  start_dt = date.today().replace(day=1, month=1, year=2017).toordinal()
  end_dt = date.today().toordinal()
  random_day = date.fromordinal(random.randint(start_dt, end_dt))
  dateCreatedAt = random_day

  f.write('createdAt: ' + 'new Date(' + '"' + str(dateCreatedAt) + '"' + ')' + ',')
  f.write('\n')

  numberOfSkills = randrange(1, 10)
  f.write('feedback: [')

  for x in range(0, numberOfSkills):
    skillId = random.randint(1, 52)
    rating = random.randint(1, 5)
    description = lorem.sentence()

    f.write('{' + 'skillId: ' + str(skillId) + ',' + 'rating: ' + str(rating) + ',' + 'description: ' + '"' + description + '"' + '},')
    f.write('\n')
  
  f.write(']')
  f.write('\n')
  f.write('},')
  f.write('\n')

  i += 1

f.write(']')


