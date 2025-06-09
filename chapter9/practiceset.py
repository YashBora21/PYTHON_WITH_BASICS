"""
with open("poem.txt") as f:
    content=f.read()
    if "twinkle" in content:
        print("is present ")
    else:
        print("not")
"""
'''
import random 

def game():
    score=random.randint(1,50)
    print("your are playing game...")
    


    with open("poem.txt") as f:
      highscore=f.read()
      if (highscore!=""):
        highscore=int(highscore)
      else:
        highscore=0
    print(f" your score is: {score}")

    if score>highscore or highscore=="":
        with open("poem.txt","a") as f:
            f.write(str(score))
     
    return score

game()'''
'''
import random 

def game():
    score = random.randint(1, 50)
    print("you are playing game...\n")  # Fixed: don't overwrite print

    with open("poem.txt") as f:
        highscore = f.read()
        if highscore != "":
            highscore = int(highscore)
        else:
            highscore = 0

    print(f"your score is: {score}")

    if score > highscore:
        with open("poem.txt", "w") as f:  # Changed from 'a' to 'w' to overwrite with new highscore
            f.write(str(score))

    return score

game()
'''

'''
def genratetable(n):
  table=""
  for i in range(1,11):
    table+=(f"{n} X {i} = {n*i} \n")

  with open(f"table/table_{n}","w") as f:
    f.write(table)



for i in range(2,21):
  genratetable(i)
'''
words=["donkey","bad","shame"]
content=""
with open("poem.txt") as f:
    content=f.read()
for word in words:
   content = content.replace(word, "#"*len(word))

# Step 3: Write the updated content back to the file
with open("poem.txt", "w") as f:
    f.write(content)

#to wipeout content 
with open("poem.txt", "w") as f:
    f.write("")
