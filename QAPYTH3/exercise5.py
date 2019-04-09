#!/usr/bin/python3

machines = {'user100': 'yogi',
    'user1' : 'booboo',
    'user2' : 'rupert',
    'user3' : 'teddy',
    'user4' : 'care',
    'user5' : 'winnie',
    'user6' : 'sooty',
    'user7' : 'padders',
    'user8' : 'polar',
    'user9' : 'grizzly',
    'user10' : 'baloo',
    'user11' : 'bungle',
    'user12' : 'fozzie',
    'user13' : 'huggy',
    'user14' : 'barnaby',
    'user15' : 'hair',
    'user16' : 'greppy'}


machines['user14'] = None
print(machines)
machines['user15'] = 'cinnamon'
print(machines)
machines['user17'] = machines['user16']
del machines['user16']
print(machines)
unallocated = []
for user in ('user4', 'user5', 'user6'):
    unallocated += [machines.pop(user)]
print(machines)
machines['user8'] = [machines['user8'], 'kodiak']
print(machines)

for user, machine in machines.items():
    print(user, machine)

print(sorted(unallocated))
