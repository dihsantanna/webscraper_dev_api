import threading


def set_interval(func, sec):
    def func_wrapper():
        func()
        set_interval(func, sec)

    timer = threading.Timer(sec, func_wrapper)
    timer.start()
    return timer
