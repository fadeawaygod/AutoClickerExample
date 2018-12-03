import win32api, win32con
import time
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def clean_trash():
	click(1800, 200)
	time.sleep(0.5)
	click(1500,630)
	time.sleep(1)
	click(1100,550)
	time.sleep(0.5)

def delete_files(n):
	click(750,280)
	for i in range(n):
		time.sleep(0.2)
		click(750,200)
#win32api.SetCursorPos((750,20))
for epoch in range(500):
	delete_files(100)
	clean_trash()


