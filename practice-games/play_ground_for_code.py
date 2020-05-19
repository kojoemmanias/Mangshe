import random

#count,before assign gift score += 100

def roll_the_die():
    the_die = random.randint(1,6)
    return the_die


roll_result = []
dice = 0
num_of_dice_to_use = 6
score = 0

one_box = 0
two_box = 0
three_box = 0
four_box = 0
five_box = 0
six_box = 0

#rolling all dice
while dice < num_of_dice_to_use:
    roll_result.append(roll_the_die())
    #print(roll_result[dice])
    dice += 1

#print(f"And finally we have:\n {roll_result}")


#roll_result = [1,1,1,1,1,1]
#roll_result = [1,2,3,4,5,6]
#roll_result = [1,1,2,2,3,3]
#roll_result = [4,2,2,3,4,3]
#roll_result = [4,2,2,3,2,3]
#roll_result = [1,2,2,3,2,3]
#roll_result = [4,6,5,6,1,3]
#roll_result = [4, 3, 1, 5, 1, 2]
#roll_result = [4, 5, 1, 5, 1, 2]
# roll_result = [1,1,2,2,1,3]
# roll_result = [1,1,2,5,1,3]
# roll_result = [1,1,2,5,1,5]
#roll_result = [5, 2, 3, 3, 5, 2]
#roll_result = [5, 5, 1, 1, 4, 1]
#roll_result = [1, 6, 4, 6, 2, 3]
#roll_result = [5, 2, 5, 2, 5, 3]
#roll_result = [4, 2, 4, 2, 4, 3]

#testing
print(f"we are dealing with {roll_result} okay")

#counting them
for target in roll_result:
    #print(target)
    if target == 1:
        one_box += 1
    elif target == 2:
        two_box += 1
    elif target == 3:
        three_box += 1
    elif target == 4:
        four_box += 1
    elif target == 5:
        five_box += 1
    elif target == 6:
        six_box += 1
    else:
        print("something is wrong")
the_count = [one_box, two_box, three_box, four_box, five_box, six_box]
print(f"These are the break downs\n1 = {one_box}\n2 = {two_box}\n3 = {three_box}\n4 = {four_box}\n5 = {five_box}\n6 = {six_box}")




#inspect them
dice_are_there = 0
while dice_are_there < num_of_dice_to_use:
    #print("am in")
    if one_box == two_box == three_box == four_box == five_box == six_box == 1:
        print("You win 1000 points for seq")
        score += 1000
        break
    elif two_box == three_box == four_box == five_box == six_box == 0 and one_box == 6:
        print("You win all")
        score = "You win all"
        break
    elif (one_box >= 1) and (one_box < 3):
        print("You win 100 points for one dice")
        score += 100
        one_box -= 1
    elif (five_box >= 1) and (five_box < 3):
        print("You win 50 points")
        score += 50
        five_box -= 1
        inform = True
    elif one_box == 3:
        print("You win 1000 points")
        score += 1000
        num_of_dice_to_use -= 3
        break
    elif two_box == 3:
        print("You win 200 points")
        score += 200
        two_box -= 3
        num_of_dice_to_use -= 3
        break
    elif three_box == 3:
        print("You win 300 points")
        score += 300
        num_of_dice_to_use -= 3
        break
    elif four_box == 3:
        print("You win 400 points")
        score += 400
        num_of_dice_to_use -= 3
        break
    elif five_box == 3:
        print("You win 500 points")
        score += 500
        num_of_dice_to_use -= 3
        break
    elif six_box == 3:
        print("You win 600 points")
        score += 600
        num_of_dice_to_use -= 3
        break
    else:
        spoted = 0
        for look_out in the_count:
            if look_out == 2:
                spoted += 1
        if spoted == 3:
            print("You win 1000 points for 3 pairs")
            score += 1000
            if inform == True:
                score -= 100
            the_count.clear()
            break
            #the_count[look_out] = 0 #anew
            #print(f"look into {the_count[look_out]}")
    dice_are_there += 1
    bring = num_of_dice_to_use - 1
    #print(f"The end {dice_are_there}")
#print(f"why you {dice_are_there}")
print(f"The score is {score}")
#print(f"The score is {score} and these are the break downs\n1 = {one_box}\n2 = {two_box}\n3 = {three_box}\n4 = {four_box}\n5 = {five_box}\n6 = {six_box}")


# a=0
# b=0
# c=0
# u = [a,b,c]

#print(the_count)
