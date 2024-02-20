import threading

def range_print():
    for i in range(30,51):
        print(threading.current_thread().name,'->',i)
        # time.sleep(0.5)

t1 = threading.Thread(target=range_print)
t2 = threading.Thread(target=range_print)

t1.start()
t2.start()

t1.join()
t2.join()