#!/usr/bin/python

import sys
from faker import Faker
from subprocess import call

fake = Faker()
users = {}
count = sys.argv[1]

print("Generating " + str(count) + " test users.")

while len(users) < int(count):
    user = {
        'email' :   fake.email(),
        'name'  :   fake.first_name()
    }

    users[user['email']] = user

i = 1;

for key in users:
    call([
        'wp',
        'user',
        'create',
        users[key]['name'],
        users[key]['email'],
        '--role=subscriber',
        '--user_pass=Test123$'
    ])
    print("User " + str(i) + " of " + str(count) + " generated. " + users[key]['email'])
    i = int(i) + 1
