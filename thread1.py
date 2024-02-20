import threading as td

def get_threadname():
    print(td.current_thread().name)
    
if __name__ == "__main__":
    t1 = td.Thread(target=get_threadname)
    t2 = td.Thread(target=get_threadname)
    
    t1.start()
    t2.start()
    
    t2.join()
    t1.join()