import os
import psutil
import threading
import dec
import show

@dec.print_file("cpu_info.json")
def cpu_inform():
    value=psutil.cpu_percent(interval=1)
    if isinstance(value,float): 
        loading="CPU[" + "|"*round(value/2)
        value_str=str(round(value,1)) +"%"
    inform = [loading, value_str]
    show.show_cpu_inform(inform)
    return ["CPU", value_str]

@dec.print_file("cpu_info.json")
def process_info():
    tasks=str(len(list(psutil.process_iter())))
    threads = str(threading.active_count())
    show.show_process_info([tasks, threads])
    return [tasks, threads]

@dec.print_file("cpu_info.json")
def load_average_info():
    value = list(map(lambda x: str(round(x,2)),psutil.getloadavg()))
    show.show_load_average_info(value)
    return value

@dec.print_file("cpu_info.json")
def uptime_info():
    value = round(float(open("/proc/uptime").read().split()[0]))
    day = str(value // 3600 // 24)
    hours = str(value // 3600 % 24)
    minutes = str(value // 60 % 60)
    seconds = str(value % 60)
    inform = "Uptime: "+ day + " days, " + hours + ":" + minutes + ":" + seconds
    show.show_uptime_info(inform)
    return inform


@dec.print_file("menory_info.json")
def virtual_memory_inform():
    value=psutil.virtual_memory()
    active="|"*round(value[5]/value[0]*50)
    free="|"*round(value[4]/value[0]*50)
    not_used=str(round((value[0] - value[1])/1024/1024/1024,1))
    total=str(round(value[0]/1024/1024/1024,1))
    stat_inf =not_used+"G/" + total + "G"
    show.show_virtual_memory_inform([active, free,stat_inf])
    return ["Memory: ",stat_inf]

@dec.print_file("menory_info.json")
def swap_virtual_memory_inform():
    value=psutil.swap_memory()
    active="|"*round(value[1]/value[0]*50)
    free="|"*round(value[2]/value[0]*50)
    used=str(round(value[1]/1024/1024/1024,1))
    total=str(round(value[0]/1024/1024/1024,1))
    stat_inf=used+"G/" + total + "G"
    show.show_swap_memory_inform([active, free,stat_inf])
    return ["Swap memory: ",stat_inf]

@dec.print_file("process_info.json")
def process_list_info():
    process_list=[['PID','User','VIRT','RES','CPU%','MEM%','Time','Command']]
    for p in psutil.process_iter():
        temp_list=[]
        temp_list.append(p.pid)
        temp_list.append(p.username())
        temp_list.append(round(p.memory_info()[1]/1024/1024,1))
        temp_list.append(round(p.memory_info()[0]/1024/1024,1))
        temp_list.append(round(p.cpu_percent(),1))
        temp_list.append(round(p.memory_percent(),1))
        value = p.cpu_times()[0]
        minut=int(value)//60
        second=round(value - minut*60,2)
        temp_list.append(format(str(minut)+":"+str(second)))
        names=p.cmdline()
        if len(names)>0:
            temp_list.append(" " + str(names[0]))
        else:
            temp_list.append("NA")
        process_list.append(temp_list)
    show.show_process_list_info(process_list)    
    return process_list