b = open('modifiedjson.json', 'r').read().split('\n')
a = open('originaljson.json', 'r').read().split('\n')
c = open('newpairs.json', 'w')
c.write('\n'.join([comm for comm in b if not (comm in a)]))
c.close()