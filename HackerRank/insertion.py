#!/bin/python3

import sys
from bisect import *

def insertion(array, el):
  for i in range(len(array)):
    array_el = array[i]
    if el < array_el:
      return array[:i] + [el] + array[i:]
    return array + [el]

def median(array, l):
  if l == 0:
    return "Empty list"
  if l%2 == 0:
    m1 = array[(l//2)-1]
    m2 = array[(l//2)]
    return (m1+m2)/2
  else:
    return array[l//2]


def activityNotifications(expenditure, d):
  nrOfNotifications = 0
  window = expenditure[0:d]
  sorted_window = sorted(window)
  #print(prev_d)
  for i in range(d,len(expenditure)):
    expence = expenditure[i]
    old = expenditure[i-d]
    median_expense = median(sorted_window, d)
    if expence >= 2*median_expense:
      nrOfNotifications+=1
    sorted_window.remove(old)
    insort(sorted_window, expence)
    #prev_d = insertion(prev_d,expence)
  
  return nrOfNotifications
    # Complete this function

