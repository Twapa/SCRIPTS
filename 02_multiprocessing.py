import multiprocessing

def do_some_work(data):
    print("Doing some work in another process")
    print("Data: {}".format(data))
    return

def main():
    d = 102
    t = multiprocessing.Process(target=do_some_work, args=(d,))
    t.start()
    t.join()

if __name__ == '__main__':
    main()