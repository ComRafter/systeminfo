import time
import platform



#linux or windows  // imo only Linux/Debian
def running_system():
    run_system = platform.system()
    return run_system


#CPU INFO //Linux
def cpu_info():
    cpu_info_file = open('/proc/cpuinfo')
    cpu_info_list = list(cpu_info_file)
    cpu_info_file.close()
    cpu_core = " ".join((cpu_info_list[12]).split())
    cpu_model = " ".join((cpu_info_list[4]).split())
    cpu_mhz = " ".join((cpu_info_list[7]).split())
    return cpu_core, cpu_model, cpu_mhz


#collect data for plotting cpu-temp //Linux
def collect_cpu_temp():
    user_in_interval = int(input("enter intervals in sec: ")) #tkinter slider for select
    user_in_time = int(input("enter timescale in min: "))    #tkinter slider for select
    time_count = user_in_time*60/user_in_interval

    cpu_temp_counter = 0
    while cpu_temp_counter < time_count :
        temp_file = open('/sys/class/thermal/thermal_zone0/temp')
        raw_cpu_temp = temp_file.read()
        temp_file.close()
        cpu_temp = round(float(raw_cpu_temp)/1000, 2)
        print(cpu_temp)
        cpu_temp_counter += 1
        if time_count - cpu_temp_counter == 0:
            break
        else:
            time.sleep(user_in_interval)

collect_cpu_temp()
