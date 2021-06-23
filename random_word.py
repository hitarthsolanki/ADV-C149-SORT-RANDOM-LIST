from tkinter import *
import random
root=Tk()
root.title("SORT RANDOM LIST")
root.geometry("500x500")
root.configure(bg="yellow")

alpha_list = ["A", "B", "C", "D", "E","F", "G", "H", "I", "J","K", "L", "M", "N", "O","P", "Q", "R", "S", "T","U", "V", "W", "X", "Y","Z"]
print(alpha_list)
random_friend = Label(root)

def random_wordf():
    random_no = random.randint(0,25)
    print(random_no)
    random_lucky_friend = alpha_list[random_no]
    print("Your Lucky friend is : ", random_lucky_friend)
    random_no = random.sample(range(0,10),5)
    random_friend["text"] = str(random_lucky_friend)
    random_no.sort()
    
btn1 = Button(root)
btn1 = Button(root, text = "Generate Random Word", command=random_wordf)    
btn1.place(relx = 0.5,rely = 0.5, anchor = CENTER)

random_friend.place(relx=0.5,rely=0.6, anchor=CENTER)
    
root.mainloop()
