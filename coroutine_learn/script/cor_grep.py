def grep(pattern): 
    print("Searching for %s" % pattern) 
    n = 1 
    while True: 
        print("RUNNING num is %d" % n) 
        line = (yield)      # 此时已经把yield变成一个协程了，它将不再包含任何初始值 
        print("have been seed value.") 
        if pattern in line: # 相反，要从外部传值给它，传值通过send()方法向它传值 
            print(line) 
        n += 1 

search = grep("coroutine") # coroutine是协程的英文单词        
next(search)      
search.send("a") 
search.send("coroutinedfsadf") 
search.send("coroutinedf woshi nihao ")    
search.close() # 通过调用close()方法来关闭一个协程          
search.send("adfad") # error
