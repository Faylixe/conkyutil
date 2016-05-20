
import sys

""" """

class ConkyWriter:
    """ """

    def __init__(self, stream=sys.stdout):
        """ """
        self.stream = stream

    def write(self, text):
        """ """
        self.stream.write(text)
        self.stream.flush()

    def writeCommand(command, parameters):
        """ """
        arguments = ''
        if type(parameters) is list:
            for parameter in parameters:
                if parameter != None:
                    arguments += parameter + ' '
                    # TODO : remove leading space.
        elif type(parameters) is tuple:

        else:
            arguments = parameters
        self.write('${%s %s}' % (command, arguments))

	def acpiacadapter(self, adapter=None):
		""" ACPI ac adapter state. On linux, the adapter option specifies the subfolder of /sys/class/power_supply containing the state information (tries "AC" and "ADP1" if there is no argument given). Non-linux systems ignore it. """
		self.writeCommand('acpiacadapter', adapter)

	def acpifan(self):
		""" ACPI fan state """
		self.writeCommand('acpifan')

	def acpitemp(self):
		""" ACPI temperature in C. """
		self.writeCommand('acpitemp')

	def addr(self, interface=None):
		""" IP address for an interface, or "No Address" if no address is assigned. """
		self.writeCommand('addr', interface)

	def addrs(self, interface=None):
		""" IP addresses for an interface (if one - works like addr). Linux only. """
		self.writeCommand('addrs', interface)

	def adt746xcpu(self):
		""" CPU temperature from therm_adt746x """
		self.writeCommand('adt746xcpu')

	def adt746xfan(self):
		""" Fan speed from therm_adt746x """
		self.writeCommand('adt746xfan')

	def alignc(self, num=None):
		""" Align text to centre """
		self.writeCommand('alignc', num)

	def alignr(self, num=None):
		""" Right-justify text, with space of N """
		self.writeCommand('alignr', num)

	def apcupsd(self, host):
		""" Sets up the connection to apcupsd daemon. Prints nothing, defaults to localhost:3551 """
		self.writeCommand('apcupsd', host)

	def apcupsd_cable(self):
		""" Prints the UPS connection type. """
		self.writeCommand('apcupsd_cable')

	def apcupsd_charge(self):
		""" Current battery capacity in percent. """
		self.writeCommand('apcupsd_charge')

	def apcupsd_lastxfer(self):
		""" Reason for last transfer from line to battery. """
		self.writeCommand('apcupsd_lastxfer')

	def apcupsd_linev(self):
		""" Nominal input voltage. """
		self.writeCommand('apcupsd_linev')

	def apcupsd_load(self):
		""" Current load in percent. """
		self.writeCommand('apcupsd_load')

	def apcupsd_loadbar(self):
		""" Bar showing current load. """
		self.writeCommand('apcupsd_loadbar')

	def apcupsd_loadgauge(self, size=None):
		""" Gauge that shows current load. Size parameter should be a tuple (height, width) """
		self.writeCommand('apcupsd_loadgauge', size)

	def apcupsd_loadgraph(self, size=None, gradientColor1=None, gradientColor2=None, scale=None, t=False, l=False):
		""" History graph of current load. """
        parameters = [size, gradientColor1, gradientColor2, scale]
        if t:
            parameters.append('-t')
        if l:
            parameters.append('-l')
		self.writeCommand('apcupsd_loadgraph', parameters)

	def apcupsd_model(self):
		""" Prints the model of the UPS. """
		self.writeCommand('apcupsd_model')

	def apcupsd_name(self):
		""" Prints the UPS user-defined name. """
		self.writeCommand('apcupsd_name')

	def apcupsd_status(self):
		""" Prints current status (on-line, on-battery). """
		self.writeCommand('apcupsd_status')

	def apcupsd_temp(self):
		""" Current internal temperature. """
		self.writeCommand('apcupsd_temp')

	def apcupsd_timeleft(self):
		""" Time left to run on battery. """
		self.writeCommand('apcupsd_timeleft')

	def apcupsd_upsmode(self):
		""" Prints the UPS mode (e.g. standalone). """
		self.writeCommand('apcupsd_upsmode')

	def apm_adapter(self):
		""" Display APM AC adapter status (FreeBSD only) """
		self.writeCommand('apm_adapter')

	def apm_battery_life(self):
		""" Display APM battery life in percent (FreeBSD only) """
		self.writeCommand('apm_battery_life')

	def apm_battery_time(self):
		""" Display remaining APM battery life in hh:mm:ss or "unknown" if AC adapterstatus is on-line or charging (FreeBSD only) """
		self.writeCommand('apm_battery_time')

	def audacious_bar(self, size=None):
		""" Progress bar """
		self.writeCommand('audacious_bar', size)

	def audacious_bitrate(self):
		""" Bitrate of current tune """
		self.writeCommand('audacious_bitrate')

	def audacious_channels(self):
		""" Number of audio channels of current tune """
		self.writeCommand('audacious_channels')

	def audacious_filename(self):
		""" Full path and filename of current tune """
		self.writeCommand('audacious_filename')

	def audacious_frequency(self):
		""" Sampling frequency of current tune """
		self.writeCommand('audacious_frequency')

	def audacious_length(self):
		""" Total length of current tune as MM:SS """
		self.writeCommand('audacious_length')

	def audacious_length_seconds(self):
		""" Total length of current tune in seconds """
		self.writeCommand('audacious_length_seconds')

	def audacious_main_volume(self):
		""" The current volume fetched from Audacious """
		self.writeCommand('audacious_main_volume')

	def audacious_playlist_length(self):
		""" Number of tunes in playlist """
		self.writeCommand('audacious_playlist_length')

	def audacious_playlist_position(self):
		""" Playlist position of current tune """
		self.writeCommand('audacious_playlist_position')

	def audacious_position(self):
		""" Position of current tune (MM:SS) """
		self.writeCommand('audacious_position')

	def audacious_position_seconds(self):
		""" Position of current tune in seconds """
		self.writeCommand('audacious_position_seconds')

	def audacious_status(self):
		""" Player status (Playing/Paused/Stopped/Not running) """
		self.writeCommand('audacious_status')

	def audacious_title(self, maxLength=None):
		""" Title of current tune with optional maximum length specifier """
		self.writeCommand('audacious_title', maxLength)

	def battery(self, num=None):
		""" Battery status and remaining percentage capacity of ACPI or APM battery. ACPI battery number can be given as argument (default is BAT0). """
		self.writeCommand('battery', num)

	def battery_bar(self):
		""" Battery percentage remaining of ACPI battery in a bar. ACPI battery number can be given as argument (default is BAT0). """
		self.writeCommand('battery_bar')

	def battery_percent(self, num=None):
		""" Battery percentage remaining for ACPI battery. ACPI battery number can be given as argument (default is BAT0). """
		self.writeCommand('battery_percent', num)

	def battery_short(self, num=None):
		""" Battery status and remaining percentage capacity of ACPI or APM battery. ACPI battery number can be given as argument (default is BAT0). This mode display a short status, which means that C is displayed instead of charging, D for discharging, F for full, N for not present, E for empty and U for unknown. """
		self.writeCommand('battery_short', num)

	def battery_time(self, num=None):
		""" Battery charge/discharge time remaining of ACPI battery. ACPI battery number can be given as argument (default is BAT0). """
		self.writeCommand('battery_time', num)

	def startBlink(self):
		""" Start blinking """
		self.write('${blink ')

    def endBlink(self):
        """ End blinking """
        self.write('}')

	def bmpx_album(self):
		""" Album in current BMPx track """
		self.writeCommand('bmpx_album')

	def bmpx_artist(self):
		""" Artist in current BMPx track """
		self.writeCommand('bmpx_artist')

	def bmpx_bitrate(self):
		""" Bitrate of the current BMPx track """
		self.writeCommand('bmpx_bitrate')

	def bmpx_title(self):
		""" Title of the current BMPx track """
		self.writeCommand('bmpx_title')

	def bmpx_track(self):
		""" Track number of the current BMPx track """
		self.writeCommand('bmpx_track')

	def bmpx_uri(self):
		""" URI of the current BMPx track """
		self.writeCommand('bmpx_uri')

	def buffers(self):
		""" Amount of memory buffered """
		self.writeCommand('buffers')

	def cached(self):
		""" Amount of memory cached """
		self.writeCommand('cached')

	def cmdlineToPID(self, search):
		""" PID of the first process that has string in it's commandline """
		self.writeCommand('cmdline_to_pid', search)

	def color(self, color=None):
		""" Change drawing color to 'color' which is a name of a color or a hexcode preceded with # (for example #0A1B2C ). If you use ncurses only the following colors are supported: red,green,yellow,blue,magenta,cyan,black,white. """
		self.writeCommand('color', color)

	def colorN(self, n):
		""" Change drawing color to colorN configuration option, where N is a digit between 0 and 9, inclusively. """
        # TODO : Check if between 0 and 9
		self.writeCommand('color%d' % n)

	def combine(self, var1, var2):
		""" Places the lines of var2 to the right of the lines of var1 separated by the chars that are put between var1 and var2. For example: ${combine ${head /proc/cpuinfo 2} - ${head /proc/meminfo 1}} gives as output "cpuinfo_line1 - meminfo_line1" on line 1 and "cpuinfo_line2 -" on line 2. $combine vars can also be nested to place more vars next to each other. """
		self.writeCommand('combine', [var1, var2])

	def conky_build_arch(self):
		""" CPU architecture Conky was built for """
		self.writeCommand('conky_build_arch')

	def conky_build_date(self):
		""" Date Conky was built """
		self.writeCommand('conky_build_date')

	def conky_version(self):
		""" Conky version """
		self.writeCommand('conky_version')

	def cpu(self, n=None):
		""" CPU usage in percents. For SMP machines, the CPU number can be provided as an argument. ${cpu cpu0} is the total usage, and ${cpu cpuX} (X >= 1) are individual CPUs. """
		self.writeCommand('cpu', n)

	def cpubar(self, n=None, size=None):
		""" Bar that shows CPU usage, height is bar's height in pixels. See $cpu for more info on SMP. """
		self.writeCommand('cpubar', [n, size])

	def cpugauge(self, n=None, size=None):
		""" Elliptical gauge that shows CPU usage, height and width are gauge's vertical and horizontal axis respectively. See $cpu for more info on SMP. """
		self.writeCommand('cpugauge', [n, size])

	def cpugraph(self, n=None, size=None, gradientColor1=None, gradientColor2=None, scale=None, t=False, l=False):
		""" CPU usage graph, with optional colours in hex, minus the #. See $cpu for more info on SMP. Uses a logarithmic scale (to see small numbers) when you use the -l switch. Takes the switch '-t' to use a temperature gradient, which makes the gradient values change depending on the amplitude of a particular graph value (try it and see). """
        parameters = [n, size, gradientColor1, gradientColor2, scale]
        if t:
            parameters.append('-t')
        if l:
            parameters.append('-l')
		self.writeCommand('cpugraph')

	def curl(self, url, interval=None):
		""" Download data from URI using Curl at the specified interval. The interval may be a floating point value greater than 0, otherwise defaults to 15 minutes. Most useful when used in conjunction with Lua and the Lua API. This object is threaded, and once a thread is created it can't be explicitly destroyed. One thread will run for each URI specified. You can use any protocol that Curl supports. """
		self.writeCommand('curl', [url, interval])

	def desktop(self):
		""" Number of the desktop on which conky is running or the message "Not running in X" if this is the case. """
		self.writeCommand('desktop')

	def desktop_name(self):
		""" Name of the desktop on which conky is running or the message "Not running in X" if this is the case. """
		self.writeCommand('desktop_name')

	def desktop_number(self):
		""" Number of desktops or the message "Not running in X" if this is the case. """
		self.writeCommand('desktop_number')

	def disk_protect(self, device):
		""" Disk protection status, if supported (needs kernel-patch). Prints either "frozen" or "free " (note the padding). """
		self.writeCommand('disk_protect', device)

	def diskio(self, device=None):
		""" Displays current disk IO. Device is optional, and takes the form of sda for /dev/sda. Individual partitions are allowed. """
		self.writeCommand('diskio', device)

	def diskio_read(self, device=None):
		""" Displays current disk IO for reads. Device as in diskio. """
		self.writeCommand('diskio_read', device)

	def diskio_write(self, device=None):
		""" Displays current disk IO for writes. Device as in diskio. """
		self.writeCommand('diskio_write', device)

	def diskiograph(self, device=None, size=None, gradientColor1=None, gradientColor2=None, scale=None, t=False, l=False):
		""" Disk IO graph, colours defined in hex, minus the #. If scale is non-zero, it becomes the scale for the graph. Uses a logarithmic scale (to see small numbers) when you use -l switch. Takes the switch '-t' to use a temperature gradient, which makes the gradient values change depending on the amplitude of a particular graph value (try it and see). """
        parameters = [device, size, gradientColor1, gradientColor2, scale]
        if t:
            parameters.append('-t')
        if l:
            parameters.append('-l')
		self.writeCommand('diskiograph', parameters)

	def diskiograph_read(self, device=None, size=None, gradientColor1=None, gradientColor2=None, scale=None, t=False, l=False):
		""" Disk IO graph for reads, colours defined in hex, minus the #. If scale is non-zero, it becomes the scale for the graph. Device as in diskio. Uses a logarithmic scale (to see small numbers) when you use -l switch. Takes the switch '-t' to use a temperature gradient, which makes the gradient values change depending on the amplitude of a particular graph value (try it and see). """
        parameters = [device, size, gradientColor1, gradientColor2, scale]
        if t:
            parameters.append('-t')
        if l:
            parameters.append('-l')
		self.writeCommand('diskiograph_read')

	def diskiograph_write(self, device=None, size=None, gradientColor1=None, gradientColor2=None, scale=None, t=False, l=False):
		""" Disk IO graph for writes, colours defined in hex, minus the #. If scale is non-zero, it becomes the scale for the graph. Device as in diskio. Uses a logarithmic scale (to see small numbers) when you use -l switch. Takes the switch '-t' to use a temperature gradient, which makes the gradient values change depending on the amplitude of a particular graph value (try it and see). """
        parameters = [device, size, gradientColor1, gradientColor2, scale]
        if t:
            parameters.append('-t')
        if l:
            parameters.append('-l')
		self.writeCommand('diskiograph_write')

	def downspeed(self, net=None):
		""" Download speed in suitable IEC units """
		self.writeCommand('downspeed', net)

	def downspeedf(self, net=None):
		""" Download speed in KiB with one decimal """
		self.writeCommand('downspeedf', net)

	def downspeedgraph(self, netdev=None, size=None, gradientColor1=None, gradientColor2=None, scale=None, t=False, l=False):
		""" Download speed graph, colours defined in hex, minus the #. If scale is non-zero, it becomes the scale for the graph. Uses a logarithmic scale (to see small numbers) when you use -l switch. Takes the switch '-t' to use a temperature gradient, which makes the gradient values change depending on the amplitude of a particular graph value (try it and see). """
        parameters = [netdev, size, gradientColor1, gradientColor2, scale]
        if t:
            parameters.append('-t')
        if l:
            parameters.append('-l')
		self.writeCommand('downspeedgraph', parameters)

	def draft_mails(self, maildir=None):
		""" Number of mails marked as draft in the specified mailbox or mail spool if not. Only maildir type mailboxes are supported, mbox type will return -1. """
		self.writeCommand('draft_mails', maildir)

	def elseCondition(self):
		""" Text to show if any of the above are not true """
		self.writeCommand('else')

	def endif(self):
		""" Ends an $if block. """
		self.writeCommand('endif')

	def entropy_avail(self):
		""" Current entropy available for crypto freaks """
		self.writeCommand('entropy_avail')

	def entropy_bar(self, size=None):
		""" Normalized bar of available entropy for crypto freaks """
		self.writeCommand('entropy_bar', size)

	def entropy_perc(self):
		""" Percentage of entropy available in comparison to the poolsize """
		self.writeCommand('entropy_perc')

	def entropy_poolsize(self):
		""" Total size of system entropy pool for crypto freaks """
		self.writeCommand('entropy_poolsize')

	def eval(self, string):
		""" Evaluates given string according to the rules of TEXT interpretation, i.e. parsing any contained text object specifications into their output, any occuring '$$' into a single '$' and so on. The output is then being parsed again. """
		self.writeCommand('eval', string)

	def eve(self, api_userid, api_key, character_id):
		""" Fetches your currently training skill from the Eve Online API servers (http://www.eve-online.com/) and displays the skill along with the remaining training time. """
		self.writeCommand('eve', [api_userid, api_key, character_id])

	def execCommand(self, command):
		""" Executes a shell command and displays the output in conky. warning: this takes a lot more resources than other variables. I'd recommend coding wanted behaviour in C and posting a patch. """
		self.writeCommand('exec', command)

	def execbar(self, command):
		""" Same as exec, except if the first value return is a value between 0-100, it will use that number for a bar. The size for bars can be controlled via the default_bar_size config setting. """
		self.writeCommand('execbar', command)

	def execgauge(self, command):
		""" Same as exec, except if the first value returned is a value between 0-100, it will use that number for a gauge. The size for gauges can be controlled via the default_gauge_size config setting. """
		self.writeCommand('execgauge', command)

	def execgraph(self, command, t=False, l=False):
		""" Same as execbar, but graphs values. Uses a logaritmic scale when the log option (-l switch) is given (to see small numbers). Values still have to be between 0 and 100. The size for graphs can be controlled via the default_graph_size config setting. Takes the switch '-t' to use a temperature gradient, which makes the gradient values change depending on the amplitude of a particular graph value (try it and see). If -t or -l is your first argument, you may need to preceed it by a space (' '). """
        parameters = []
        if t:
            parameters.append('-t')
        if l:
            parameters.append('-l')
        parameters.append(command)
		self.writeCommand('execgraph', parameters)

	def execi(self, interval, command):
		""" Same as exec but with specific interval. Interval can't be less than update_interval in configuration. See also $texeci """
		self.writeCommand('execi', [interval, command])

	def execibar(self, interval, command):
		""" Same as execbar, except with an interval """
		self.writeCommand('execibar', [interval, command])

	def execigauge(self, interval, command):
		""" Same as execgauge, but takes an interval arg and gauges values. """
		self.writeCommand('execigauge', [interval, command])

	def execigraph(self, interval, command, t=False, l=False):
		""" Same as execgraph, but takes an interval arg and graphs values. If -t or -l is your first argument, you may need to preceed it by a space (' '). """
        parameters = [interval]
        if t:
            parameters.append('-t')
        if l:
            parameters.append('-l')
        parameters.append(command)
		self.writeCommand('execigraph', parameters)

	def execp(self, command):
		""" Executes a shell command and displays the output in conky. warning: this takes a lot more resources than other variables. I'd recommend coding wanted behaviour in C and posting a patch. This differs from $exec in that it parses the output of the command, so you can insert things like ${color red}hi!${color} in your script and have it correctly parsed by Conky. Caveats: Conky parses and evaluates the output of $execp every time Conky loops, and then destroys all the objects. If you try to use anything like $execi within an $execp statement, it will functionally run at the same interval that the $execp statement runs, as it is created and destroyed at every interval. """
		self.writeCommand('execp', command)

	def execpi(self, interval, command):
		""" Same as execp but with specific interval. Interval can't be less than update_interval in configuration. Note that the output from the $execpi command is still parsed and evaluated at every interval. """
		self.writeCommand('execpi', [interval, command])

	def flagged_mails(self, maildir=None):
		""" Number of mails marked as flagged in the specified mailbox or mail spool if not. Only maildir type mailboxes are supported, mbox type will return -1. """
		self.writeCommand('flagged_mails', maildir)

	def font(self, font):
		""" Specify a different font. This new font will apply to the current line and everything following. You can use a $font with no arguments to change back to the default font (much like with $color) """
		self.writeCommand('font')

	def format_time(self, seconds, format):
		""" Format time given in seconds. This var only works when the times_in_seconds configuration setting is on. Format is a string that should start and end with a "-char. The "-chars are not part of the output, \w,\d,\h,\m,\s,\(,\) and \\ are replaced by weeks,days,hours,minutes,seconds,(,) and \. If you leave out a unit, it's value will be expressed in the highest unite lower then the one left out. Text between ()-chars will not be visible if a replaced unit in this text is 0. If seconds is a decimal number then you can see the numbers behind the point by using \S followed by a number that specifies the amount of digits behind the point that you want to see (maximum 9). You can also place a 'x' behind \S so you have all digits behind the point and no trailing zero's. (also maximum 9) """
		self.writeCommand('format_time', [seconds, format])

	def forwarded_mails(self, maildir=None):
		""" Number of mails marked as forwarded in the specified mailbox or mail spool if not. Only maildir type mailboxes are supported, mbox type will return -1. """
		self.writeCommand('forwarded_mails', maildir)

	def freq(self, n=None):
		""" Returns CPU #n's frequency in MHz. CPUs are counted from 1. If omitted, the parameter defaults to 1. """
		self.writeCommand('freq', n)

	def freq_g(self, n=None):
		""" Returns CPU #n's frequency in GHz. CPUs are counted from 1. If omitted, the parameter defaults to 1. """
		self.writeCommand('freq_g', n)

	def fs_bar(self, fs, size=None):
		""" Bar that shows how much space is used on a file system. height is the height in pixels. fs is any file on that file system. """
		self.writeCommand('fs_bar', [fs, size])

	def fs_bar_free(self, fs, size=None):
		""" Bar that shows how much space is free on a file system. height is the height in pixels. fs is any file on that file system. """
		self.writeCommand('fs_bar_free', [fs, size])

	def fs_free(self, fs=None):
		""" Free space on a file system available for users. """
		self.writeCommand('fs_free', fs)

	def fs_free_perc(self, fs=None):
		""" Free percentage of space on a file system available for users. """
		self.writeCommand('fs_free_perc', fs)

	def fs_size(self, fs=None):
		""" File system size. """
		self.writeCommand('fs_size', fs)

	def fs_type(self, fs=None):
		""" File system type. """
		self.writeCommand('fs_type', fs)

	def fs_used(self, fs=None):
		""" File system used space. """
		self.writeCommand('fs_used', fs)

	def fs_used_perc(self, fs=None):
		""" Percent of file system used space. """
		self.writeCommand('fs_used_perc', fs)

	def goto(self, x):
		""" The next element will be printed at position 'x'. """
		self.writeCommand('goto', x)

	def gw_iface(self):
		""" Displays the default route's interface or "multiple"/"none" accordingly. """
		self.writeCommand('gw_iface')

	def gw_ip(self):
		""" Displays the default gateway's IP or "multiple"/"none" accordingly. """
		self.writeCommand('gw_ip')

	def hddtemp(self, dev=None):
		""" Displays temperature of a selected hard disk drive as reported by the hddtemp daemon. Use hddtemp_host and hddtemp_port to specify a host and port for all hddtemp objects. If no dev parameter is given, the first disk returned by the hddtemp daemon is used. """
		self.writeCommand('hddtemp', dev)

	def head(self, logfile, lines, next_check=None):
		""" Displays first N lines of supplied text file. The file is checked every 'next_check' update. If next_check is not supplied, Conky defaults to 2. Max of 30 lines can be displayed, or until the text buffer is filled. """
		self.writeCommand('head', [logfile, lines, next_check])

	def hr(self, height=None):
		""" Horizontal line, height is the height in pixels """
		self.writeCommand('hr', height)

	def hwmon(self, type, n, device=None):
		""" Hwmon sensor from sysfs (Linux 2.6). Parameter dev may be omitted if you have only one hwmon device. Parameter type is either 'in' or 'vol' meaning voltage; 'fan' meaning fan; 'temp' meaning temperature. Parameter n is number of the sensor. See /sys/class/hwmon/ on your local computer. The optional arguments 'factor' and 'offset' allow precalculation of the raw input, which is being modified as follows: 'input = input * factor + offset'. Note that they have to be given as decimal values (i.e. contain at least one decimal place). """
		self.writeCommand('hwmon')

	def i2c(self):
		""" I2C sensor from sysfs (Linux 2.6). Parameter dev may be omitted if you have only one I2C device. Parameter type is either 'in' or 'vol' meaning voltage; 'fan' meaning fan; 'temp' meaning temperature. Parameter n is number of the sensor. See /sys/bus/i2c/devices/ on your local computer. The optional arguments 'factor' and 'offset' allow precalculation of the raw input, which is being modified as follows: 'input = input * factor + offset'. Note that they have to be given as decimal values (i.e. contain at least one decimal place). """
		self.writeCommand('i2c')

	def i8k_ac_status(self):
		""" If running the i8k kernel driver for Inspiron laptops, displays whether ac power is on, as listed in /proc/i8k (translated to human-readable). Beware that this is by default not enabled by i8k itself. """
		self.writeCommand('i8k_ac_status')

	def i8k_bios(self):
		""" If running the i8k kernel driver for Inspiron laptops, displays the bios version as listed in /proc/i8k. """
		self.writeCommand('i8k_bios')

	def i8k_buttons_status(self):
		""" If running the i8k kernel driver for Inspiron laptops, displays the volume buttons status as listed in /proc/i8k. """
		self.writeCommand('i8k_buttons_status')

	def i8k_cpu_temp(self):
		""" If running the i8k kernel driver for Inspiron laptops, displays the cpu temperature in Celsius, as reported by /proc/i8k. """
		self.writeCommand('i8k_cpu_temp')

	def i8k_left_fan_rpm(self):
		""" If running the i8k kernel driver for Inspiron laptops, displays the left fan's rate of rotation, in revolutions per minute as listed in /proc/i8k. Beware, some laptops i8k reports these fans in reverse order. """
		self.writeCommand('i8k_left_fan_rpm')

	def i8k_left_fan_status(self):
		""" If running the i8k kernel driver for Inspiron laptops, displays the left fan status as listed in /proc/i8k (translated to human-readable). Beware, some laptops i8k reports these fans in reverse order. """
		self.writeCommand('i8k_left_fan_status')

	def i8k_right_fan_rpm(self):
		""" If running the i8k kernel driver for Inspiron laptops, displays the right fan's rate of rotation, in revolutions per minute as listed in /proc/i8k. Beware, some laptops i8k reports these fans in reverse order. """
		self.writeCommand('i8k_right_fan_rpm')

	def i8k_right_fan_status(self):
		""" If running the i8k kernel driver for Inspiron laptops, displays the right fan status as listed in /proc/i8k (translated to human-readable). Beware, some laptops i8k reports these fans in reverse order. """
		self.writeCommand('i8k_right_fan_status')

	def i8k_serial(self):
		""" If running the i8k kernel driver for Inspiron laptops, displays your laptop serial number as listed in /proc/i8k. """
		self.writeCommand('i8k_serial')

	def i8k_version(self):
		""" If running the i8k kernel driver for Inspiron laptops, displays the version formatting of /proc/i8k. """
		self.writeCommand('i8k_version')

	def ibm_brightness(self):
		""" If running the IBM ACPI, displays the brigtness of the laptops's LCD (0-7). """
		self.writeCommand('ibm_brightness')

	def ibm_fan(self):
		""" If running the IBM ACPI, displays the fan speed. """
		self.writeCommand('ibm_fan')

	def ibm_temps(self, n):
		""" If running the IBM ACPI, displays the temperatures from the IBM temperature sensors (N=0..7) Sensor 0 is on the CPU, 3 is on the GPU. """
		self.writeCommand('ibm_temps', n)

	def ibm_volume(self):
		""" If running the IBM ACPI, displays the "master" volume, controlled by the volume keys (0-14). """
		self.writeCommand('ibm_volume')

	def iconv_start(self, codeset_from, codeset_to):
		""" Convert text from one codeset to another using GNU iconv. Needs to be stopped with iconv_stop. """
		self.writeCommand('iconv_start', [codeset_from, codeset_to])

	def iconv_stop(self):
		""" Stop iconv codeset conversion. """
		self.writeCommand('iconv_stop')

	def if_empty(self, var):
		""" if conky variable VAR is empty, display everything between $if_empty and the matching $endif """
		self.writeCommand('if_empty', var)

	def if_existing(self, file, search=None):
		""" if FILE exists, display everything between if_existing and the matching $endif. The optional second parameter checks for FILE containing the specified string and prints everything between $if_existing and the matching $endif. """
		self.writeCommand('if_existing', [file, search])

	def if_gw(self):
		""" if there is at least one default gateway, display everything between $if_gw and the matching $endif """
		self.writeCommand('if_gw')

	def if_match(self, expression):
		""" Evaluates the given boolean expression, printing everything between $if_match and the matching $endif depending on whether the evaluation returns true or not. Valid expressions consist of a left side, an operator and a right side. Left and right sides are being parsed for contained text objects before evaluation. Recognised left and right side types are: double - Argument consists of only digits and a single dot.long - Argument consists of only digits.string - Argument is enclosed in quotation marks (")Valid operands are: '>', '<', '>=', '<=', '==', '!='. """
		self.writeCommand('if_match', expression)

	def if_mixer_mute(self, mixer=None):
		""" If mixer exists, display everything between $if_mixer_mute and the matching $endif. If no mixer is specified, "Vol" is used. """
		self.writeCommand('if_mixer_mute', mixer)

	def if_mounted(self, mountpoint=None):
		""" if MOUNTPOINT is mounted, display everything between $if_mounted and the matching $endif """
		self.writeCommand('if_mounted', mountpoint)

	def if_mpd_playing(self):
		""" if mpd is playing or paused, display everything between $if_mpd_playing and the matching $endif """
		self.writeCommand('if_mpd_playing')

	def if_running(self, process=None):
		""" if PROCESS is running, display everything $if_running and the matching $endif. This uses the ``pidof'' command, so the -x switch is also supported. """
		self.writeCommand('if_running', process)

	def if_smapi_bat_installed(self, index=None):
		""" when using smapi, if the battery with index INDEX is installed, display everything between $if_smapi_bat_installed and the matching $endif """
		self.writeCommand('if_smapi_bat_installed', index)

	def if_up(self, interface=None):
		""" if INTERFACE exists and is up, display everything between $if_up and the matching $endif """
		self.writeCommand('if_up', interface)

	def if_updatenr(self, updatenr=None):
		""" If it's the UPDATENR-th time that conky updates, display everything between $if_updatenr and the matching $endif. The counter resets when the highest UPDATENR is reached. Example : "{$if_updatenr 1}foo$endif{$if_updatenr 2}bar$endif{$if_updatenr 4}$endif" shows foo 25% of the time followed by bar 25% of the time followed by nothing the other half of the time. """
		self.writeCommand('if_updatenr', updatenr)

	def if_xmms2_connected(self):
		""" Display everything between $if_xmms2_connected and the matching $endif if xmms2 is running. """
		self.writeCommand('if_xmms2_connected')

	def image(self):
		""" Renders an image from the path specified using Imlib2. Takes 4 optional arguments: a position, a size, a no-cache switch, and a cache flush interval. Changing the x,y position will move the position of the image, and changing the WxH will scale the image. If you specify the no-cache flag (-n), the image will not be cached. Alternately, you can specify the -f int switch to specify a cache flust interval for a particular image. Example: ${image /home/brenden/cheeseburger.jpg -p 20,20 -s 200x200} will render 'cheeseburger.jpg' at (20,20) scaled to 200x200 pixels. Conky does not make any attempt to adjust the position (or any other formatting) of images, they are just rendered as per the arguments passed. The only reason $image is part of the TEXT section, is to allow for runtime modifications, through $execp $lua_parse, or some other method. """
		self.writeCommand('image')

	def imap_messages(self, args=None):
		""" Displays the number of messages in your global IMAP inbox by default. You can define individual IMAP inboxes separately by passing arguments to this object. Arguments are: "host user pass [-i interval (in seconds)] [-f 'folder'] [-p port] [-e 'command'] [-r retries]". Default port is 143, default folder is 'INBOX', default interval is 5 minutes, and default number of retries before giving up is 5. If the password is supplied as '*', you will be prompted to enter the password when Conky starts. """
		self.writeCommand('imap_messages', args)

	def imap_unseen(self, args=None):
		""" Displays the number of unseen messages in your global IMAP inbox by default. You can define individual IMAP inboxes separately by passing arguments to this object. Arguments are: "host user pass [-i interval (in seconds)] [-f 'folder'] [-p port] [-e 'command'] [-r retries]". Default port is 143, default folder is 'INBOX', default interval is 5 minutes, and default number of retries before giving up is 5. If the password is supplied as '*', you will be prompted to enter the password when Conky starts. """
		self.writeCommand('imap_unseen', args)

	def include(self, path):
		""" Loads the configfile at path, places the configsettings behind the configsettings in the orginal config and places the vars where the includevar stood. """
		self.writeCommand('include', path)

	def ioscheduler(self, disk):
		""" Prints the current ioscheduler used for the given disk name (i.e. e.g. "hda" or "sdb") """
		self.writeCommand('ioscheduler', disk)

	def kernel(self):
		""" Kernel version """
		self.writeCommand('kernel')

	def laptop_mode(self):
		""" The value of /proc/sys/vm/laptop_mode """
		self.writeCommand('laptop_mode')

	def lines(self, textfile):
		""" Displays the number of lines in the given file """
		self.writeCommand('lines', textfile)

	def loadavg(self, n=None):
		""" System load average, 1 is for past 1 minute, 2 for past 5 minutes and 3 for past 15 minutes. Without argument, prints all three values separated by whitespace. """
        # TODO : Check if n = 1|2|3
		self.writeCommand('loadavg', n)

	def loadgraph(self, size=None, gradientColor1=None, gradientColor2=None, scale=None, t=False, l=False):
		""" Load1 average graph, similar to xload, with optional colours in hex, minus the #. Uses a logarithmic scale (to see small numbers) when you use the -l switch. Takes the switch '-t' to use a temperature gradient, which makes the gradient values change depending on the amplitude of a particular graph value (try it and see). """
        parameters = [size, gradientColor1, gradientColor2, scale]
        if t:
            parameters.append('-t')
        if l:
            parameters.append('-l')
		self.writeCommand('loadgraph', parameters)

	def lua(self, function_name, args=None):
		""" Executes a Lua function with given parameters, then prints the returned string. See also 'lua_load' on how to load scripts. Conky puts 'conky_' in front of function_name to prevent accidental calls to the wrong function unless you put you place 'conky_' in front of it yourself. """
		self.writeCommand('lua', [function_name, args])

	def lua_bar(self, function_name, size=None, args=None):
		""" Executes a Lua function with given parameters and draws a bar. Expects result value to be an integer between 0 and 100. See also 'lua_load' on how to load scripts. Conky puts 'conky_' in front of function_name to prevent accidental calls to the wrong function unless you put you place 'conky_' in front of it yourself. """
		self.writeCommand('lua_bar', [size, function_name, args])

	def lua_gauge(self, function_name, size=None, args=None):
		""" Executes a Lua function with given parameters and draws a gauge. Expects result value to be an integer between 0 and 100. See also 'lua_load' on how to load scripts. Conky puts 'conky_' in front of function_name to prevent accidental calls to the wrong function unless you put you place 'conky_' in front of it yourself. """
		self.writeCommand('lua_gauge', [size, function_name, args])

	def lua_graph(self, function_name, size=None, gradientColor1=None, gradientColor2=None, scale=None, t=False, l=False):
		""" Executes a Lua function with and draws a graph. Expects result value to be any number, and by default will scale to show the full range. See also 'lua_load' on how to load scripts. Takes the switch '-t' to use a temperature gradient, which makes the gradient values change depending on the amplitude of a particular graph value (try it and see). Conky puts 'conky_' in front of function_name to prevent accidental calls to the wrong function unless you put you place 'conky_' in front of it yourself. """
        parameters = [function_name, size, gradientColor1, gradientColor2, scale]
        if t:
            parameters.append('-t')
        if l:
            parameters.append('-l')
		self.writeCommand('lua_graph', parameters)

	def lua_parse(self, function_name, args=None):
		""" Executes a Lua function with given parameters as per $lua, then parses and prints the result value as per the syntax for Conky's TEXT section. See also 'lua_load' on how to load scripts. Conky puts 'conky_' in front of function_name to prevent accidental calls to the wrong function unless you put you place 'conky_' in front of it yourself. """
		self.writeCommand('lua_parse', [function_name, args])

	def machine(self):
		""" Machine, i686 for example """
		self.writeCommand('machine')

	def mails(self, mailbox=None):
		""" Mail count in the specified mailbox or your mail spool if not. Both mbox and maildir type mailboxes are supported. You can use a program like fetchmail to get mails from some server using your favourite protocol. See also new_mails. """
		self.writeCommand('mails', mailbox)

	def mboxscan(self, mbox, n=None, fw=None, sw=None):
		""" Print a summary of recent messages in an mbox format mailbox. mbox parameter is the filename of the mailbox (can be encapsulated using '"', ie. ${mboxscan -n 10 "/home/brenden/some box"} """
        parameters = []
        if n != None:
            parameters.append('-n')
            parameters.append(n)
        if fw != None:
            parameters.append('-fw')
            parameters.append(fw)
        if sw != None:
            parameters.append('-sw')
            parameters.append(sw)
        parameters.append(mbox)
		self.writeCommand('mboxscan', parameters)

	def mem(self):
		""" Amount of memory in use """
		self.writeCommand('mem')

	def membar(self, size=None):
		""" Bar that shows amount of memory in use """
		self.writeCommand('membar', size)

	def memeasyfree(self):
		""" Amount of free memory including the memory that is very easily freed (buffers/cache) """
		self.writeCommand('memeasyfree')

	def memfree(self):
		""" Amount of free memory """
		self.writeCommand('memfree')

	def memgauge(self, size=None):
		""" Gauge that shows amount of memory in use (see cpugauge) """
		self.writeCommand('memgauge', size)

	def memgraph(self, size=None, gradientColor1=None, gradientColor2=None, scale=None, t=False, l=False):
		""" Memory usage graph. Uses a logarithmic scale (to see small numbers) when you use the -l switch. Takes the switch '-t' to use a temperature gradient, which makes the gradient values change depending on the amplitude of a particular graph value (try it and see). """
        parameters = [size, gradientColor1, gradientColor2, scale]
        if t:
            parameters.append('-t')
        if l:
            parameters.append('-l')
		self.writeCommand('memgraph', parameters)

	def memmax(self):
		""" Total amount of memory """
		self.writeCommand('memmax')

	def memperc(self):
		""" Percentage of memory in use """
		self.writeCommand('memperc')

	def mixer(self, device=None):
		""" Prints the mixer value as reported by the OS. On Linux, this variable uses the OSS emulation, so you need the proper kernel module loaded. Default mixer is "Vol", but you can specify one of the available OSS controls: "Vol", "Bass", "Trebl", "Synth", "Pcm", "Spkr", "Line", "Mic", "CD", "Mix", "Pcm2 ", "Rec", "IGain", "OGain", "Line1", "Line2", "Line3", "Digital1", "Digital2", "Digital3", "PhoneIn", "PhoneOut", "Video", "Radio" and "Monitor". """
		self.writeCommand('mixer', device)

	def mixerbar(self, device=None):
		""" Displays mixer value in a bar as reported by the OS. See docs for $mixer for details on arguments. """
		self.writeCommand('mixerbar', device)

	def mixerl(self, device=None:
		""" Prints the left channel mixer value as reported by the OS. See docs for $mixer for details on arguments. """
		self.writeCommand('mixerl', device)

	def mixerlbar(self, device=None):
		""" Displays the left channel mixer value in a bar as reported by the OS. See docs for $mixer for details on arguments. """
		self.writeCommand('mixerlbar', device)

	def mixerr(self, device=None):
		""" Prints the right channel mixer value as reported by the OS. See docs for $mixer for details on arguments. """
		self.writeCommand('mixerr', device)

	def mixerrbar(self, device=None):
		""" Displays the right channel mixer value in a bar as reported by the OS. See docs for $mixer for details on arguments. """
		self.writeCommand('mixerrbar', device)

	def moc_album(self):
		""" Album of the current MOC song """
		self.writeCommand('moc_album')

	def moc_artist(self):
		""" Artist of the current MOC song """
		self.writeCommand('moc_artist')

	def moc_bitrate(self):
		""" Bitrate in the current MOC song """
		self.writeCommand('moc_bitrate')

	def moc_curtime(self):
		""" Current time of the current MOC song """
		self.writeCommand('moc_curtime')

	def moc_file(self):
		""" File name of the current MOC song """
		self.writeCommand('moc_file')

	def moc_rate(self):
		""" Rate of the current MOC song """
		self.writeCommand('moc_rate')

	def moc_song(self):
		""" The current song name being played in MOC. """
		self.writeCommand('moc_song')

	def moc_state(self):
		""" Current state of MOC; playing, stopped etc. """
		self.writeCommand('moc_state')

	def moc_timeleft(self):
		""" Time left in the current MOC song """
		self.writeCommand('moc_timeleft')

	def moc_title(self):
		""" Title of the current MOC song """
		self.writeCommand('moc_title')

	def moc_totaltime(self):
		""" Total length of the current MOC song """
		self.writeCommand('moc_totaltime')

	def monitor(self):
		""" Number of the monitor on which conky is running or the message "Not running in X" if this is the case. """
		self.writeCommand('monitor')

	def monitor_number(self):
		""" Number of monitors or the message "Not running in X" if this is the case. """
		self.writeCommand('monitor_number')

	def mpd_album(self):
		""" Album in current MPD song """
		self.writeCommand('mpd_album')

	def mpd_artist(self):
		""" Artist in current MPD song must be enabled at compile """
		self.writeCommand('mpd_artist')

	def mpd_bar(self, size=None):
		""" Bar of mpd's progress """
		self.writeCommand('mpd_bar', size)

	def mpd_bitrate(self):
		""" Bitrate of current song """
		self.writeCommand('mpd_bitrate')

	def mpd_date(self):
		""" Date of current song """
		self.writeCommand('mpd_date')

	def mpd_elapsed(self):
		""" Song's elapsed time """
		self.writeCommand('mpd_elapsed')

	def mpd_file(self):
		""" Prints the file name of the current MPD song """
		self.writeCommand('mpd_file')

	def mpd_length(self):
		""" Song's length """
		self.writeCommand('mpd_length')

	def mpd_name(self):
		""" Prints the MPD name field """
		self.writeCommand('mpd_name')

	def mpd_percent(self):
		""" Percent of song's progress """
		self.writeCommand('mpd_percent')

	def mpd_random(self):
		""" Random status (On/Off) """
		self.writeCommand('mpd_random')

	def mpd_repeat(self):
		""" Repeat status (On/Off) """
		self.writeCommand('mpd_repeat')

	def mpd_smart(self, maxLength=None):
		""" Prints the song name in either the form "artist - title" or file name, depending on whats available """
		self.writeCommand('mpd_smart', maxLength)

	def mpd_status(self):
		""" Playing, stopped, et cetera. """
		self.writeCommand('mpd_status')

	def mpd_title(self, maxLength=None):
		""" Title of current MPD song """
		self.writeCommand('mpd_title', maxLength)

	def mpd_track(self):
		""" Prints the MPD track field """
		self.writeCommand('mpd_track')

	def mpd_vol(self):
		""" MPD's volume """
		self.writeCommand('mpd_vol')

	def nameserver(self, index=None):
		""" Print a nameserver from /etc/resolv.conf. Index starts at and defaults to 0. """
		self.writeCommand('nameserver', index)

	def new_mails(self, mailbox=None):
		""" Unread mail count in the specified mailbox or mail spool if not. Both mbox and maildir type mailboxes are supported. """
		self.writeCommand('new_mails', mailbox)

	def nodename(self):
		""" Hostname """
		self.writeCommand('nodename')

	def nodename_short(self):
		""" Short hostname (same as 'hostname -s' shell command). """
		self.writeCommand('nodename_short')

	def nvidia(self, threshold):
		""" Nvidia graficcard support for the XNVCtrl library. Each option can be shortened to the least significant part. Temperatures are printed as float, all other values as integer. threshold - The thresholdtemperature at which the gpu slows down temp - Gives the gpu current temperature ambient - Gives current air temperature near GPU case gpufreq - Gives the current gpu frequency memfreq - Gives the current mem frequency imagequality - Which imagequality should be chosen by OpenGL applications """
		self.writeCommand('nvidia', threshold)

	def offset(self, pixels=None):
		""" Move text over by N pixels. See also $voffset. """
		self.writeCommand('offset', pixels)

	def outlinecolor(self, color=None):
		""" Change outline color """
		self.writeCommand('outlinecolor', color)

	def pb_battery(self, item):
		""" If running on Apple powerbook/ibook, display information on battery status. The item parameter specifies, what information to display. Exactly one item must be specified. Valid items are: status - Display if battery is fully charged, charging, discharging or absent (running on AC) percent - Display charge of battery in percent, if charging or discharging. Nothing will be displayed, if battery is fully charged or absent. time - Display the time remaining until the battery will be fully charged or discharged at current rate. Nothing is displayed, if battery is absent or if it's present but fully charged and not discharging. """
		self.writeCommand('pb_battery', item)

	def pid_chroot(self, pid):
		""" Directory used as rootdirectory by the process (this will be "/" unless the process did a chroot syscall) """
		self.writeCommand('pid_chroot', pid)

	def pid_cmdline(self, pid):
		""" Command line this process was invoked with """
		self.writeCommand('pid_cmdline', pid)

	def pid_cwd(self, pid):
		""" Current working directory of the process """
		self.writeCommand('pid_cwd', pid)

	def pid_environ(self, pid, varname):
		""" Contents of a environment-var of the process """
		self.writeCommand('pid_environ', [pid, varname])

	def pid_environ_list(self, pid):
		""" List of environment-vars that the process can see """
		self.writeCommand('pid_environ_list', pid)

	def pid_exe(self, pid):
		""" Path to executed command that started the process """
		self.writeCommand('pid_exe', pid)

	def pid_nice(self, pid):
		""" The nice value of the process """
		self.writeCommand('pid_nice', pid)

	def pid_openfiles(self, pid):
		""" List of files that the process has open """
		self.writeCommand('pid_openfiles', pid)

	def pid_parent(self, pid):
		""" The pid of the parent of the process """
		self.writeCommand('pid_parent', pid)

	def pid_priority(self, pid):
		""" The priority of the process (see 'priority' in "man 5 proc") """
		self.writeCommand('pid_priority', pid)

	def pid_read(self, pid):
		""" Total number of bytes read by the process """
		self.writeCommand('pid_read', pid)

	def pid_state(self, pid):
		""" State of the process """
		self.writeCommand('pid_state', pid)

	def pid_state_short(self, pid):
		""" One of the chars in "RSDZTW" representing the state of the process where R is running, S is sleeping in an interruptible wait, D is waiting in uninterruptible disk sleep, Z is zombie, T is traced or stopped (on a signal), and W is paging """
		self.writeCommand('pid_state_short', pid)

	def pid_stderr(self, pid):
		""" Filedescriptor binded to the STDERR of the process """
		self.writeCommand('pid_stderr', pid)

	def pid_stdin(self, pid):
		""" Filedescriptor binded to the STDIN of the process """
		self.writeCommand('pid_stdin', pid)

	def pid_stdout(self, pid):
		""" Filedescriptor binded to the STDOUT of the process """
		self.writeCommand('pid_stdout', pid)

	def pid_threads(self, pid):
		""" Number of threads in process containing this thread """
		self.writeCommand('pid_threads', pid)

	def pid_thread_list(self, pid):
		""" List with pid's from threads from this process """
		self.writeCommand('pid_thread_list', pid)

	def pid_time_kernelmode(self, pid):
		""" Amount of time that the process has been scheduled in kernel mode in seconds """
		self.writeCommand('pid_time_kernelmode', pid)

	def pid_time_usermode(self, pid):
		""" Amount of time that the process has been scheduled in user mode in seconds """
		self.writeCommand('pid_time_usermode', pid)

	def pid_time(self, pid):
		""" Sum of $pid_time_kernelmode and $pid_time_usermode """
		self.writeCommand('pid_time', pid)

	def pid_uid(self, pid):
		""" The real uid of the process """
		self.writeCommand('pid_uid', pid)

	def pid_euid(self, pid):
		""" The effective uid of the process """
		self.writeCommand('pid_euid', pid)

	def pid_suid(self, pid):
		""" The saved set uid of the process """
		self.writeCommand('pid_suid', pid)

	def pid_fsuid(self, pid):
		""" The file system uid of the process """
		self.writeCommand('pid_fsuid', pid)

	def pid_gid(self, pid):
		""" The real gid of the process """
		self.writeCommand('pid_gid', pid)

	def pid_egid(self, pid):
		""" The effective gid of the process """
		self.writeCommand('pid_egid', pid)

	def pid_sgid(self, pid):
		""" The saved set gid of the process """
		self.writeCommand('pid_sgid', pid)

	def pid_fsgid(self, pid):
		""" The file system gid of the process """
		self.writeCommand('pid_fsgid', pid)

	def pid_vmpeak(self, pid):
		""" Peak virtual memory size of the process """
		self.writeCommand('pid_vmpeak', pid)

	def pid_vmsize(self, pid):
		""" Virtual memory size of the process """
		self.writeCommand('pid_vmsize', pid)

	def pid_vmlck(self, pid):
		""" Locked memory size of the process """
		self.writeCommand('pid_vmlck', pid)

	def pid_vmhwm(self, pid):
		""" Peak resident set size ("high water mark") of the process """
		self.writeCommand('pid_vmhwm', pid)

	def pid_vmrss(self, pid):
		""" Resident set size of the process """
		self.writeCommand('pid_vmrss', pid)

	def pid_vmdata(self, pid):
		""" Data segment size of the process """
		self.writeCommand('pid_vmdata', pid)

	def pid_vmstk(self, pid):
		""" Stack segment size of the process """
		self.writeCommand('pid_vmstk', pid)

	def pid_vmexe(self, pid):
		""" Text segment size of the process """
		self.writeCommand('pid_vmexe', pid)

	def pid_vmlib(self, pid):
		""" Shared library code size of the process """
		self.writeCommand('pid_vmlib', pid)

	def pid_vmpte(self, pid):
		""" Page table entries size of the process """
		self.writeCommand('pid_vmpte', pid)

	def pid_write(self, pid):
		""" Total number of bytes written by the process """
		self.writeCommand('pid_write', pid)

	def platform(self, type, n, dev=None):
		""" Platform sensor from sysfs (Linux 2.6). Parameter dev may be omitted if you have only one platform device. Platform type is either 'in' or 'vol' meaning voltage; 'fan' meaning fan; 'temp' meaning temperature. Parameter n is number of the sensor. See /sys/bus/platform/devices/ on your local computer. The optional arguments 'factor' and 'offset' allow precalculation of the raw input, which is being modified as follows: 'input = input * factor + offset'. Note that they have to be given as decimal values (i.e. contain at least one decimal place). """
		self.writeCommand('platform')

	def pop3_unseen(self, args=None):
		""" Displays the number of unseen messages in your global POP3 inbox by default. You can define individual POP3 inboxes separately by passing arguments to this object. Arguments are: "host user pass [-i interval (in seconds)] [-p port] [-e 'command'] [-r retries]". Default port is 110, default interval is 5 minutes, and default number of retries before giving up is 5. If the password is supplied as '*', you will be prompted to enter the password when Conky starts. """
		self.writeCommand('pop3_unseen', args)

	def pop3_used(self, args=None):
		""" Displays the amount of space (in MiB, 2^20) used in your global POP3 inbox by default. You can define individual POP3 inboxes separately by passing arguments to this object. Arguments are: "host user pass [-i interval (in seconds)] [-p port] [-e 'command'] [-r retries]". Default port is 110, default interval is 5 minutes, and default number of retries before giving up is 5. If the password is supplied as '*', you will be prompted to enter the password when Conky starts. """
		self.writeCommand('pop3_used', args)

	def pre_exec(self, shell, command):
		""" Executes a shell command one time before conky displays anything and puts output as text. """
		self.writeCommand('pre_exec', [shell, command])

	def processes(self):
		""" Total processes (sleeping and running) """
		self.writeCommand('processes')

	def read_tcp(self, port, host=None):
		""" Connects to a tcp port on a host (default is localhost), reads every char available at the moment and shows them. """
		self.writeCommand('read_tcp', [host, port])

	def replied_mails(self, maildir=None):
		""" Number of mails marked as replied in the specified mailbox or mail spool if not. Only maildir type mailboxes are supported, mbox type will return -1. """
		self.writeCommand('replied_mails', maildir)

	def rss(self, uri, interval, action):
		""" Download and parse RSS feeds. The interval may be a floating point value greater than 0, otherwise defaults to 15 minutes. Action may be one of the following: feed_title, item_title (with num par), item_desc (with num par) and item_titles (when using this action and spaces_in_front is given conky places that many spaces in front of each item). This object is threaded, and once a thread is created it can't be explicitly destroyed. One thread will run for each URI specified. You can use any protocol that Curl supports. """
		self.writeCommand('rss')

	def running_processes(self):
		""" Running processes (not sleeping), requires Linux 2.6 """
		self.writeCommand('running_processes')

	def running_threads(self):
		""" Number of running (runnable) threads. Linux only. """
		self.writeCommand('running_threads')

	def scroll(self, length, text, step=None):
		""" Scroll 'text' by 'step' characters showing 'length' number of characters at the same time. The text may also contain variables. 'step' is optional and defaults to 1 if not set. If a var creates output on multiple lines then the lines are placed behind each other separated with a '|'-sign. If you change the textcolor inside $scroll it will automatically have it's old value back at the end of $scroll. The end and the start of text will be separated by 'length' number of spaces. """
		self.writeCommand('scroll', [length, step, text])

	def seen_mails(self, maildir=None):
		""" Number of mails marked as seen in the specified mailbox or mail spool if not. Only maildir type mailboxes are supported, mbox type will return -1. """
		self.writeCommand('seen_mails', maildir)

	def shadecolor(self, color=None):
		""" Change shading color """
		self.writeCommand('shadecolor', color)

	def smapi(self, args=None):
		""" when using smapi, display contents of the /sys/devices/platform/smapi directory. ARGS are either '(FILENAME)' or 'bat (INDEX) (FILENAME)' to display the corresponding files' content. This is a very raw method of accessing the smapi values. When available, better use one of the smapi_* variables instead. """
		self.writeCommand('smapi', args)

	def smapi_bat_bar(self):
		""" when using smapi, display the remaining capacity of the battery with index INDEX as a bar. """
		self.writeCommand('smapi_bat_bar')

	def smapi_bat_perc(self, index=None):
		""" when using smapi, display the remaining capacity in percent of the battery with index INDEX. This is a separate variable because it supports the 'use_spacer' configuration option. """
		self.writeCommand('smapi_bat_perc', index)

	def smapi_bat_power(self, index):
		""" when using smapi, display the current power of the battery with index INDEX in watt. This is a separate variable because the original read out value is being converted from mW. The sign of the output reflects charging (positive) or discharging (negative) state. """
		self.writeCommand('smapi_bat_power', index)

	def smapi_bat_temp(self, index):
		""" when using smapi, display the current temperature of the battery with index INDEX in degree Celsius. This is a separate variable because the original read out value is being converted from milli degree Celsius. """
		self.writeCommand('smapi_bat_temp', index)

	def sony_fanspeed(self):
		""" Displays the Sony VAIO fanspeed information if sony-laptop kernel support is enabled. Linux only. """
		self.writeCommand('sony_fanspeed')

	def stippled_hr(self, space=None):
		""" Stippled (dashed) horizontal line """
		self.writeCommand('stippled_hr', space)

	def swap(self):
		""" Amount of swap in use """
		self.writeCommand('swap')

	def swapbar(self, size=None):
		""" Bar that shows amount of swap in use """
		self.writeCommand('swapbar', size)

	def swapfree(self):
		""" Amount of free swap """
		self.writeCommand('swapfree')

	def swapmax(self):
		""" Total amount of swap """
		self.writeCommand('swapmax')

	def swapperc(self):
		""" Percentage of swap in use """
		self.writeCommand('swapperc')

	def sysname(self):
		""" System name, Linux for example """
		self.writeCommand('sysname')

	def tab(self, size=None):
		""" Puts a tab of the specified width, starting from column 'start'. The unit is pixels for both arguments. """
		self.writeCommand('tab', size)

	def tail(self, logfile, lines, next_check=None):
		""" Displays last N lines of supplied text file. The file is checked every 'next_check' update. If next_check is not supplied, Conky defaults to 2. Max of 30 lines can be displayed, or until the text buffer is filled. """
		self.writeCommand('tail', [logfile, lines, next_check])

	def tcp_portmon(self, port_begin, port_end, item, index=None):
		""" TCP port (both IPv6 and IPv4) monitor for specified local ports. Port numbers must be in the range 1 to 65535. Valid items are:count - Total number of connections in the range rip - Remote ip address rhost - Remote host name rport - Remote port number rservice - Remote service name from /etc/services lip - Local ip address lhost - Local host name lport - Local port number lservice - Local service name from /etc/services The connection index provides you with access to each connection in the port monitor. The monitor will return information for index values from 0 to n-1 connections. Values higher than n-1 are simply ignored. For the "count" item, the connection index must be omitted. It is required for all other items.Examples:${tcp_portmon 6881 6999 count} - Displays the number of connections in the bittorrent port range ${tcp_portmon 22 22 rip 0} - Displays the remote host ip of the first sshd connection ${tcp_portmon 22 22 rip 9} - Displays the remote host ip of the tenth sshd connection ${tcp_portmon 1 1024 rhost 0} - Displays the remote host name of the first connection on a privileged port ${tcp_portmon 1 1024 rport 4} - Displays the remote host port of the fifth connection on a privileged port ${tcp_portmon 1 65535 lservice 14} - Displays the local service name of the fifteenth connection in the range of all ports Note that port monitor variables which share the same port range actually refer to the same monitor, so many references to a single port range for different items and different indexes all use the same monitor internally. In other words, the program avoids creating redundant monitors. """
		self.writeCommand('tcp_portmon', [port_begin, port_end, item, index])

	def templateN(self, arg1=None):
		""" Evaluate the content of the templateN configuration variable (where N is a value between 0 and 9, inclusively), applying substitutions as described in the documentation of the corresponding configuration variable. The number of arguments is optional, but must match the highest referred index in the template. You can use the same special sequences in each argument as the ones valid for a template definition, e.g. to allow an argument to contain a whitespace. Also simple nesting of templates is possible this way.Here are some examples of template definitions:template0 $\1\2template1 \1: ${fs_used \2} / ${fs_size \2}template2 \1 \2The following list shows sample usage of the templates defined above, with the equivalent syntax when not using any template at all: using template same without template ${template0 node name} $nodename ${template1 root /} root: ${fs_free /} / ${fs_size /} ${template1 ${template2\ disk\ root} /} disk root: ${fs_free /} / ${fs_size /} """
		self.writeCommand('templateN', arg1)

	def texeci(self, interval, command):
		""" Runs a command at an interval inside a thread and displays the output. Same as $execi, except the command is run inside a thread. Use this if you have a slow script to keep Conky updating. You should make the interval slightly longer then the time it takes your script to execute. For example, if you have a script that take 5 seconds to execute, you should make the interval at least 6 seconds. See also $execi. This object will clean up the thread when it is destroyed, so it can safely be used in a nested fashion, though it may not produce the desired behaviour if used this way. """
		self.writeCommand('texeci', [interval, command])

	def threads(self):
		""" Total threads """
		self.writeCommand('threads')

	def time(self, format=None):
		""" Local time, see man strftime to get more information about format """
		self.writeCommand('time', format)

	def to_bytes(self, size):
		""" If 'size' is a number followed by a size-unit (kilobyte,mb,GiB,...) then it converts the size to bytes and shows it without unit, otherwise it just shows 'size'. """
		self.writeCommand('to_bytes', size)

	def top(self, type, num):
		""" This takes arguments in the form:top (name) (number) Basically, processes are ranked from highest to lowest in terms of cpu usage, which is what (num) represents. The types are: "name", "pid", "cpu", "mem", "mem_res", "mem_vsize", "time", "uid", "user", "io_perc", "io_read" and "io_write". There can be a max of 10 processes listed. """
		self.writeCommand('top', [type, num])

	def top_io(self, type, num):
		""" Same as top, except sorted by the amount of I/O the process has done during the update interval """
		self.writeCommand('top_io', [type, num])

	def top_mem(self, type, num):
		""" Same as top, except sorted by mem usage instead of cpu """
		self.writeCommand('top_mem', [type, num])

	def top_time(self, type, num):
		""" Same as top, except sorted by total CPU time instead of current CPU usage """
		self.writeCommand('top_time', [type, num])

	def totaldown(self, net=None):
		""" Total download, overflows at 4 GB on Linux with 32-bit arch and there doesn't seem to be a way to know how many times it has already done that before conky has started. """
		self.writeCommand('totaldown', net)

	def totalup(self, net=None):
		""" Total upload, this one too, may overflow """
		self.writeCommand('totalup', net)

	def trashed_mails(self, maildir=None):
		""" Number of mails marked as trashed in the specified mailbox or mail spool if not. Only maildir type mailboxes are supported, mbox type will return -1. """
		self.writeCommand('trashed_mails', maildir)

	def tztime(self):
		""" Local time for specified timezone, see man strftime to get more information about format. The timezone argument is specified in similar fashion as TZ environment variable. For hints, look in /usr/share/zoneinfo. e.g. US/Pacific, Europe/Zurich, etc. """
		self.writeCommand('tztime')

	def gid_name(self, gid):
		""" Name of group with this gid """
		self.writeCommand('gid_name', gid)

	def uid_name(self, uid):
		""" Username of user with this uid """
		self.writeCommand('uid_name', uid)

	def unflagged_mails(self, maildir=None):
		""" Number of mails not marked as flagged in the specified mailbox or mail spool if not. Only maildir type mailboxes are supported, mbox type will return -1. """
		self.writeCommand('unflagged_mails', maildir)

	def unforwarded_mails(self, maildir=None):
		""" Number of mails not marked as forwarded in the specified mailbox or mail spool if not. Only maildir type mailboxes are supported, mbox type will return -1. """
		self.writeCommand('unforwarded_mails', maildir)

	def unreplied_mails(self, maildir=None):
		""" Number of mails not marked as replied in the specified mailbox or mail spool if not. Only maildir type mailboxes are supported, mbox type will return -1. """
		self.writeCommand('unreplied_mails', maildir)

	def unseen_mails(self, maildir=None):
		""" Number of new or unseen mails in the specified mailbox or mail spool if not. Only maildir type mailboxes are supported, mbox type will return -1. """
		self.writeCommand('unseen_mails', maildir)

	def updates(self, n):
		""" for debugging """
		self.writeCommand('updates', n)

	def upspeed(self, net=None):
		""" Upload speed in suitable IEC units """
		self.writeCommand('upspeed', net)

	def upspeedf(self, net=None):
		""" Upload speed in KiB with one decimal """
		self.writeCommand('upspeedf', net)

	def upspeedgraph(self, netdev=None, size=None, gradientColor1=None, gradientColor2=None, scale=None, t=False, l=False):
		""" Upload speed graph, colours defined in hex, minus the #. If scale is non-zero, it becomes the scale for the graph. Uses a logarithmic scale (to see small numbers) when you use the -l switch. Takes the switch '-t' to use a temperature gradient, which makes the gradient values change depending on the amplitude of a particular graph value (try it and see). """
        parameters = [netdev, size, gradientColor1, gradientColor2, scale]
        if t:
            parameters.append('-t')
        if l:
            parameters.append('-l')
		self.writeCommand('upspeedgraph', parameters)

	def uptime(self):
		""" Uptime """
		self.writeCommand('uptime')

	def uptime_short(self):
		""" Uptime in a shorter format """
		self.writeCommand('uptime_short')

	def user_names(self):
		""" Lists the names of the users logged in """
		self.writeCommand('user_names')

	def user_number(self):
		""" Number of users logged in """
		self.writeCommand('user_number')

	def user_terms(self):
		""" Lists the consoles in use """
		self.writeCommand('user_terms')

	def user_times(self):
		""" Lists how long users have been logged in for """
		self.writeCommand('user_times')

	def user_time(self, console):
		""" Lists how long the user for the given console has been logged in for """
		self.writeCommand('user_time', console)

	def utime(self, format=None):
		""" Display time in UTC (universal coordinate time). """
		self.writeCommand('utime', format)

	def voffset(self, pixels=None):
		""" Change vertical offset by N pixels. Negative values will cause text to overlap. See also $offset. """
		self.writeCommand('voffset', pixels)

	def voltage_mv(self, n=None):
		""" Returns CPU #n's voltage in mV. CPUs are counted from 1. If omitted, the parameter defaults to 1. """
		self.writeCommand('voltage_mv', n)

	def voltage_v(self, n=None):
		""" Returns CPU #n's voltage in V. CPUs are counted from 1. If omitted, the parameter defaults to 1. """
		self.writeCommand('voltage_v', n)

	def weather(self, uri, locid, data_type, interval=None):
		""" Download, parse and display METAR data.For the 'URI', there are two possibilities: http://weather.noaa.gov/pub/data/observations/metar/stations/ http://xoap.weather.com/weather/local/The first one is free to use but the second requires you to register and obtain your partner ID and license key. These two must be written, separated by a space, into a file called .xoaprc which needs to be placed into your home directory.'locID' must be a valid location identifier for the required uri. For the NOAA site this must be a valid ICAO (see for instance https://pilotweb.nas.faa.gov/qryhtml/icao/). For the weather.com site this must be a valid location ID (see for instance http://aspnetresources.com/tools/locid.aspx).'data_type' must be one of the following:last_update - The date and time stamp of the data. The result depends on the URI used. For the NOAA site it is date (yyyy/mm/dd) and UTC time. For the weather.com one it is date ([m]m/[d]d/yy) and Local Time of the station.temperature - Air temperature (you can use the 'temperature_unit' config setting to change units)cloud_cover - The highest cloud cover statuspressure - Air pressure in millibarwind_speed - Wind speed in km/hwind_dir - Wind directionwind_dir_DEG - Compass wind directionhumidity - Relative humidity in %weather - Any relevant weather event (rain, snow, etc.). This is not used if you are querying the weather.com site since this data is aggregated into the cloud_cover oneicon - Weather icon (only for www.weather.com). Can be used together with the icon kit provided upon registering to their service.'delay_in_minutes' (optional, default 30) cannot be less than 30 minutes.This object is threaded, and once a thread is created it can't be explicitly destroyed. One thread will run for each URI specified.Note that these variables are still EXPERIMENTAL and can be subject to many future changes. """
		self.writeCommand('weather', [uri, locid, data_type, interval])

	def weather_forecast(self, uri, locid, day, data_type, interval=None):
		""" Download, parse and display weather forecast data for a given day (daytime only).For the 'URI', for the time being only http://xoap.weather.com/weather/local/ is supported. See 'weather' above for details of usage'locID', see 'weather' above.'day' is a number from 0 (today) to 4 (3 days after tomorrow).'data_type' must be one of the following:day - Day of the week date - Date, in the form MMM DD (ie. Jul 14) low - Minimun temperature (you can use the 'temperature_unit' config setting to change units) hi - Maximum temperature (you can use the 'temperature_unit' config setting to change units) icon - Weather icon. Can be used together with the icon kit provided upon registering to the weather.com service forecast - Weather forecast (sunny, rainy, etc.) wind_speed - Wind speed in km/h wind_dir - Wind direction wind_dir_DEG - Compass wind direction humidity - Relative humidity in % precipitation - Probability of having a precipitation (in %) 'delay_in_minutes' (optional, default 210) cannot be lower than 210 min.This object is threaded, and once a thread is created it can't be explicitly destroyed. One thread will run for each URI specified. You can use any protocol that Curl supports.Note that these variables are still EXPERIMENTAL and can be subject to many future changes. """
		self.writeCommand('weather_forecast', [uri, locid, day, data_type, interval])

	def wireless_ap(self, net=None):
		""" Wireless access point MAC address (Linux only) """
		self.writeCommand('wireless_ap', net)

	def wireless_bitrate(self, net=None):
		""" Wireless bitrate (ie 11 Mb/s) (Linux only) """
		self.writeCommand('wireless_bitrate', net)

	def wireless_essid(self, net=None):
		""" Wireless access point ESSID (Linux only) """
		self.writeCommand('wireless_essid', net)

	def wireless_link_bar(self, size=None, net=None):
		""" Wireless link quality bar (Linux only) """
		self.writeCommand('wireless_link_bar', [size, net])

	def wireless_link_qual(self, net=None):
		""" Wireless link quality (Linux only) """
		self.writeCommand('wireless_link_qual', net)

	def wireless_link_qual_max(self, net=None):
		""" Wireless link quality maximum value (Linux only) """
		self.writeCommand('wireless_link_qual_max', net)

	def wireless_link_qual_perc(self, net=None):
		""" Wireless link quality in percents (Linux only) """
		self.writeCommand('wireless_link_qual_perc', net)

	def wireless_mode(self, net=None):
		""" Wireless mode (Managed/Ad-Hoc/Master) (Linux only) """
		self.writeCommand('wireless_mode', net)

	def words(self, textfile):
		""" Displays the number of words in the given file """
		self.writeCommand('words', textfile)

	def xmms2_album(self):
		""" Album in current XMMS2 song """
		self.writeCommand('xmms2_album')

	def xmms2_artist(self):
		""" Artist in current XMMS2 song """
		self.writeCommand('xmms2_artist')

	def xmms2_bar(self, size=None):
		""" Bar of XMMS2's progress """
		self.writeCommand('xmms2_bar', size)

	def xmms2_bitrate(self):
		""" Bitrate of current song """
		self.writeCommand('xmms2_bitrate')

	def xmms2_comment(self):
		""" Comment in current XMMS2 song """
		self.writeCommand('xmms2_comment')

	def xmms2_date(self):
		""" Returns song's date. """
		self.writeCommand('xmms2_date')

	def xmms2_duration(self):
		""" Duration of current song """
		self.writeCommand('xmms2_duration')

	def xmms2_elapsed(self):
		""" Song's elapsed time """
		self.writeCommand('xmms2_elapsed')

	def xmms2_genre(self):
		""" Genre in current XMMS2 song """
		self.writeCommand('xmms2_genre')

	def xmms2_id(self):
		""" XMMS2 id of current song """
		self.writeCommand('xmms2_id')

	def xmms2_percent(self):
		""" Percent of song's progress """
		self.writeCommand('xmms2_percent')

	def xmms2_playlist(self):
		""" Returns the XMMS2 playlist. """
		self.writeCommand('xmms2_playlist')

	def xmms2_size(self):
		""" Size of current song """
		self.writeCommand('xmms2_size')

	def xmms2_smart(self):
		""" Prints the song name in either the form "artist - title" or file name, depending on whats available """
		self.writeCommand('xmms2_smart')

	def xmms2_status(self):
		""" XMMS2 status (Playing, Paused, Stopped, or Disconnected) """
		self.writeCommand('xmms2_status')

	def xmms2_timesplayed(self):
		""" Number of times a song was played (presumably). """
		self.writeCommand('xmms2_timesplayed')

	def xmms2_title(self):
		""" Title in current XMMS2 song """
		self.writeCommand('xmms2_title')

	def xmms2_tracknr(self):
		""" Track number in current XMMS2 song """
		self.writeCommand('xmms2_tracknr')

	def xmms2_url(self):
		""" Full path to current song """
		self.writeCommand('xmms2_url')
