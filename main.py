from matplotlib import pyplot as plt
import time
import platform
import app


def running_system():
    """Checks for Linux or Win /// code runes only on Linux/Debian"""
    run_system = platform.system()
    return run_system
#imo not relevant


class CpuInfo():
    """Get cpu information from /proc/cpuinfo"""
    def __init__(self, select_info, only_value=None):
        self.select_info = select_info
        self.only_value = only_value

    def cpu_core(self):
        """creat cpu_info object: use select_info/commands to get index for /proc/cpuinfo; only_value False = returns full string , True = return only value; EXAMPLE: core = CpuInfo("core", True).cpu_core()  """
        cpu_info_file = open('/proc/cpuinfo')
        cpu_info_list = list(cpu_info_file)
        cpu_info_file.close()
        commands = {
            "model": 4,
            "mhz" : 7,
            "core": 12
        }
        if self.select_info in commands:
            info_index = commands.get(self.select_info)

            if self.only_value == True:
                return " ".join(((cpu_info_list[info_index]).split(":")[1]).split())
            else:
                return " ".join((cpu_info_list[info_index]).split())
        else:
            "unknown command"
#imo not relevant





def user_input_plot():
    """User Input for plotting: time period(user_in_time*60) x, for y coordinates intervals"""
    user_in_interval = app.interval_scale.get()
    user_in_time = app.time_scale.get()
    number_of_interval = user_in_time*60/user_in_interval+1
    return int(user_in_interval), int(user_in_time), int(number_of_interval)


def plot_time_x():
    """GENERAL x coordiantes label, from def user_input_plot """
    global user_in_interval
    global user_in_time
    global number_of_interval
    user_in_interval, user_in_time, number_of_interval = user_input_plot()

    plot_x = []
    x_coordinate_steps = range(0, number_of_interval*user_in_interval, user_in_interval)
    for x in x_coordinate_steps:
        plot_x.append(x)
    return plot_x


def plot_cpu_temp_y():
    """y coordinates / cpu temp"""
    plot_temp_y = []
    cpu_temp_counter = 0
    while cpu_temp_counter < number_of_interval :
        temp_file = open('/sys/class/thermal/thermal_zone0/temp')
        raw_cpu_temp = temp_file.read()
        temp_file.close()
        cpu_temp = int(raw_cpu_temp)/1000
        plot_temp_y.append(int(cpu_temp))
        cpu_temp_counter += 1
        if number_of_interval - cpu_temp_counter == 0:
            break
        else:
            time.sleep(user_in_interval)
    return plot_temp_y
