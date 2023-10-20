# 1) Set users variable to an empty list
users = []

assert users == [], f"Expected `users` to be [] but got: {repr(users)}"

# 2) Add kevin, bob, alice and the users list
users.append('kevin')
users.append('bob')
users.append('alice')

assert users == ['kevin', 'bob', 'alice'], f"Expected `users` to be ['kevin', 'bob', 'alice'] but got: {repr(users)}"

# 3) Remove bob from the users list without reassiging the variable
del users[1]

assert users == ['kevin', 'alice'], f"Expected `users` to be ['kevin', 'alice'] but got: {repr(users)}"

# 4) Reverse users list and assign result to rev_users
rev_users = list(reversed(users))

assert rev_users == ['alice', 'kevin'], f"Expected `users` to be ['alice', 'kevin'] but got: {repr(rev_users)}"

# 5) Add melody to users list in bobs previous position
users.insert(1, 'melody')

assert users == ['kevin', 'melody', 'alice'], f"Expected `users` to be ['kevin', 'melody', 'alice'] but got: {repr(users)}"

# 6) Add users andy, wanda, and jim to users list in a single command
users += ['andy', 'wanda', 'jim']

assert users == ['kevin', 'melody', 'alice', 'andy', 'wanda', 'jim'], f"Expected `users` to be ['kevin', 'melody', 'alice', 'andy', 'wanda', 'jim'] but got: {repr(users)}"

# 7) Slice users and return 3rd and 4th items and assign to center_users
center_users = users[2:4]

assert center_users == ['alice', 'andy'], f"Expected `users` to be ['alice', 'andy'] but got: {repr(users)}"