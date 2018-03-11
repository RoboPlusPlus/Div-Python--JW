import random
import re

run_app = 1
done_loop = 0
while run_app ==1:
    done_loop = 0
    print("\n\ntype -'keyword' - 'number of dice' - 'd' - 'sides on dice'\n")
    print("For list of keywords and examples, type'?'")
    print("Type 'exit' to exit")

    raw_input = input()
    user_input = raw_input.lower()

    if user_input == "?":
        print("\n\n##### Keywords and info #####\n")
        print("Keyword 'roll' will roll a number of dice of a given type, \nprint the individual rolls and print the total")
        print("Example: 'roll 3d6' might give an output = [3, 5, 3, total 11]\n")
        print("Keyword 'avg' returns the average of your specified dice")
        print("Example 'avg 4d4' returns [1, 3, 2, 2] avg = 2.0\n")
        print("##########")

        print("\n\n\n")
        done_loop = 1



    #vurerer user-input.
        
    if done_loop == 0:

        try:            #sjekker om to-ords user-input hvor andre ord inneholder d
            keyword, xdy = user_input.split(" ")

            number_of_dice, sides_on_dice = xdy.split("d")
            
        except:
            try:        #sjekker om ett-ords input i format 
                keyword = user_input.split(" ")
            except:
                print("not able to parse " + user_input)
                done_loop = 1



    #hvis "exit"
                
    if user_input == "exit":
        done_loop = 1
        run_app = 0



    #Hvis keyword = "roll"
        
    if keyword == "roll":
        roll_total = 0
        roll_result = []
        for i in range(0, int(number_of_dice)):
           roll_result.append(random.randrange(1,int(sides_on_dice)))
                              
        print("roll results = " + str(roll_result))

        for j in roll_result:
            roll_total = roll_total + j
        print("Roll Total = " + str(roll_total))


    
    #Hvis keyword = "avg"
        
    if keyword == "avg":
        roll_total = 0
        roll_result = []
        for i in range(0, int(number_of_dice)):
           roll_result.append(random.randrange(1,int(sides_on_dice)))
                              
        print("roll results = " + str(roll_result))

        for j in roll_result:
            roll_total = roll_total + j
        print("Roll average = " + str(roll_total/int(number_of_dice)))



    #Hvis keyword = "fav"
    if keyword == "fav":
        roll_result = []
        for i in range(0, int(number_of_dice)):
           dice_result = random.randrange(1,int(sides_on_dice))
           roll_result.append(dice_result)

        roll_result.sort()
        print("removed " + str(roll_result[0]))
        del(roll_result[0])
        print("roll results = " + str(roll_result))


        
    #Hvis keyword = "unfav"
    if keyword == "unfav":
        roll_result = []
        for i in range(0, int(number_of_dice)):
           dice_result = random.randrange(1,int(sides_on_dice))
           roll_result.append(dice_result)

        roll_result.sort()
        print("removed " + str(roll_result[int(number_of_dice)-1]))
        del(roll_result[int(number_of_dice)-1])
        print("roll results = " + str(roll_result))
        
    
