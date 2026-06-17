def create_staircase_a(nums):
  while len(nums) != 0:
    step = 1
    subsets = []
    if len(nums) >= step:
      subsets.append(nums[0:step])
      nums = nums[step:]
      step += 1
    else:
      return False

  return subsets


def create_staircase_b(nums):
  step = 1
  subsets = []
  while len(nums) != 0:
    if len(nums) >= step:
      subsets.append(nums[0:step])
      nums = nums[step:]
      step += 1
    else:
      return False
      
  return subsets

list_of_data = [
  [1, 2, 3, 4, 5, 6],
  [1, 2, 3, 4, 5, 6, 7]
]
for x in list_of_data:
  print('Input data: ', x)
  print('Starting func A')
  print(create_staircase_a(x))
  print('Starting func B')
  print(create_staircase_b(x))