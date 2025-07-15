name = 'Lillie'
experience = 1
projects = 1

print('Example 1:' ,'My name is' ,name ,'and I have level' ,str(experience), 'experience and', str(projects), 'projects.')

print('Example 2: ' + 'My name is ' + name + ' and I have level ' + str(experience) + ' experience and ' + str(projects) + ' projects.')

print(f'Example 3: My name is {name} and I have level {experience} experience and {projects} projects.')

name = input('Name: ')
experience = input('Your Experience: ')
projects = input('How many prohects have you done?: ')

print(f'Example 4: Hello World!, I am {name}, my experience is {experience} years and I have done {projects} projects.')
