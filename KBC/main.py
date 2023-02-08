import random

#To Create 10 random Number List (Non repeatable) 
def generate_l(randomList):
    count = 0
    for i in range(25):
        r=random.randint(1,30)
        if r not in randomList:
            randomList.append(r)
            count+=1
            if (count==10):
                break
    return randomList

# To Extrat all Questions for txt file to List  
def extrat_all_Q(randomList):
    with open(r"Questions.txt", 'r',encoding="utf8") as fp:
        line_numbers = []
        for i in randomList:
            pos = i - 1
            pos = pos * 4
            for j in range(4):
                line_numbers.append(pos)
                pos = pos+1
        # To store lines
        for i, line in enumerate(fp):
        # read lines
            if i in line_numbers:
                lines.append(line.strip())
            elif i > 200:
                # don't read after line 200 to save time
                return lines    

#To divide each Question in Sub List
def slice_Q(q_l,lines):
    for i in range(len(lines)):
        if(i%4==0 or i == 0):
            q_l.append(lines[i:i+3])

# Read and play The Game
def play(q_l,q_count,randomList,res,l_count,money):
    for i in q_l:

        q_no = "Q."+ str(q_count)
        q_count +=1
        print("-------------------------|{}|--------------------------".format(q_no))

        for k in i:
            print("\n",k)
        n = input("\nEnter Your Answer:")
        lst = sorted(randomList)
        key = lst[l_count]

        if (n==res[key]):
            print("Option {} is Correct Answer.!!".format(n))
            print("You Won = {} Rs\n".format(money[l_count+1]))
        else:
            print("Option {} is Wrong Answer.!!".format(n))
            print("You Won = {} Rs\n".format(money[l_count]))
            break
        l_count+=1

if __name__ == "__main__":
    randomList=[]
    q_l = []
    lines = []
    q_count = 1
    l_count = 0
    res = {1:'B',2:'A',3:'D',4:'A',5:'C',6:'A',7:'C',8:'B',9:'D',10:'A',
        11:'D',12:'A',13:'C',14:'C',15:'D',16:'A',17:'B',18:'A',19:'C',20:'D',
        21:'B',22:'C',23:'D',24:'B',25:'C',26:'A',27:'C',28:'D',29:'B',30:'A'}

    money = ["0 rs","1 Lakh","5 Lakh","10 Lakh","25 Lakh","50 Lakh",
             "60 Lakh","70 Lakh","80 Lakh","90 Lakh","1 Cr"]

    generate_l(randomList)
    print(sorted(randomList))
    extrat_all_Q(randomList)
    slice_Q(q_l,lines)
    play(q_l,q_count,randomList,res,l_count,money)