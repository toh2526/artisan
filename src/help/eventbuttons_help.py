# This is an autogenerated file -- Do not edit
# Edit the source file in artisan/doc/help_dialogs/Input_files
# then execute artisan/doc/help_dialogs/Script/xlsx_to_artisan_help.py
import prettytable
import re
try:
    from PyQt6.QtWidgets import QApplication # @Reimport @UnresolvedImport @UnusedImport # pylint: disable=import-error
except Exception: # pylint: disable=broad-except
    from PyQt5.QtWidgets import QApplication # type: ignore # @Reimport @UnresolvedImport @UnusedImport

def content() -> str:
    strlist = []
    helpstr = ''  # noqa: F841 #@UnusedVariable # pylint: disable=unused-variable
    newline = '\n'  # noqa: F841 #@UnusedVariable  # pylint: disable=unused-variable
    strlist.append('<head><style> td, th {border: 1px solid #ddd;  padding: 6px;} th {padding-top: 6px;padding-bottom: 6px;text-align: left;background-color: #0C6AA6; color: white;} </style></head> <body>')
    strlist.append('<b>')
    strlist.append(QApplication.translate('HelpDlg','EVENT CUSTOM BUTTONS'))
    strlist.append('</b>')
    tbl_Buttonstop = prettytable.PrettyTable()
    tbl_Buttonstop.header = False
    tbl_Buttonstop.add_row([QApplication.translate('HelpDlg','Button numbers can be drag and dropped to a new position. While holding the ALT key (Windows) / OPTION (macOS) buttons are swapped\n')])
    strlist.append(tbl_Buttonstop.get_html_string(attributes={'width':'100%','border':'1','padding':'1','border-collapse':'collapse'}))
    tbl_Buttons = prettytable.PrettyTable()
    tbl_Buttons.field_names = [QApplication.translate('HelpDlg','Column'),QApplication.translate('HelpDlg','Description')]
    tbl_Buttons.add_row([QApplication.translate('HelpDlg','Button Label'),QApplication.translate('HelpDlg','Enter \\n to create labels with multiple lines. \\t is substituted by the event type.')])
    tbl_Buttons.add_row([QApplication.translate('HelpDlg','Event Description'),QApplication.translate('HelpDlg','Description of the Event to be recorded.')])
    tbl_Buttons.add_row([QApplication.translate('HelpDlg','Event Type'),QApplication.translate('HelpDlg','Event type to be recorded or leave blank for no event. \u0027\u00B1\u0027 types add a chosen offset (positive or negative) to the present value of the chosen event.')])
    tbl_Buttons.add_row([QApplication.translate('HelpDlg','Event Value'),QApplication.translate('HelpDlg','Value of event (1-100) to be recorded.')])
    tbl_Buttons.add_row([QApplication.translate('HelpDlg','Action'),QApplication.translate('HelpDlg','Perform an action at the time of the event.')])
    tbl_Buttons.add_row([QApplication.translate('HelpDlg','Documentation'),QApplication.translate('HelpDlg','The action Command.  Depends on the action type, &#39;{}&#39; is replaced by the event value and the offset in case of a \u00B1 event type.')])
    tbl_Buttons.add_row([QApplication.translate('HelpDlg','Button Visibility'),QApplication.translate('HelpDlg','Hides/shows individual button.')])
    strlist.append(tbl_Buttons.get_html_string(attributes={'width':'100%','border':'1','padding':'1','border-collapse':'collapse'}))
    strlist.append('<br/><br/><b>')
    strlist.append(QApplication.translate('HelpDlg','EVENT BUTTONS CONFIGURATION OPTIONS'))
    strlist.append('</b>')
    tbl_Options = prettytable.PrettyTable()
    tbl_Options.field_names = [QApplication.translate('HelpDlg','Option'),QApplication.translate('HelpDlg','Description')]
    tbl_Options.add_row([QApplication.translate('HelpDlg','Max buttons per row'),QApplication.translate('HelpDlg','Sets a maximum number of buttons to display on a single row.')])
    tbl_Options.add_row([QApplication.translate('HelpDlg','Button size'),QApplication.translate('HelpDlg','Sets a size for the buttons.  Choices are tiny, small and large.')])
    tbl_Options.add_row([QApplication.translate('HelpDlg','Color Pattern'),QApplication.translate('HelpDlg','Applies one of 99 autogenerated color patterns to the buttons.  Set to "0" to manually choose the button colors.')])
    tbl_Options.add_row([QApplication.translate('HelpDlg','Mark Last Pressed'),QApplication.translate('HelpDlg','Invert state and color of last button pressed')])
    tbl_Options.add_row([QApplication.translate('HelpDlg','Tooltips'),QApplication.translate('HelpDlg','Show button specification as tooltips on hovering a button')])
    tbl_Options.add_row([QApplication.translate('HelpDlg','Add'),QApplication.translate('HelpDlg','Adds a new button to the bottom of the table.')])
    tbl_Options.add_row([QApplication.translate('HelpDlg','Insert'),QApplication.translate('HelpDlg','Inserts a new button above the selected button.')])
    tbl_Options.add_row([QApplication.translate('HelpDlg','Delete'),QApplication.translate('HelpDlg','Deletes the selected button.')])
    tbl_Options.add_row([QApplication.translate('HelpDlg','Copy Table'),QApplication.translate('HelpDlg','Copy the button table in tab separated format to the clipboard.  Option or ALT click to copy a tabular format to the clipboard.')])
    tbl_Options.add_row([QApplication.translate('HelpDlg','Help'),QApplication.translate('HelpDlg','Opens this window.')])
    strlist.append(tbl_Options.get_html_string(attributes={'width':'100%','border':'1','padding':'1','border-collapse':'collapse'}))
    strlist.append('<br/><br/><b>')
    strlist.append(QApplication.translate('HelpDlg','LABELS'))
    strlist.append('</b>')
    tbl_Labelstop = prettytable.PrettyTable()
    tbl_Labelstop.header = False
    tbl_Labelstop.add_row([QApplication.translate('HelpDlg','The following substitutions are applied to button labels\n')])
    strlist.append(tbl_Labelstop.get_html_string(attributes={'width':'100%','border':'1','padding':'1','border-collapse':'collapse'}))
    tbl_Labels = prettytable.PrettyTable()
    tbl_Labels.field_names = [QApplication.translate('HelpDlg','String'),QApplication.translate('HelpDlg','Substitution')]
    tbl_Labels.add_row(['\\n',QApplication.translate('HelpDlg','New line character')])
    tbl_Labels.add_row(['\\t',QApplication.translate('HelpDlg','Event name (translated if using default event names)')])
    tbl_Labels.add_row(['\\q',QApplication.translate('HelpDlg','Event type 1')])
    tbl_Labels.add_row(['\\w',QApplication.translate('HelpDlg','Event type 2')])
    tbl_Labels.add_row(['\\e',QApplication.translate('HelpDlg','Event type 3')])
    tbl_Labels.add_row(['\\r',QApplication.translate('HelpDlg','Event type 4')])
    tbl_Labels.add_row(['\\0',QApplication.translate('HelpDlg','OFF (translated)')])
    tbl_Labels.add_row(['\\1',QApplication.translate('HelpDlg','ON (translated)')])
    tbl_Labels.add_row(['\\2',QApplication.translate('HelpDlg','OFF (translated, respecting button state)')])
    tbl_Labels.add_row(['\\3',QApplication.translate('HelpDlg','ON (translated, respecting button state)')])
    tbl_Labels.add_row(['\\p',QApplication.translate('HelpDlg','STOP (translated)')])
    tbl_Labels.add_row(['\\s',QApplication.translate('HelpDlg','START (translated)')])
    tbl_Labels.add_row(['\\P',QApplication.translate('HelpDlg','STOP (translated, respecting button state)')])
    tbl_Labels.add_row(['\\S',QApplication.translate('HelpDlg','START (translated, respecting button state)')])
    tbl_Labels.add_row(['\\c',QApplication.translate('HelpDlg','CLOSE (translated)')])
    tbl_Labels.add_row(['\\o',QApplication.translate('HelpDlg','OPEN (translated)')])
    tbl_Labels.add_row(['\\C',QApplication.translate('HelpDlg','CLOSE (translated, respecting button state)')])
    tbl_Labels.add_row(['\\O',QApplication.translate('HelpDlg','OPEN (translated, respecting button state)')])
    tbl_Labels.add_row(['\\a',QApplication.translate('HelpDlg','AUTO (translated)')])
    tbl_Labels.add_row(['\\m',QApplication.translate('HelpDlg','MANUAL (translated)')])
    tbl_Labels.add_row(['\\A',QApplication.translate('HelpDlg','AUTO (translated, respecting button state)')])
    tbl_Labels.add_row(['\\M',QApplication.translate('HelpDlg','MANUAL (translated, respecting button state)')])
    tbl_Labels.add_row(['\\i',QApplication.translate('HelpDlg','STIRRER')])
    tbl_Labels.add_row(['\\f',QApplication.translate('HelpDlg','FILL')])
    tbl_Labels.add_row(['\\D',QApplication.translate('HelpDlg','DISCHARGE')])
    tbl_Labels.add_row(['\\R',QApplication.translate('HelpDlg','RELEASE')])
    tbl_Labels.add_row(['\\h',QApplication.translate('HelpDlg','HEATING')])
    tbl_Labels.add_row(['\\l',QApplication.translate('HelpDlg','COOLING')])
    tbl_Labels.add_row(['\\b',QApplication.translate('HelpDlg','FLAP')])
    tbl_Labels.add_row(['\\d',QApplication.translate('HelpDlg','CONTROL')])
    tbl_Labels.add_row(['\\V',QApplication.translate('HelpDlg','event value')])
    tbl_Labels.add_row(['\\F',QApplication.translate('HelpDlg','event value interpreted as temperature in Fahrenheit converted to the current temperature mode')])
    tbl_Labels.add_row(['\\T',QApplication.translate('HelpDlg','event value interpreted as temperature in Celsius converted to the current temperature mode')])
    strlist.append(tbl_Labels.get_html_string(attributes={'width':'100%','border':'1','padding':'1','border-collapse':'collapse'}))
    strlist.append('<br/><br/><b>')
    strlist.append(QApplication.translate('HelpDlg','COMMANDS'))
    strlist.append('</b>')
    tbl_Commandstop = prettytable.PrettyTable()
    tbl_Commandstop.header = False
    tbl_Commandstop.add_row([QApplication.translate('HelpDlg','Note: "{}" can be used as a placeholder, it will be substituted by the current button value plus the offset for \u00B1 event types.  If a placeholder occurs several times in a description/command, all those occurrences are replaced by the value.\n')+newline+QApplication.translate('HelpDlg','Note: The placeholders {ET}, {BT}, {time}, {ETB}, {BTB}, and {WEIGHTin} will be substituted by the current ET, BT, time, ET background, BT background value, and batch size (in g) in Serial/Artisan/CallProgram/MODBUS/S7/WebSocket commands\n')+newline+QApplication.translate('HelpDlg','Note: Commands can be sequenced, separated by semicolons like in “<cmd1>;<cmd2>;<cmd3>”\n')+newline+QApplication.translate('HelpDlg','Note: All characters given as documentation to a Serial Command action are sent as one string to the connected device. If the device can interpret this string as separate commands separated by semicolon this is fine. Otherwise you can use a Multiple Event referencing a number of event buttons (using a comma separated list of event button numbers as documentation string) where each of the referenced event buttons issues one of the commands via a corresponding Serial Command action. Those event buttons can be hidden thus having the same effect as if the Serial Command allowed a sequence of commands.\n')+newline+QApplication.translate('HelpDlg','Note: In PHIDGET commands, the optional parameter <sn> has the form <hub_serial>[:<hub_port>] allows to refer to a specific Phidget HUB by given its serial number, and optionally specifying the port number the addressed module is connected to.\n')+newline+QApplication.translate('HelpDlg','Note: In YOCTOPUCE commands, the optional parameter <sn> holds either the modules serial number or its name')])
    strlist.append(tbl_Commandstop.get_html_string(attributes={'width':'100%','border':'1','padding':'1','border-collapse':'collapse'}))
    tbl_Commands = prettytable.PrettyTable()
    tbl_Commands.field_names = [QApplication.translate('HelpDlg','Action'),QApplication.translate('HelpDlg','Command'),QApplication.translate('HelpDlg','Description')]
    tbl_Commands.add_row([QApplication.translate('HelpDlg','Serial Command'),QApplication.translate('HelpDlg','ASCII serial command or binary a2b_uu(serial command)'),'&#160;'])
    tbl_Commands.add_row([QApplication.translate('HelpDlg','Call Program'),QApplication.translate('HelpDlg','A program/script path (absolute or relative)'),QApplication.translate('HelpDlg','start an external program')])
    tbl_Commands.add_row([QApplication.translate('HelpDlg','Multiple Event'),QApplication.translate('HelpDlg','button numbers or sleep(<float>) separated by a comma: 1,2,sleep(2.5), 3..'),QApplication.translate('HelpDlg','triggers other buttons')])
    tbl_Commands.add_row([QApplication.translate('HelpDlg','Modbus Command'),'_',QApplication.translate('HelpDlg','variable holding the last value read via MODBUS')])
    tbl_Commands.add_row(['&#160;','$',QApplication.translate('HelpDlg','variable holding the last state of the button pressed (1 or 0)')])
    tbl_Commands.add_row(['&#160;','sleep(<float>)',QApplication.translate('HelpDlg','sleep: add a delay of <float> seconds')])
    tbl_Commands.add_row(['&#160;','button(i,b)',QApplication.translate('HelpDlg','sets button i to pressed if value b is yes, true, t, or 1, otherwise to normal')])
    tbl_Commands.add_row(['&#160;','button(<bool>)',QApplication.translate('HelpDlg','sets calling button to “pressed” if argument is 1 or True')])
    tbl_Commands.add_row(['&#160;','button()',QApplication.translate('HelpDlg','toggles the state of the button')])
    tbl_Commands.add_row(['&#160;','read(slaveID,register)',QApplication.translate('HelpDlg','reads 1 16bit register from slave slaveID using function 3 (Read Multiple Holding Registers) interpreted as unsigned integer. The result is bound to the placeholder `_` and thus can be accessed in later commands.')])
    tbl_Commands.add_row(['&#160;','readSigned(slaveId,register)',QApplication.translate('HelpDlg','reads 1 16bit register from slave slaveID using function 3 (Read Multiple Holding Registers) interpreted as signed integer. The result is bound to the placeholder `_` and thus can be accessed in later commands.')])
    tbl_Commands.add_row(['&#160;','readBCD(slaveID,register)',QApplication.translate('HelpDlg','reads 1 16bit register from slave slaveID using function 3 (Read Multiple Holding Registers) interpreted as BCD. The result is bound to the placeholder `_` and thus can be accessed in later commands.')])
    tbl_Commands.add_row(['&#160;','read32(slaveID,register)',QApplication.translate('HelpDlg','reads 2 16bit registers from slave slaveID using function 3 (Read Multiple Holding Registers) interpreted as unsigned integer. The result is bound to the placeholder `_` and thus can be accessed in later commands.')])
    tbl_Commands.add_row(['&#160;','read32Signed(slaveID,register)',QApplication.translate('HelpDlg','reads 2 16bit registers from slave slaveID using function 3 (Read Multiple Holding Registers) interpreted as signed integer. The result is bound to the placeholder `_` and thus can be accessed in later commands.')])
    tbl_Commands.add_row(['&#160;','read32BCD(slaveID,register)',QApplication.translate('HelpDlg','reads 2 16bit register from slave slaveID using function 3 (Read Multiple Holding Registers) interpreted as BCD. The result is bound to the placeholder `_` and thus can be accessed in later commands.')])
    tbl_Commands.add_row(['&#160;','readFloat(slaveID,register)',QApplication.translate('HelpDlg','reads 2 16bit registers from slave slaveID using function 3 (Read Multiple Holding Registers) interpreted as float. The result is bound to the placeholder `_` and thus can be accessed in later commands.')])
    tbl_Commands.add_row(['&#160;','write(slaveId,register,value) or write([slaveId,register,value],..,[slaveId,register,value])',QApplication.translate('HelpDlg','write register: MODBUS function 6 (int) or function 16 (float)')])
    tbl_Commands.add_row(['&#160;','wcoil(slaveId,register,<bool>)',QApplication.translate('HelpDlg','write coil: MODBUS function 5')])
    tbl_Commands.add_row(['&#160;','wcoils(slaveId,register,[<bool>,..,<bool>])',QApplication.translate('HelpDlg','write coils: MODBUS function 15')])
    tbl_Commands.add_row(['&#160;','mwrite(slaveId,register,andMask,orMask) or mwrite(s,r,am,om,v)',QApplication.translate('HelpDlg','mask write register: MODBUS function 22 or simulates function 22 with function 6 and the given value v')])
    tbl_Commands.add_row(['&#160;','writem(slaveId,register,value) or writem(slaveId,register,[<int>,..,<int>])',QApplication.translate('HelpDlg','write registers: MODBUS function 16')])
    tbl_Commands.add_row(['&#160;','writeBCD(s,r,v) or writeBCD([s,r,v],..,[s,r,v])',QApplication.translate('HelpDlg','write 16bit BCD encoded value v to register r of slave s ')])
    tbl_Commands.add_row(['&#160;','writeWord(slaveId,register,value) or writeWord([slaveId,register,value],..,[slaveId,register,value])',QApplication.translate('HelpDlg','write 32bit float to two 16bit int registers: MODBUS function 16')])
    tbl_Commands.add_row(['&#160;','writeLong(slaveId,register,value) or writeLong([slaveId,register,value],..,[slaveId,register,value])',QApplication.translate('HelpDlg','write 32bit integer to two 16bit int registers: MODBUS function 16')])
    tbl_Commands.add_row(['&#160;','writeSingle(slaveId,register,value) or writeSingle([slaveId,register,value],..,[slaveId,register,value])',QApplication.translate('HelpDlg','write 16bit integer to a single 16bit register: MODBUS function 6 (int)')])
    tbl_Commands.add_row([QApplication.translate('HelpDlg','DTA Command'),QApplication.translate('HelpDlg','Insert Data address : value, ex. 4701:1000 and sv is 100. \nAlways multiply with 10 if value Unit: 0.1 / ex. 4719:0 stops heating'),'&#160;'])
    tbl_Commands.add_row([QApplication.translate('HelpDlg','IO Command'),'_',QApplication.translate('HelpDlg','variable holding the last result value')])
    tbl_Commands.add_row(['&#160;','$',QApplication.translate('HelpDlg','variable holding the last state of the button pressed (1 or 0)')])
    tbl_Commands.add_row(['&#160;','set(c,b[,sn])',QApplication.translate('HelpDlg','PHIDGET Binary Output: switches channel c off (b=0) and on (b=1)')])
    tbl_Commands.add_row(['&#160;','toggle(c[,sn])',QApplication.translate('HelpDlg','PHIDGET Binary Output: toggles channel c')])
    tbl_Commands.add_row(['&#160;','pulse(c,t[,sn])',QApplication.translate('HelpDlg','PHIDGET Binary Output: sets the output of channel c to on for time t in milliseconds')])
    tbl_Commands.add_row(['&#160;','out(c,v[,sn])',QApplication.translate('HelpDlg','PHIDGET Voltage Output: sets voltage output of channel c to v (float)')])
    tbl_Commands.add_row(['&#160;','accel(c,v[,sn])',QApplication.translate('HelpDlg','PHIDGET DCMotor: sets acceleration of channel c to v (float)')])
    tbl_Commands.add_row(['&#160;','vel(c,v[,sn])',QApplication.translate('HelpDlg','PHIDGET DCMotor: sets target velocity of channel c to v (float)')])
    tbl_Commands.add_row(['&#160;','limit(c,v[,sn])',QApplication.translate('HelpDlg','PHIDGET DCMotor: sets current limit of channel c to v (float)')])
    tbl_Commands.add_row(['&#160;','on(c[,sn])',QApplication.translate('HelpDlg','YOCTOPUCE Relay Output: turn channel c of the relay module on')])
    tbl_Commands.add_row(['&#160;','off(c[,sn])',QApplication.translate('HelpDlg','YOCTOPUCE Relay Output: turn channel c of the relay module off')])
    tbl_Commands.add_row(['&#160;','yset(c,b[,sn])',QApplication.translate('HelpDlg','YOCTOPUCE Relay Output: switches channel c of the relay module off (b=0) and on (b=1)')])
    tbl_Commands.add_row(['&#160;','flip(c[,sn])',QApplication.translate('HelpDlg','YOCTOPUCE Relay Output: toggle the state of channel c')])
    tbl_Commands.add_row(['&#160;','pip(c,delay,duration[,sn])',QApplication.translate('HelpDlg','YOCTOPUCE Relay Output: pulse the channel c on after a delay of delay milliseconds for the duration of duration milliseconds')])
    tbl_Commands.add_row(['&#160;','powerReset([sn])',QApplication.translate('HelpDlg','YOCTOPUCE resets the power counter of the Yocto-Watt module')])
    tbl_Commands.add_row(['&#160;','slider(c,v)',QApplication.translate('HelpDlg','move slider c to value v')])
    tbl_Commands.add_row(['&#160;','button(i,c,b[,sn])',QApplication.translate('HelpDlg','switches PHIDGET Binary Output channel c off (b=0) and on (b=1) and sets button i to pressed or normal depending on the value b')])
    tbl_Commands.add_row(['&#160;','button(i,b)',QApplication.translate('HelpDlg','sets button i to pressed if value b is yes, true, t, or 1, otherwise to normal')])
    tbl_Commands.add_row(['&#160;','button(b)',QApplication.translate('HelpDlg','sets button to pressed if value b is yes, true, t, or 1, otherwise to normal')])
    tbl_Commands.add_row(['&#160;','button()',QApplication.translate('HelpDlg','toggles the state of the button')])
    tbl_Commands.add_row(['&#160;','sleep(<float>)',QApplication.translate('HelpDlg','sleep: add a delay of <float> seconds')])
    tbl_Commands.add_row(['&#160;','santoker(<target>,<value>)',QApplication.translate('HelpDlg','sends integer <value> to <target> register specified by as byte in hex notation like “fa” via the Santoker Network protocol')])
    tbl_Commands.add_row(['&#160;','kaleido(<target>,<value>)',QApplication.translate('HelpDlg','sends <value> to <target> via the Kaleido Serial or Network protocol')])
    tbl_Commands.add_row([QApplication.translate('HelpDlg','Hottop Heater'),'&#160;',QApplication.translate('HelpDlg','sets heater to value')])
    tbl_Commands.add_row([QApplication.translate('HelpDlg','Hottop Fan'),'&#160;',QApplication.translate('HelpDlg','sets fan to value')])
    tbl_Commands.add_row([QApplication.translate('HelpDlg','Hottop Command'),'motor(n),solenoid(n),stirrer(n),heater(h),fan(f) ',QApplication.translate('HelpDlg','with n={0 ,1},h={0,..100},f={0,..10}')])
    tbl_Commands.add_row([QApplication.translate('HelpDlg','p-i-d'),'<p>;<i>;<d>',QApplication.translate('HelpDlg','configures PID to the values <p>;<i>;<d>')])
    tbl_Commands.add_row([QApplication.translate('HelpDlg','Fuji Command'),'write(<unitId>,<register>,<value>)','&#160;'])
    tbl_Commands.add_row([QApplication.translate('HelpDlg','PWM Command'),'out(<channel>,<value>[,<sn>])',QApplication.translate('HelpDlg','PHIDGET PWM Output: <value> in [0-100]')])
    tbl_Commands.add_row(['&#160;','toggle(<channel>[,<sn>])',QApplication.translate('HelpDlg','PHIDGET PWM Output: toggles <channel>')])
    tbl_Commands.add_row(['&#160;','pulse(<channel>,<millis>[,<sn>])',QApplication.translate('HelpDlg','PHIDGET PWM Output: turn <channel> on for <millis> milliseconds')])
    tbl_Commands.add_row(['&#160;','outhub(<port>,<value>[,<sn>])',QApplication.translate('HelpDlg','PHIDGET HUB PWM Output ON port <port> to  <value> in [0-100]')])
    tbl_Commands.add_row(['&#160;','togglehub(<port>[,<sn>])',QApplication.translate('HelpDlg','PHIDGET HUB PWM Output: toggles <port>')])
    tbl_Commands.add_row(['&#160;','pulsehub(<port>,<millis>[,<sn>])',QApplication.translate('HelpDlg','PHIDGET HUB PWM Output:  turn <port> ON for <millis> milliseconds')])
    tbl_Commands.add_row(['&#160;','enabled(c,b[,sn])',QApplication.translate('HelpDlg','YOCTOPUCE PWM Output: PWM running state')])
    tbl_Commands.add_row(['&#160;','freq(c,f[,sn])',QApplication.translate('HelpDlg','YOCTOPUCE PWM Output: set PWM frequency to f (Hz)')])
    tbl_Commands.add_row(['&#160;','duty(c,d[,sn])',QApplication.translate('HelpDlg','YOCTOPUCE PWM Output: set PWM period with the duty cycle in % as a float [0.0-100.0]')])
    tbl_Commands.add_row(['&#160;','move(c,d,t[,sn])',QApplication.translate('HelpDlg','YOCTOPUCE PWM Output: changes progressively the PWM to the specified value over the given time interval')])
    tbl_Commands.add_row([QApplication.translate('HelpDlg','VOUT Command'),'range(c,r[,sn])',QApplication.translate('HelpDlg','for PHIDGET OUTPUT modules: sets voltage voltage range (r=5 for 5V and r=10 for 10V)')])
    tbl_Commands.add_row(['&#160;','out(<n>,<v>[,<sn>])',QApplication.translate('HelpDlg','for PHIDGET OUTPUT modules: set analog output channel n to output voltage value v in V (eg. 5.5 for 5.5V)')])
    tbl_Commands.add_row(['&#160;','vout(c,v[,sn])',QApplication.translate('HelpDlg','for YOCTOPUCE VOLTAGE OUT modules with c the channel (1 or 2),v the voltage as float [0.0-10.0]')])
    tbl_Commands.add_row(['&#160;','cout(c[,sn])',QApplication.translate('HelpDlg','for YOCTOPUCE CURRENT OUT modules with c the current as float [3.0-21.0]')])
    tbl_Commands.add_row(['&#160;','sleep(<float>)',QApplication.translate('HelpDlg','sleep: add a delay of <float> seconds')])
    tbl_Commands.add_row([QApplication.translate('HelpDlg','S7 Command'),'_',QApplication.translate('HelpDlg','variable holding the last value read via S7')])
    tbl_Commands.add_row(['&#160;','$',QApplication.translate('HelpDlg','variable holding the last state of the button pressed (1 or 0)')])
    tbl_Commands.add_row(['&#160;','sleep(<float>)',QApplication.translate('HelpDlg','sleep: add a delay of <float> seconds')])
    tbl_Commands.add_row(['&#160;','button(i,b)',QApplication.translate('HelpDlg','sets button i to pressed if value b is yes, true, t, or 1, otherwise to normal')])
    tbl_Commands.add_row(['&#160;','button(<bool>)',QApplication.translate('HelpDlg','sets calling button to “pressed” if argument is 1 or True')])
    tbl_Commands.add_row(['&#160;','button()',QApplication.translate('HelpDlg','toggles the state of the button')])
    tbl_Commands.add_row(['&#160;','getDBbool(<dbnumber>,<start>,<index>)',QApplication.translate('HelpDlg','read bool from S7 DB')])
    tbl_Commands.add_row(['&#160;','getDBint(<dbnumber>,<start>)',QApplication.translate('HelpDlg','read int from S7 DB')])
    tbl_Commands.add_row(['&#160;','getDBfloat(<dbnumber>,<start>)',QApplication.translate('HelpDlg','read float from S7 DB')])
    tbl_Commands.add_row(['&#160;','setDBbool(<dbnumber>,<start>,<index>,<value>)',QApplication.translate('HelpDlg','write bool to S7 DB')])
    tbl_Commands.add_row(['&#160;','setDBint(<dbnumber>,<start>,<value>)',QApplication.translate('HelpDlg','write int to S7 DB')])
    tbl_Commands.add_row(['&#160;','msetDBint(<dbnumber>,<start>,<andMask>,<orMask>,<value>)',QApplication.translate('HelpDlg','write value where bits are replaced by those from orMask at positions where andMask bits are not set')])
    tbl_Commands.add_row(['&#160;','setDBfloat(<dbnumber>,<start>,<value>)',QApplication.translate('HelpDlg','write float to S7 DB')])
    tbl_Commands.add_row([QApplication.translate('HelpDlg','Aillio R1 Heater'),'&#160;',QApplication.translate('HelpDlg','sets heater to value')])
    tbl_Commands.add_row([QApplication.translate('HelpDlg','Aillio R1 Fan'),'&#160;',QApplication.translate('HelpDlg','sets fan to value')])
    tbl_Commands.add_row([QApplication.translate('HelpDlg','Aillio R1 Drum'),'&#160;',QApplication.translate('HelpDlg','sets drum speed to value')])
    tbl_Commands.add_row([QApplication.translate('HelpDlg','Aillio R1 Command'),'PRS',QApplication.translate('HelpDlg','Sends PRS command')])
    tbl_Commands.add_row([QApplication.translate('HelpDlg','Artisan Command'),'$',QApplication.translate('HelpDlg','variable holding the last state of the button pressed (1 or 0)')])
    tbl_Commands.add_row(['&#160;','alarm(n,<bool>)',QApplication.translate('HelpDlg','enables/disables alarm number n')])
    tbl_Commands.add_row(['&#160;','alarms(<bool>)',QApplication.translate('HelpDlg','enables/disables alarms')])
    tbl_Commands.add_row(['&#160;','autoCHARGE(<bool>)',QApplication.translate('HelpDlg','enables/disables autoCHARGE')])
    tbl_Commands.add_row(['&#160;','autoDROP(<bool>)',QApplication.translate('HelpDlg','enables/disables autoDROP')])
    tbl_Commands.add_row(['&#160;','sleep(<float>)',QApplication.translate('HelpDlg','sleep: add a delay of <float> seconds')])
    tbl_Commands.add_row(['&#160;','tare(<int>)',QApplication.translate('HelpDlg','tare channel <int> with 1 => ET, 2 => BT, 3 => E1c1, 4: E1c2,..')])
    tbl_Commands.add_row(['&#160;','PIDon',QApplication.translate('HelpDlg','turns PID on')])
    tbl_Commands.add_row(['&#160;','PIDoff',QApplication.translate('HelpDlg','turns PID off')])
    tbl_Commands.add_row(['&#160;','PIDtoggle',QApplication.translate('HelpDlg','toggles the PID state')])
    tbl_Commands.add_row(['&#160;','pidmode(<int>)',QApplication.translate('HelpDlg','sets PID mode to 0: manual, 1: RS, 2: background follow')])
    tbl_Commands.add_row(['&#160;','p-i-d(<p>,<i>,<d>)',QApplication.translate('HelpDlg','sets the p-i-d parameters of the PID')])
    tbl_Commands.add_row(['&#160;','adjustSV(<int>)',QApplication.translate('HelpDlg','increases or decreases the current target SV value by <int>')])
    tbl_Commands.add_row(['&#160;','pidSV(<int>)',QApplication.translate('HelpDlg','sets the PID target set value SV')])
    tbl_Commands.add_row(['&#160;','pidSVC(<int>)',QApplication.translate('HelpDlg','sets the PID target set value SV given in C')])
    tbl_Commands.add_row(['&#160;','pidRS(<rs>)',QApplication.translate('HelpDlg','activates the PID Ramp-Soak pattern number <rs> (1-based!) or the one labeled <rs>')])
    tbl_Commands.add_row(['&#160;','pidSource(<int>)',QApplication.translate('HelpDlg','selects the PID input source with <n> 0: BT, 1: ET (Software PID); <n> in {0,..,3} (Arduino PID)')])
    tbl_Commands.add_row(['&#160;','pidLookahead(<int>)',QApplication.translate('HelpDlg','sets the PID lookahead')])
    tbl_Commands.add_row(['&#160;','popup(<msg>[,<int>])',QApplication.translate('HelpDlg','shows popup with message <msg> which optionally automatically closes after <int> seconds')])
    tbl_Commands.add_row(['&#160;','message(<msg>)',QApplication.translate('HelpDlg','shows message <msg> in the message line')])
    tbl_Commands.add_row(['&#160;','notifications(<bool>)',QApplication.translate('HelpDlg','enables/disables notifications; while disabled issued notifications are ignored')])
    tbl_Commands.add_row(['&#160;','notify(<title>,[<msg>])',QApplication.translate('HelpDlg','sends notification with title <title> and optional message <msg>')])
    tbl_Commands.add_row(['&#160;','setCanvasColor(<color>)',QApplication.translate('HelpDlg','sets canvas color to the RGB-hex <color> like #27f1d3')])
    tbl_Commands.add_row(['&#160;','resetCanvasColor',QApplication.translate('HelpDlg','resets canvas color')])
    tbl_Commands.add_row(['&#160;','button(i,b)',QApplication.translate('HelpDlg','sets button i to pressed if value of b is yes, true, t, or 1, otherwise to normal')])
    tbl_Commands.add_row(['&#160;','button(<name>|<bool>)',QApplication.translate('HelpDlg','activates button <name> from { START, CHARGE, DRY, FCs, FCe, SCs, SCe, DROP, COOL, OFF } ; sets calling button to “pressed” if argument is 1 or True')])
    tbl_Commands.add_row(['&#160;','button()',QApplication.translate('HelpDlg','toggles the state of the button')])
    tbl_Commands.add_row(['&#160;','visible(i,b)',QApplication.translate('HelpDlg','sets button i to visible if value of b is yes, true, t, or 1, otherwise to hidden')])
    tbl_Commands.add_row(['&#160;','palette(<p>)',QApplication.translate('HelpDlg','activates palette <p> with <p> either a number 0-9 or a palette label')])
    tbl_Commands.add_row(['&#160;','playbackmode(<int>)',QApplication.translate('HelpDlg','sets playback mode to 0: off, 1: time, 2: BT, 3: ET')])
    tbl_Commands.add_row(['&#160;','playback(n,<bool>)',QApplication.translate('HelpDlg','toggles playback per event type n from {1,2,3,4}')])
    tbl_Commands.add_row(['&#160;','ramp(n,<bool>)',QApplication.translate('HelpDlg','toggles playback ramping per event type n from {1,2,3,4}')])
    tbl_Commands.add_row(['&#160;','quantifier(n,<bool>)',QApplication.translate('HelpDlg','activate/deactivate quantification per event type n from {1,2,3,4}')])
    tbl_Commands.add_row(['&#160;','setBatchSize(<float>)',QApplication.translate('HelpDlg','set the batch size to the given value. If the value is negative, the batch size is taken from the background profile, if any is loaded')])
    tbl_Commands.add_row(['&#160;','openProperties',QApplication.translate('HelpDlg','opens the Roast Properties dialog')])
    tbl_Commands.add_row(['&#160;','loadBackground(<filepath>)',QApplication.translate('HelpDlg','loads the .alog profile at the given filepath as background profile')])
    tbl_Commands.add_row(['&#160;','clearBackground',QApplication.translate('HelpDlg','clears the current background profile')])
    tbl_Commands.add_row(['&#160;','alarmset(<as>)',QApplication.translate('HelpDlg','activates the alarmset with the given number or label')])
    tbl_Commands.add_row(['&#160;','moveBackground(<direction>,<int>)',QApplication.translate('HelpDlg','moves the background profile the indicated number of steps towards <direction>, with <direction> one of up, down, left, right')])
    tbl_Commands.add_row(['&#160;','keyboard(<bool>)',QApplication.translate('HelpDlg','enables/disables keyboard mode')])
    tbl_Commands.add_row(['&#160;','keepON(<bool>)',QApplication.translate('HelpDlg','enables/disables the Keep ON flag')])
    tbl_Commands.add_row(['&#160;','showCurve(<name>,<bool>)',QApplication.translate('HelpDlg','shows/hides the curve indicated by <name> which is one of { ET, BT, DeltaET, DeltaBT, BackgroundET, BackgroundBT}')])
    tbl_Commands.add_row(['&#160;','showExtraCurve(<extra_device>,<curve>,<bool>)',QApplication.translate('HelpDlg','shows/hides the <curve> (one of {T1,T2}) of the zero-based <extra_device> number')])
    tbl_Commands.add_row(['&#160;','showEvents(<event_type>, <bool>)',QApplication.translate('HelpDlg','shows/hides the events of <event_type> in [1,..,5]')])
    tbl_Commands.add_row(['&#160;','showBackgroundEvents(<bool>)',QApplication.translate('HelpDlg','shows/hides the events of the background profile')])
    tbl_Commands.add_row([QApplication.translate('HelpDlg','RC Command'),'pulse(ch,min,max[,sn])',QApplication.translate('HelpDlg','for PHIDGET RC modules: sets the min/max pulse width in microseconds')])
    tbl_Commands.add_row(['&#160;','pos(ch,min,max[,sn])',QApplication.translate('HelpDlg','for PHIDGET RC modules: sets the min/max position')])
    tbl_Commands.add_row(['&#160;','engaged(ch,b[,sn])',QApplication.translate('HelpDlg','for PHIDGET RC modules: engage (b=1) or disengage (b = 0)')])
    tbl_Commands.add_row(['&#160;','ramp(ch,b[,sn])',QApplication.translate('HelpDlg','for PHIDGET RC modules: activates or deactivates the speed ramping state')])
    tbl_Commands.add_row(['&#160;','volt(ch,v[,sn])',QApplication.translate('HelpDlg','for PHIDGET RC modules: set the voltage to one of 5, 6 or 7.4 in Volt')])
    tbl_Commands.add_row(['&#160;','accel(ch,a[,sn])',QApplication.translate('HelpDlg','for PHIDGET RC modules: set the acceleration')])
    tbl_Commands.add_row(['&#160;','veloc(ch,v[,sn])',QApplication.translate('HelpDlg','for PHIDGET RC modules: set the velocity')])
    tbl_Commands.add_row(['&#160;','set(ch,pos[,sn])',QApplication.translate('HelpDlg','for PHIDGET RC modules: set the target position')])
    tbl_Commands.add_row(['&#160;','enabled(c,b[,sn])',QApplication.translate('HelpDlg','for YOCTOPUCE RC modules: with c:int the channel, b a bool (eg. enabled(0,1) or enabled(0,True))')])
    tbl_Commands.add_row(['&#160;','move(c,p[,t][,sn])',QApplication.translate('HelpDlg','for YOCTOPUCE RC modules: with c:int the channel, p:int the target position, the optional t the duration in ms, sn the optional modules serial number or logical name')])
    tbl_Commands.add_row(['&#160;','neutral(c,n[,sn])',QApplication.translate('HelpDlg','for YOCTOPUCE RC modules: with n an int [0..65000] in us')])
    tbl_Commands.add_row(['&#160;','range(c,r[,sn])',QApplication.translate('HelpDlg','for YOCTOPUCE RC modules: with r an int in %')])
    tbl_Commands.add_row([QApplication.translate('HelpDlg','WebSocket Command'),'$',QApplication.translate('HelpDlg','variable holding the last state of the button pressed (1 or 0)')])
    tbl_Commands.add_row(['&#160;','send(<json>)',QApplication.translate('HelpDlg','If {} substitutions are used, json brackets need to be duplicated to escape them like in send({{ “value”: {}}})')])
    tbl_Commands.add_row(['&#160;','sleep(<float>)',QApplication.translate('HelpDlg','sleep: add a delay of <float> seconds')])
    tbl_Commands.add_row(['&#160;','button(i,b)',QApplication.translate('HelpDlg','sets button i to pressed if value b is yes, true, t, or 1, otherwise to normal')])
    tbl_Commands.add_row(['&#160;','button(<bool>)',QApplication.translate('HelpDlg','sets calling button to “pressed” if argument evaluates to 1 or True')])
    tbl_Commands.add_row(['&#160;','button()',QApplication.translate('HelpDlg','toggles the state of the button')])
    tbl_Commands.add_row(['&#160;','read(<json>)',QApplication.translate('HelpDlg','if the `<json>` text respects the JSON format it is send to the connected WebSocket server and the response is bound to the variable `_`')])
    strlist.append(tbl_Commands.get_html_string(attributes={'width':'100%','border':'1','padding':'1','border-collapse':'collapse'}))
    strlist.append('</body>')
    helpstr = ''.join(strlist)
    return re.sub(r'&amp;', r'&',helpstr)
