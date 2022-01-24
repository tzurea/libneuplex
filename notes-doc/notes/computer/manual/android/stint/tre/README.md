{{c1:: adb devices }}   {{c2::   lists connected devices }} ~ 
{{c1:: adb root }}   {{c2::   restarts adbd with root permissions   }} ~
{{c1:: adb start-server }}   {{c2::   starts the adb server   }} ~
{{c1:: adb kill-server }}   {{c2::   kills the adb server   }} ~
{{c1:: adb reboot }}   {{c2::   reboots the device   }} ~
{{c1:: adb devices }}   {{c2::  -l  list of devices by product/model   }} ~
{{c1:: adb shell }}   {{c2::   starts the background terminal   }} ~
{{c1:: exit }}   {{c2::   exits the background terminal   }} ~
{{c1:: adb help }}   {{c2::   list all commands   }} ~



{{c1:: adb -s <deviceName> <command> }}   {{c2::   redirect command to specific device   }} ~
{{c1:: adb -d <command> }}   {{c2::   directs command to only attached USB device   }} ~
{{c1:: adb -e <command> }}   {{c2::   directs command to only attached emulator   }} ~
{{c1:: adb shell install <apk> }}   {{c2::   install app   }} ~
{{c1:: adb shell install <path> }}   {{c2::   install app from phone path   }} ~
{{c1:: adb shell install -r <path> }}   {{c2::    install app from phone path   }} ~
{{c1:: adb shell uninstall <name> }}   {{c2::  remove the app PATHS   }} ~
{{c1:: /data/data/<package>/databases }}   {{c2::    app databases   }} ~
{{c1:: /data/data/<package>/shared_prefs/ }}   {{c2::    shared preferences   }} ~
{{c1:: /data/app }}   {{c2::   apk installed by user   }} ~
{{c1:: /system/app }}   {{c2::   pre-installed APK files   }} ~
{{c1:: /mmt/asec }}   {{c2::   encrypted apps   }} ~
{{c1:: /mmt/emmc }}   {{c2::   internal SD Card   }} ~
{{c1:: /mmt/adcard }}   {{c2::    external/Internal SD Card   }} ~
{{c1:: /mmt/adcard/external_sd }}   {{c2::    external SD Card   }} ~
{{c1:: adb shell ls }}   {{c2::   list directory contents   }} ~
{{c1:: adb shell ls -s }}   {{c2::   print size of each file   }} ~
{{c1:: adb shell ls -R  }}   {{c2::   list subdirectories recursively   }} ~



{{c1:: adb push <local> <remote> }}   {{c2::   copy file/dir to device   }} ~
{{c1:: adb pull <remote> <local> }}   {{c2::   copy file/dir from device   }} ~
{{c1:: run-as <package> cat <file> }}   {{c2::   access the private package files   }} ~



{{c1:: adb get-stat–µ }}   {{c2::    print device state   }} ~
{{c1:: adb get-serialno }}   {{c2::    get the serial number   }} ~
{{c1:: adb shell dumpsys iphonesybinfo }}   {{c2::    get the IMEI   }} ~
{{c1:: adb shell netstat }}   {{c2::   list TCP connectivity   }} ~
{{c1:: adb shell pwd }}   {{c2::   print current working directory   }} ~
{{c1:: adb shell dumpsys battery }}   {{c2::    battery status   }} ~
{{c1:: adb shell pm  }}   {{c2::   list features list phone features   }} ~
{{c1:: adb shell service list }}   {{c2::    list all services   }} ~
{{c1:: adb shell dumpsys activity <package>/<activity> }}   {{c2::    activity info   }} ~
{{c1:: adb shell ps }}   {{c2::    print process status   }} ~
{{c1:: adb shell wm size }}   {{c2::    displays the current screen resolution   }} ~
{{c1:: dumpsys window windows | grep -E 'mCurrentFocus|mFocusedApp' }}   {{c2::   print current app's opened activity   }} ~





{{c1:: adb shell list packages }}   {{c2::    list package names   }} ~
{{c1:: adb shell list packages -r }}   {{c2::   list package name + path to apks   }} ~
{{c1:: adb shell list packages -3  }}   {{c2::  list third party package names   }} ~
{{c1:: adb shell list packages -s }}   {{c2::   list only system packages   }} ~
{{c1:: adb shell list packages -u }}   {{c2::   list package names + uninstalled   }} ~
{{c1:: adb shell dumpsys package packages }}   {{c2::   list info on all apps   }} ~
{{c1:: adb shell dump <name>  }}   {{c2::   list info on one package   }} ~
{{c1:: adb shell path <package> }}   {{c2::  path to the apk file   }} ~





{{c1:: adb shell dumpsys battery set level <n> }}   {{c2::   change the level from 0 to 100   }} ~
{{c1:: adb shell dumpsys battery set status<n> }}   {{c2::   change the level to unknown   }} ~
{{c1:: adb shell dumpsys battery reset }}   {{c2::    reset the battery   }} ~
{{c1:: adb shell dumpsys battery set usb <n> }}   {{c2::   change the status of USB connection. ON or OFF   }} ~
{{c1:: adb shell wm size WxH }}   {{c2::   sets the resolution to WxH   }} ~




{{c1:: adb reboot-recovery }}   {{c2::   reboot device into recovery mode   }} ~
{{c1:: adb reboot fastboot }}   {{c2::   reboot device into recovery mode   }} ~
{{c1:: adb shell screencap -p "/path/to/screenshot.png" }}   {{c2::   capture screenshot   }} ~
{{c1:: adb shell screenrecord  "/path/to/record.mp4" }}   {{c2::   record device screen   }} ~
{{c1:: adb backup -apk -all -f backup.ab }}   {{c2::   backup settings and apps   }} ~
{{c1:: adb backup -apk -shared -all -f backup.ab }}   {{c2::    backup settings   }} ~
{{c1:: adb backup -apk -nosystem -all -f backup.ab }}   {{c2::   backup only non-system apps   }} ~
{{c1:: adb restore backup.ab }}   {{c2::   restore a previous backup   }} ~

{{c1:: adb shell am start|startservice|broadcast <INTENT>[<COMPONENT>] -a <ACTION> e.g. android.intent.action.VIEW -c <CATEGORY> e.g. android.intent.category.LAUNCHER }}   {{c2::   start activity intent   }} ~
{{c1:: adb shell am start -a android.intent.action.VIEW -d URL }}   {{c2::    open URL   }} ~
{{c1:: adb shell am start -t image/* -a android.intent.action.VIEW }}   {{c2::    opens gallery   }} ~


{{c1:: adb logcat [options] [filter] [filter] }}   {{c2::    view device log   }} ~
{{c1:: adb bugreport }}   {{c2::    print bug reports   }} ~


{{c1:: adb shell permissions groups }}   {{c2::   list permission groups definitions   }} ~
{{c1:: adb shell list permissions -g }}   {{c2::  -r  list permissions details   }} ~


