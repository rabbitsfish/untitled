from com.android.monkeyrunner import MonkeyRunner
from com.android.monkeyrunner import MonkeyDevice
import time
print("connect devices...")
device=MonkeyRunner.waitForConnection()
for i in range(50):
	device.startActivity(component="com.android.browser/.InnBrowserActivity")
	time.sleep(10)
	device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
	time.sleep(2)
