import os

def show_cpu_inform(inform):
    print('{:<60}'.format(inform[0]),'{:>6}'.format(inform[1]+"]"),sep="",end="   ")
    return

def show_process_info(inform):
    print('{:<25}'.format("Tasks:" + inform[0] + ",\033[32m"  + inform[1] + "\033[0m thr"))
    return

def show_load_average_info(inform):
     print('{:<25}'.format("Load average:\033[34m" + inform[0] +"\033[0m " + inform[1] + " " +inform[2])) 
     return

def show_uptime_info(inform):
    print('{:<20}'.format(inform))
    return

def show_virtual_memory_inform(inform):
    print('{:<70}'.format("Mem[\033[31m"+inform[0]+'\033[32m'+inform[1]+'\033[0m'),'{:>10}'.format(inform[2]+"]"),sep="",end="   ")
    return

def show_swap_memory_inform(inform):
    print('{:<70}'.format("Swp[\033[31m"+inform[0]+'\033[32m'+inform[1]+'\033[0m'),'{:>10}'.format(inform[2]+"]"),sep="", end = "   ")
    return

def show_process_list_info(inform):
    print('{:>6} {:^20} {:^10} {:^10} {:^7} {:^7} {:^10} {:^20}'.format(inform[0][0],inform[0][1],inform[0][2],inform[0][3],inform[0][4],inform[0][5], inform[0][6],inform[0][7]))
    for p in inform[1:len(inform)]:
                print('{:>6}'.format(p[0]),end="")
                print('{:^20}'.format(p[1]),end="")
                print('{:>10.1f}'.format(p[2]),end="")
                print('{:>10.1f}'.format(p[3]),end="")
                print('{:>8.1f}'.format(p[4]),end="")
                print('{:>8.1f}'.format(p[5]),end="")
                print('{:>10}'.format(p[6]),end="")
                print('{:^20}'.format(p[7]))
    return