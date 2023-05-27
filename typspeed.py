from time import * 
import random
def error_check(orig,us):
    error = 0 
    for i in range(len(orig)):
        try:
            if orig[i] != us[i]:
                error += 1
        except :
            error += 1
    return error

def speed_t(t_ip,t_op,userip):
    t_total = t_op - t_ip
    t_def = round(t_total,3)
    speed_check = round(len(userip)/t_def,3)
    return speed_check
print("Let's check how fast you can type.\nYou'll be provided with 3 levels abd then we'll calculate your avg typing speed...\n")
level_1 = "Shakesphere wrote that If money go before, all ways do lie open."
print(f"Level 1: {level_1}")
time_before=time()
uinput = input("Enter: ")
time_after = time()
print()
print()
print(f"Speed: {speed_t(time_before,time_after,level_1)} words/sec")
print()
print(f"Errors: {error_check(level_1,uinput)}")
print()

level_2 = "If I were to kiss you then go to hell, I would. So then I can brag with the devils I saw heaven without ever entering it."
print(f"Level 2: {level_2}")
time_before2=time()
uinput = input("Enter: ")
time_after2 = time()
print()
print()
print(f"Speed: {speed_t(time_before2,time_after2,level_2)} words/sec")
print()
print(f"Errors: {error_check(level_2,uinput)}")
print()

level_3 = "One half of me is yours, the other half is yours, Mine own, I would say; but if mine, then yours, And so all yours."
print(f"Level 3: {level_3}")
time_before3=time()
uinput = input("Enter: ")
time_after3 = time()
print()
print()
print(f"Speed: {speed_t(time_before3,time_after3,level_3)} words/sec")
print()
print(f"Errors: {error_check(level_3,uinput)}")
print()
print(f"Your average speed is: {(speed_t(time_before,time_after,level_1)+speed_t(time_before2,time_after2,level_2)+speed_t(time_before3,time_after3,level_3))/3} words/sec.")