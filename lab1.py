
def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   if int_list is None:
      raise ValueError
   max_int = int_list[0]
   for num in int_list:
      if num > max_int:
         max_int = num
   return max_int

def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   if int_list is None:
      raise ValueError
   if len(int_list) == 1:
      return int_list
   reverse = [int_list.pop(-1)]
   return reverse + reverse_rec(int_list)

def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   if len(int_list) == 0:
      return None
   if int_list is None:
      raise ValueError
   if high < low:
      raise ValueError
   middle = (high + low) // 2
   if int_list[middle] == target:
      return middle
   elif target > int_list[middle]:
      return bin_search(target, middle + 1, high, int_list)
   elif target < int_list[middle]:
      return bin_search(target, low, middle - 1, int_list)
