class Stack:
  def __init__(self, size=5):
   self.data=[]
   self.size=size

  def push(self, data):
   if len(self.data)==self.size:   #full
    return
   self.data.append(data)

  def pop(self):
   if len(self.data)==0:     #empty
    return
   return self.data.pop()

  def clear(self):
   self.data=[]

  def __str__(self):
   return f"<stack size: {self.size}, data: {self.data} >"

def main():
 s1=Stack(10)
 s1.push(10)
 s1.push(20)
 s1.push(30)
 print(s1)

 print(s1.pop())
 print(s1.pop())
 print(s1.pop())
 print(s1.pop())

main()