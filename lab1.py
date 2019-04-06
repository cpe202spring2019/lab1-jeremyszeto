
def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
# if list is None, raises ValueError
   if int_list is None:
      raise ValueError
# if list is empty, returns None
   if len(int_list) == 0:
      return None
# set max to first item in list, reassign max to the biggest number while traversing the list
   max_int = int_list[0]
   for num in int_list:
      if num > max_int:
         max_int = num
   return max_int


def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
# if list is None, raises ValueError
   if int_list is None:
      raise ValueError
# if list is empty, returns empty list
   if len(int_list) == 0:
      return []
# if list is one item, returns list
   if len(int_list) == 1:
      return int_list
# else return last item in list added to reversed list slice excluding last item until all items accounted for
   return [int_list[-1]] + reverse_rec(int_list[0:-1])


def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
# if list is None, raises ValueError
   if int_list is None:
      raise ValueError
# if list is empty (target not found), return none
   if len(int_list) == 0:
      return None
# if high index lower than low index, return none since this should be impossible
   if not low < high:
      return None
# binary search algorithm
   middle = (high + low) // 2
   if int_list[middle] == target:
      return middle
   elif target > int_list[middle]:
      return bin_search(target, middle + 1, high, int_list)
   elif target < int_list[middle]:
      return bin_search(target, low, middle - 1, int_list)
