'''
PEOPLE = [{'first':'Reuven', 'last':'Lerner',
    'email':'reuven@lerner.co.il'},
 {'first':'Donald', 'last':'Trump',
    'email':'president@whitehouse.gov'},
 {'first':'Vladimir', 'last':'Putin',
    'email':'president@kremvax.ru'}
 ]
write a function, alphabetize_names, that assumes the existence of a PEOPLE constant defined as shown in the code.
The function should return the list of dicts, but sorted by last name and then by first name.
'''
PEOPLE_LIST = [
{'first':'Reuven', 'last':'Lerner',
    'email':'reuven@lerner.co.il'},
 {'first':'Donald', 'last':'Trump',
    'email':'president@whitehouse.gov'},
{'first':'Ashish', 'last':'Trump',
    'email':'president@whitehouse.gov'},
 {'first':'Vladimir', 'last':'Putin',
    'email':'president@kremvax.ru'}
 ]

def alphabetize_names(people):
    return sorted(people, key=lambda x: (x['last'], x['first']))

if __name__ == "__main__":
    print(alphabetize_names(PEOPLE_LIST))