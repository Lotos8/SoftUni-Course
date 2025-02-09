old_version = input().split('.')
next_version = int(''.join(old_version)) + 1
new_version = str(next_version)

print('.'.join(new_version))