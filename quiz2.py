import RPi.GPIO as GPIO
 import time
 GPIO.setmode(GPIO.BCM)
 GPIO.setwarnings(False)
 GPIO.setup(18,GPIO.OUT)

def quiz():
  print("welcome to quiz")
  print("answer the following questions:")

questions = [
  "1. which of following is not a python data type a.int b.float c.rational d.string e.bool",
  "2. which of following is not a built-in operation in python a.+ b.% c.abs() d.sqrt()",
  "3. in a mixed-type expression involing ints and floats, python will convert a.float to int b.ints to strings c.floats and ints to strings d.ints to floats",
  "4. the best structure for implementing a multi-way decision in python is: a.if b.if-else c.if-elif-else d.try",
  "5. what statement can be executed in the body of a loop to cause it to terminate a.if b.exit c.continue d.break"
]
answers = [
"rational"
"sqrt()"
"ints to floats"
"if-elif-else"
"break"
]
score = 0

for i in range(len(questions)):
  user_answer = input(questions[i]).strip().lower()
  if user_answer == answers[i]:
print("correct")
score +=1
GPIO.setup(17,GPIO.OUT)
print "LED on"
GPIO.output(17,GPIO.HIGH)
time.sleep(1)
print "LED off"
GPIO.output(17,GPIO.LOW)
  else:
print("incorrect")
GPIO.setup(18,GPIO.OUT)
print "LED on"
GPIO.output(18,GPIO.HIGH)
time.sleep(1)
print "LED off"
GPIO.output(18,GPIO.LOW)


print("\n quiz completed")
print("you got {score}/{len(quesitons)} questions correct")

quiz()
#writer: Zhou Yuwei
#date: 7/4/2025
#description: a quiz with LED
