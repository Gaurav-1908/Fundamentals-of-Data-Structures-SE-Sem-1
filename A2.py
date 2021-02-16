
"""Write a Python program to store marks scored in subject “Fundamental of Data
   Structure” by N students in the class. Write functions to compute following:
	a) The average score of class
	b) Highest score and lowest score of class
	c) Count of students who were absent for the test
	d) Display mark with highest frequency"""

from array import *

def getdata():
	global N
	N=int(input("Enter No. of Students:"))
	marks=array('f',[])
	
	for i in range(1,N+1):
		print("Enter marks of students of roll no.",i,":",end='')
		mark=float(input())
		marks.append(mark)
	
	global score
	score=[-1]
	for j in range(N):
		score.append(marks[j])
	
def avg():
	sum=0
	for i in range(1,N+1):
		if(score[i]==-1):
			continue
		sum=sum+score[i]
	print("Average Score Of class is : ",sum/N)
	
def minmax():
	for i in range(N-1):
		for j in range(N-i):
			if(score[j]>score[j+1]):
				temp=score[j]
				score[j]=score[j+1]
				score[j+1]=temp			
	print("Max Score of class is : ",score[N])	
	
	for i in range(N+1):
		if(score[i]!=-1):
			break
	print("Min Score of Class is : ",score[i])
	
def absent():
	count=-1
	for i in range(N+1):
		count=count+1
		if(score[i]!=-1):
			break
	print("No. of absent Students : ",i-1)
	
def frequency():
	max=1
	count=1
	score1=[]
	
	for i in range(1,N+1):
		if(score[i]==-1):
			continue
		else:
			score1.append(score[i])
	
	for i in range(len(score1)):
		if (score1[i]==score1[i-1]):
			count+=1
			
		else:
			if (count>max):
				max=count
				print(score1[i-1])
				
			count=1
			
	if (count>max):
		max=count
		print(max)
		print("Maximum repeated Score is : ",score1[i-1])
				
getdata()
avg()
absent()
minmax()
frequency()
