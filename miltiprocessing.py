import multiprocessing 
import time
def square(x,y):
    time.sleep(y)
    print('Square : ',x**2)
def cube(x,y):
    time.sleep(y)
    print('Cube:',x**3)
    
if __name__=="main_":   
    print(f"started at {time.strftime('%X')}")
    p1=multiprocessing.Process(target=square,args=(3,5))
    p2=multiprocessing.Process(target=cube,args=(2,10))

    p1.start()
    p2.start()
    p1.join() 
    p2.join()
    print(f"Finish at {time.strftime('%X')}")