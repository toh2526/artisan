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
    strlist.append(QApplication.translate('HelpDlg','EVENT CUSTOM SLIDERS'))
    strlist.append('</b>')
    tbl_Sliders = prettytable.PrettyTable()
    tbl_Sliders.field_names = [QApplication.translate('HelpDlg','Column'),QApplication.translate('HelpDlg','Description')]
    tbl_Sliders.add_row([QApplication.translate('HelpDlg','Event'),QApplication.translate('HelpDlg','Hide or show the corresponding slider.')])
    tbl_Sliders.add_row([QApplication.translate('HelpDlg','Action'),QApplication.translate('HelpDlg','Perform an action on the slider release.')])
    tbl_Sliders.add_row([QApplication.translate('HelpDlg','Command'),QApplication.translate('HelpDlg','Command to perform, depends on the Action type. (&#39;{}&#39; is replaced by the slider value*Factor + Offset)')])
    tbl_Sliders.add_row([QApplication.translate('HelpDlg','Offset'),QApplication.translate('HelpDlg','Offset to be added to the Slider value (after scaling by Factor).')])
    tbl_Sliders.add_row([QApplication.translate('HelpDlg','Factor'),QApplication.translate('HelpDlg','Scale factor, Slider value is multiplied by this value.')])
    tbl_Sliders.add_row([QApplication.translate('HelpDlg','Min'),QApplication.translate('HelpDlg','Sets the minimum value for the range of the slider.')])
    tbl_Sliders.add_row([QApplication.translate('HelpDlg','Max'),QApplication.translate('HelpDlg','Sets the maximum value for the range of the slider.')])
    tbl_Sliders.add_row([QApplication.translate('HelpDlg','Course'),QApplication.translate('HelpDlg','When ticked the slider moves in steps of 10.')])
    tbl_Sliders.add_row([QApplication.translate('HelpDlg','Temp'),QApplication.translate('HelpDlg','Should be ticked when the slider&#39;s value is a temperature to allow Artisan to properly scale the value between Centigrade and Fahrenheit.')])
    tbl_Sliders.add_row([QApplication.translate('HelpDlg','Unit'),QApplication.translate('HelpDlg','Optional text used in annotations to the the units used for the slider value.')])
    strlist.append(tbl_Sliders.get_html_string(attributes={'width':'100%','border':'1','padding':'1','border-collapse':'collapse'}))
    strlist.append('<br/><br/><b>')
    strlist.append(QApplication.translate('HelpDlg','COMMANDS'))
    strlist.append('</b>')
    tbl_Commandstop = prettytable.PrettyTable()
    tbl_Commandstop.header = False
    tbl_Commandstop.add_row([QApplication.translate('HelpDlg','Note: "{}" can be used as a placeholder, it will be substituted by (value*factor + offset). In all slider command actions, but for IO, VOUT, S7 and RC Commands, the bound value is converted from a float to an int.\n')+newline+QApplication.translate('HelpDlg','Note: The placeholders {ET}, {BT}, {time}, {ETB}, {BTB}, and {WEIGHTin} will be substituted by the current ET, BT, time, ET background, BT background value, and batch size (in g) in Serial/Artisan/CallProgram/MODBUS/S7/WebSocket commands\n')+newline+QApplication.translate('HelpDlg','Note: commands can be sequenced, separated by semicolons like in “<cmd1>;<cmd2>;<cmd3>”\n')+newline+QApplication.translate('HelpDlg','Note: in PHIDGET commands, the optional parameter <sn> has the form <hub_serial>[:<hub_port>] allows to refer to a specific Phidget HUB by given its serial number, and optionally specifying the port number the addressed module is connected to.\n')+newline+QApplication.translate('HelpDlg','Note: in YOCTOPUCE commands, the optional parameters <sn> holds either the modules serial number or its name')])
    strlist.append(tbl_Commandstop.get_html_string(attributes={'width':'100%','border':'1','padding':'1','border-collapse':'collapse'}))
    tbl_Commands = prettytable.PrettyTable()
    tbl_Commands.field_names = [QApplication.translate('HelpDlg','Action'),QApplication.translate('HelpDlg','Command'),QApplication.translate('HelpDlg','Description')]
    tbl_Commands.add_row([QApplication.translate('HelpDlg','Serial Command'),QApplication.translate('HelpDlg','ASCII serial command or binary a2b_uu(serial command)'),'&#160;'])
    tbl_Commands.add_row([QApplication.translate('HelpDlg','Modbus Command'),'_',QApplication.translate('HelpDlg','variable holding the last value read via MODBUS')])
    tbl_Commands.add_row(['&#160;','sleep(<float>)',QApplication.translate('HelpDlg','sleep: add a delay of <float> seconds')])
    tbl_Commands.add_row(['&#160;','button(<bool>)',QApplication.translate('HelpDlg','sets calling button to “pressed” if argument is 1 or True')])
    tbl_Commands.add_row(['&#160;','read(slaveID,register)',QApplication.translate('HelpDlg','reads register from slave slaveID using function 3 (Read Multiple Holding Registers). The result is bound to the placeholder `_` and thus can be accessed in later commands.')])
    tbl_Commands.add_row(['&#160;','readSigned(slaveId,register)',QApplication.translate('HelpDlg','reads 1 16bit register from slave slaveID using function 3 (Read Multiple Holding Registers) interpreted as signed integer. The result is bound to the placeholder `_` and thus can be accessed in later commands.')])
    tbl_Commands.add_row(['&#160;','readBCD(slaveID,register)',QApplication.translate('HelpDlg','reads 1 16bit register from slave slaveID using function 3 (Read Multiple Holding Registers) interpreted as BCD. The result is bound to the placeholder `_` and thus can be accessed in later commands.')])
    tbl_Commands.add_row(['&#160;','read32(slaveID,register)',QApplication.translate('HelpDlg','reads 2 16bit registers from slave slaveID using function 3 (Read Multiple Holding Registers) interpreted as unsigned integer. The result is bound to the placeholder `_` and thus can be accessed in later commands.')])
    tbl_Commands.add_row(['&#160;','read32Signed(slaveID,register)',QApplication.translate('HelpDlg','reads 2 16bit registers from slave slaveID using function 3 (Read Multiple Holding Registers) interpreted as signed integer. The result is bound to the placeholder `_` and thus can be accessed in later commands.')])
    tbl_Commands.add_row(['&#160;','read32BCD(slaveID,register)',QApplication.translate('HelpDlg','reads 2 16bit register from slave slaveID using function 3 (Read Multiple Holding Registers) interpreted as BCD. The result is bound to the placeholder `_` and thus can be accessed in later commands.')])
    tbl_Commands.add_row(['&#160;','readFloat(slaveID,register)',QApplication.translate('HelpDlg','reads 2 16bit registers from slave slaveID using function 3 (Read Multiple Holding Registers) interpreted as float. The result is bound to the placeholder `_` and thus can be accessed in later commands.')])
    tbl_Commands.add_row(['&#160;','write(slaveId,register,value) or write([slaveId,register,value],..,[slaveId,register,value])',QApplication.translate('HelpDlg','write register: MODBUS function 6 (int) or function 16 (float)')])
    tbl_Commands.add_row(['&#160;','wcoil(slaveId,register,<bool>)',QApplication.translate('HelpDlg','write coil: MODBUS function 5')])
    tbl_Commands.add_row(['&#160;','wcoils(slaveId,register,[<bool>,..,<bool>])',QApplication.translate('HelpDlg','write coils: MODBUS function 15')])
    tbl_Commands.add_row([QApplication.translate('HelpDlg',' '),'mwrite(slaveId,register,andMask,orMask) or mwrite(s,r,am,om,v)',QApplication.translate('HelpDlg','mask write register: MODBUS function 22 or simulates function 22 with function 6 and the given value v')])
    tbl_Commands.add_row(['&#160;','writem(slaveId,register,value) or writem(slaveId,register,[<int>,..,<int>])',QApplication.translate('HelpDlg','write registers: MODBUS function 16')])
    tbl_Commands.add_row(['&#160;','writeBCD(s,r,v) or writeBCD([s,r,v],..,[s,r,v])',QApplication.translate('HelpDlg','write 16bit BCD encoded value v to register r of slave s ')])
    tbl_Commands.add_row(['&#160;','writeWord(slaveId,register,value) or writeWord([slaveId,register,value],..,[slaveId,register,value])',QApplication.translate('HelpDlg','write 32bit float to two 16bit int registers: MODBUS function 16')])
    tbl_Commands.add_row(['&#160;','writeLong(slaveId,register,value) or writeLong([slaveId,register,value],..,[slaveId,register,value])',QApplication.translate('HelpDlg','write 32bit integer to two 16bit int registers: MODBUS function 16')])
    tbl_Commands.add_row(['&#160;','writeSingle(slaveId,register,value) or writeSingle([slaveId,register,value],..,[slaveId,register,value])',QApplication.translate('HelpDlg','write 16bit integer to a single 16bit register: MODBUS function 6 (int)')])
    tbl_Commands.add_row([QApplication.translate('HelpDlg','DTA Command'),QApplication.translate('HelpDlg','Insert Data address : value, ex. 4701:1000 and sv is 100. '),QApplication.translate('HelpDlg','Always multiply with 10 if value Unit: 0.1 / ex. 4719:0 stops heating')])
    tbl_Commands.add_row([QApplication.translate('HelpDlg','Call Program'),QApplication.translate('HelpDlg','A program/script path (absolute or relative)'),QApplication.translate('HelpDlg','start and external program')])
    tbl_Commands.add_row([QApplication.translate('HelpDlg','Hottop Heater'),'&#160;',QApplication.translate('HelpDlg','sets heater to value')])
    tbl_Commands.add_row([QApplication.translate('HelpDlg','Hottop Fan'),'&#160;',QApplication.translate('HelpDlg','sets fan to value')])
    tbl_Commands.add_row([QApplication.translate('HelpDlg','Hottop Command'),'motor(n),solenoid(n),stirrer(n),heater(h),fan(f) ',QApplication.translate('HelpDlg','with n={0 ,1},h={0,..100},f={0,..10}')])
    tbl_Commands.add_row([QApplication.translate('HelpDlg','Fuji Command'),'write(<unitId>,<register>,<value>)','&#160;'])
    tbl_Commands.add_row([QApplication.translate('HelpDlg','PWM Command'),'out(<channel>,<value>[,<sn>])',QApplication.translate('HelpDlg','PHIDGET PWM Output: <value> in [0-100]')])
    tbl_Commands.add_row(['&#160;','toggle(<channel>[,<sn>])',QApplication.translate('HelpDlg','PHIDGET PWM Output: toggles <channel>')])
    tbl_Commands.add_row(['&#160;','pulse(<channel>,<millis>[,<sn>])',QApplication.translate('HelpDlg','PHIDGET PWM Output: turn <channel> on for <millis> milliseconds')])
    tbl_Commands.add_row(['&#160;','outhub(<channel>,<value>[,<sn>])',QApplication.translate('HelpDlg','PHIDGET HUB PWM Output: <value> in [0-100]')])
    tbl_Commands.add_row(['&#160;','togglehub(<channel>[,<sn>])',QApplication.translate('HelpDlg','PHIDGET HUB PWM Output: toggles <channel>')])
    tbl_Commands.add_row(['&#160;','pulsehub(<channel>,<millis>[,<sn>])',QApplication.translate('HelpDlg','PHIDGET HUB PWM Output:  turn <channel> on for <millis> milliseconds')])
    tbl_Commands.add_row(['&#160;','enabled(c,b[,sn])',QApplication.translate('HelpDlg','YOCTOPUCE PWM Output: PWM running state')])
    tbl_Commands.add_row(['&#160;','freq(c,f[,sn])',QApplication.translate('HelpDlg','YOCTOPUCE PWM Output: set PWM frequency to f (Hz)')])
    tbl_Commands.add_row(['&#160;','duty(c,d[,sn])',QApplication.translate('HelpDlg','YOCTOPUCE PWM Output: set PWM period with the duty cycle in % as a float [0.0-100.0]')])
    tbl_Commands.add_row(['&#160;','move(c,d,t[,sn])',QApplication.translate('HelpDlg','YOCTOPUCE PWM Output: changes progressively the PWM to the specified value over the given time interval')])
    tbl_Commands.add_row([QApplication.translate('HelpDlg','VOUT Command'),'range(c,r[,sn])',QApplication.translate('HelpDlg','for PHIDGET OUTPUT modules: sets voltage voltage range (r=5 for r5V and r=10 for 10V)')])
    tbl_Commands.add_row(['&#160;','out(n,v[,sn])',QApplication.translate('HelpDlg','for PHIDGET OUTPUT modules: set analog output channel n to output voltage value v in V (eg. 5.5 for 5.5V)')])
    tbl_Commands.add_row(['&#160;','vout(c,v[,sn])',QApplication.translate('HelpDlg','for YOCTOPUCE VOLTAGE OUT modules with c the channel (1 or 2),v the voltage as float [0.0-10.0]')])
    tbl_Commands.add_row(['&#160;','cout(c[,sn])',QApplication.translate('HelpDlg','for YOCTOPUCE CURRENT OUT modules with c the current as float [3.0-21.0]')])
    tbl_Commands.add_row(['&#160;','sleep(<float>)',QApplication.translate('HelpDlg','sleep: add a delay of <float> seconds')])
    tbl_Commands.add_row([QApplication.translate('HelpDlg','IO Command'),'set(c,b[,sn])',QApplication.translate('HelpDlg','PHIDGET Binary Output: switches channel c off (b=0) and on (b=1)')])
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
    tbl_Commands.add_row([QApplication.translate('HelpDlg','S7 Command'),'_',QApplication.translate('HelpDlg','variable holding the last value read via S7')])
    tbl_Commands.add_row(['&#160;','sleep(<float>)',QApplication.translate('HelpDlg','sleep: add a delay of <float> seconds')])
    tbl_Commands.add_row(['&#160;','button(<bool>)',QApplication.translate('HelpDlg','sets calling button to “pressed” if argument evaluates to 1 or True')])
    tbl_Commands.add_row(['&#160;','getDBbool(<dbnumber>,<start>,<index>)',QApplication.translate('HelpDlg','read bool from S7 DB')])
    tbl_Commands.add_row(['&#160;','getDBint(<dbnumber>,<start>)',QApplication.translate('HelpDlg','read int from S7 DB')])
    tbl_Commands.add_row(['&#160;','getDBfloat(<dbnumber>,<start>)',QApplication.translate('HelpDlg','read float from S7 DB')])
    tbl_Commands.add_row(['&#160;','setDBbool(<dbnumber>,<start>,<index>,<value>)',QApplication.translate('HelpDlg','write bool to S7 DB')])
    tbl_Commands.add_row(['&#160;','setDBint(<dbnumber>,<start>,<value>)',QApplication.translate('HelpDlg','write int to S7 DB')])
    tbl_Commands.add_row(['&#160;','setDBfloat(<dbnumber>,<start>,<value>)',QApplication.translate('HelpDlg','write float to S7 DB')])
    tbl_Commands.add_row([QApplication.translate('HelpDlg','Aillio R1 Heater'),'&#160;',QApplication.translate('HelpDlg','sets heater to value')])
    tbl_Commands.add_row([QApplication.translate('HelpDlg','Aillio R1 Fan'),'&#160;',QApplication.translate('HelpDlg','sets fan to value')])
    tbl_Commands.add_row([QApplication.translate('HelpDlg','Aillio R1 Drum'),'&#160;',QApplication.translate('HelpDlg','sets drum speed to value')])
    tbl_Commands.add_row([QApplication.translate('HelpDlg','Artisan Command'),'&#160;',QApplication.translate('HelpDlg','enables/disables alarms')])
    tbl_Commands.add_row(['&#160;','alarm(n,<bool>)',QApplication.translate('HelpDlg','enables/disables alarm number n')])
    tbl_Commands.add_row(['&#160;','autoCHARGE(<bool>)',QApplication.translate('HelpDlg','enables/disables autoCHARGE')])
    tbl_Commands.add_row(['&#160;','autoDROP(<bool>)',QApplication.translate('HelpDlg','enables/disables autoDROP')])
    tbl_Commands.add_row(['&#160;','sleep(<float>)',QApplication.translate('HelpDlg','sleep: add a delay of <float> seconds')])
    tbl_Commands.add_row(['&#160;','tare(<int>)',QApplication.translate('HelpDlg','tare channel <int> with 1 => ET, 2 => BT, 3 => E1c1, 4: E1c2,..')])
    tbl_Commands.add_row(['&#160;','PIDon',QApplication.translate('HelpDlg','turns PID on')])
    tbl_Commands.add_row(['&#160;','PIDoff',QApplication.translate('HelpDlg','turns PID off')])
    tbl_Commands.add_row(['&#160;','PIDtoggle',QApplication.translate('HelpDlg','toggles the PID state')])
    tbl_Commands.add_row(['&#160;','pidmode(<int>)',QApplication.translate('HelpDlg','sets PID mode to 0: manual, 1: RS, 2: background follow')])
    tbl_Commands.add_row(['&#160;','p-i-d(<p>,<i>,<d>)',QApplication.translate('HelpDlg','sets the p-i-d parameters of the PID')])
    tbl_Commands.add_row(['&#160;','adjustSV(<float>)',QApplication.translate('HelpDlg','increases or decreases the current target SV value by <float>')])
    tbl_Commands.add_row(['&#160;','pidSV(<float>)',QApplication.translate('HelpDlg','sets the PID target set value SV')])
    tbl_Commands.add_row(['&#160;','pidSVC(<float>)',QApplication.translate('HelpDlg','sets the PID target set value SV given in C')])
    tbl_Commands.add_row(['&#160;','pidRS(<rs>)',QApplication.translate('HelpDlg','activates the PID Ramp-Soak pattern number <rs> (1-based!) or the one labeled <rs>')])
    tbl_Commands.add_row(['&#160;','pidSource(<int>)',QApplication.translate('HelpDlg','selects the PID input source with <n> 0: BT, 1: ET (Software PID); <n> in {0,..,3} (Arduino PID)')])
    tbl_Commands.add_row(['&#160;','pidLookahead(<int>)',QApplication.translate('HelpDlg','sets the PID lookahead')])
    tbl_Commands.add_row(['&#160;','popup(<msg>[,<int>])',QApplication.translate('HelpDlg','shows popup with message <msg> which optionally automatically closes after <int> seconds')])
    tbl_Commands.add_row(['&#160;','message(<msg>)',QApplication.translate('HelpDlg','shows message <msg> in the message line')])
    tbl_Commands.add_row(['&#160;','notifications(<bool>)',QApplication.translate('HelpDlg','enables/disables notifications; while disabled issued notifications are ignored')])
    tbl_Commands.add_row(['&#160;','notify(<title>,[<msg>])',QApplication.translate('HelpDlg','sends notification with title <title> and optional message <msg>')])
    tbl_Commands.add_row(['&#160;','setCanvasColor(<color>)',QApplication.translate('HelpDlg','sets canvas color to the RGB-hex <color> like #27f1d3')])
    tbl_Commands.add_row(['&#160;','resetCanvasColor',QApplication.translate('HelpDlg','resets canvas color')])
    tbl_Commands.add_row(['&#160;','button(<name>)',QApplication.translate('HelpDlg','activates button <name> from { START, CHARGE, DRY, FCs, FCe, SCs, SCe, DROP, COOL, OFF } ')])
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
    tbl_Commands.add_row(['&#160;','move(c,p[,t][,sn])',QApplication.translate('HelpDlg','for YOCTOPUCE RC modules: with c:int the channel, p:int the target position, the optional t the duration in ms')])
    tbl_Commands.add_row(['&#160;','neutral(c,n[,sn])',QApplication.translate('HelpDlg','for YOCTOPUCE RC modules: with n an int [0..65000] in us')])
    tbl_Commands.add_row(['&#160;','range(c,r[,sn])',QApplication.translate('HelpDlg','for YOCTOPUCE RC modules: with r an int in %')])
    tbl_Commands.add_row([QApplication.translate('HelpDlg','WebSocket Command'),'send(<json>)',QApplication.translate('HelpDlg','If {} substitutions are used, json brackets need to be duplicated to escape them like in send({{ “value”: {}}})')])
    tbl_Commands.add_row(['&#160;','sleep(<float>)',QApplication.translate('HelpDlg','sleep: add a delay of <float> seconds')])
    tbl_Commands.add_row(['&#160;','button(<bool>)',QApplication.translate('HelpDlg','sets calling button to “pressed” if argument evaluates to 1 or True')])
    tbl_Commands.add_row(['&#160;','read(<json>)',QApplication.translate('HelpDlg','if the `<json>` text respects the JSON format it is send to the connected WebSocket server and the response is bound to the variable `_`')])
    strlist.append(tbl_Commands.get_html_string(attributes={'width':'100%','border':'1','padding':'1','border-collapse':'collapse'}))
    strlist.append('</body>')
    helpstr = ''.join(strlist)
    return re.sub(r'&amp;', r'&',helpstr)
