## https://programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(len(words)):
        s = s.replace(words[i], str(i))

    return int(s)
  
  
  ################
  
  def solution(s):
    s=s.replace('one', '1')
    s=s.replace('two', '2')
    s=s.replace('three', '3')
    s=s.replace('four', '4')
    s=s.replace('five', '5')
    s=s.replace('six', '6')
    s=s.replace('seven', '7')
    s=s.replace('eight', '8')
    s=s.replace('nine', '9')
    s=s.replace('zero', '0')
    return int(s)