from time import sleep

def sleep_3s():
    sleep(3)
    print('wakeup')

print('start')
sleep_3s() # blocking
print('end')