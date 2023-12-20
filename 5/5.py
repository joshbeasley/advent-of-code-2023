

def in_range(mapping, source):
  if source >= mapping[1] and source < mapping[1] + mapping[2]:
    return True
  return False

def execute_mapping(mapping, source):
  return source - mapping[1] + mapping[2]

print(execute_mapping())