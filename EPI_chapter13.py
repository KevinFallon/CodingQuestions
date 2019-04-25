import collections


# Question 13.1: Computer the intersection of 2 sorted arrays
def intersect_two_sorted_arrays(A, B):
  i, j, result = 0, 0, []
  while i < len(A) and j < len(B):
    if A[i] == B[j]:
      if i == 0 or A[i] != A[i-1]:
        result.append(A[i])
      i, j = i + 1, j + 1
    elif A[i] > B[j]:
      j += 1
    else:
      i += 1
  return result


A = [2,3,3,5,5,6,7,7,8,12]
B = [5,5,6,8,8,9,10,10]
print(intersect_two_sorted_arrays(A, B) == [5,6,8])
print(intersect_two_sorted_arrays(A, []) == [])

def merge_sorted_arrays(A, len_A, B, len_B):
  i, j, write = len_A - 1, len_B - 1, len_A + len_B - 1
  while i >= 0 and j >= 0:
    if A[i] > B[j]:
      A[write] = A[i]
      i -= 1
    else:
      A[write] = B[j]
      j -= 1
    write -= 1
  while j >= 0:
    A[write] = B[j]
    j, write = j - 1, write - 1
  return A

first_A = [5, 13, 17,0,0,0,0,0]
second_A = [3,7,11,19]
print(merge_sorted_arrays(first_A, 3, second_A, 4) == [3, 5, 7, 11, 13, 17, 19, 0])

# 13.3 Remove first-name duplicates

class Name:
  def __init__(self, first, last):
    self.first, self.last = first, last

  def __eq__(self, other):
    return self.first == other.first

  def __lt__(self, other):
    if self.first != other.first:
      return self.first < other.first
    else:
      return self.last < other.last

  def __repr__(self):
    return self.first

def remove_dupe_names(A):
  A.sort()
  write_idx = 1
  for name in A[1:]:
    if name != A[write_idx - 1]:
      A[write_idx] = name
      write_idx += 1
  del A[write_idx:]

name_1 = Name("Ian", "Bell")
name_2 = Name("David", "Gower")
name_3 = Name("Ian", "Ver")
name_4 = Name("Kevin", "Fallon")
name_5 = Name("Kevin", "William")

names = [name_1, name_2, name_3, name_4, name_5]
remove_dupe_names(names)
print(list(map(lambda x: x.first, names)) == ["David", "Ian", "Kevin"])



# 13.5 Render a calendar - Write a program that takes a set of events, and determines the maximum
# number of events that take place concurrently.

CalEvent = collections.namedtuple('Event', ('start', 'finish')) # Made up of end points
Endpoint = collections.namedtuple("Endpoint", ("time", 'is_start'))

def find_max_concurrent_events(cal_events):
  end_points = []
  for event in cal_events:
    end_points.append(Endpoint(event.start, True))
    end_points.append(Endpoint(event.finish, False))

  end_points.sort(key=lambda e: (e.time, not e.is_start))
  max_concurrent_events, curr_concurrent_events = 0, 0
  for end_point in end_points:
    if end_point.is_start:
      curr_concurrent_events += 1
      max_concurrent_events = max(curr_concurrent_events, max_concurrent_events)
    else:
      curr_concurrent_events -= 1
  return max_concurrent_events

event_array = []
for pair in [ [1,5], [6,10], [11,13], [14, 15], [2, 7], [8,10], [12,15], [4, 5], [9,17] ]:
  event_array.append(CalEvent(pair[0], pair[1]))
print(find_max_concurrent_events(event_array) == 3)
