from cat import Cat

print("Welcome to my Cat Game!")

name = input("Enter Cat name: ")
colour = input("Enter Cat's colour: ")

my_cat = Cat(name,colour)
while True:
    action = input("""
What would you like to do:
1. Train
2. Feed
3. Play
4. Sleep
5. Show Stats
""")

    if action == '1':
        my_cat.train()
    elif action == '2':
        my_cat.feed()
    elif action == '3':
        my_cat.play()
    elif action == '4':
        my_cat.sleep()
    elif action == '5':
        my_cat.showStatsj()
    else:
        print("That was not an option.")