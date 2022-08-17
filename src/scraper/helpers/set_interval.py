import threading


def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()

    timer = threading.Timer(sec, func_wrapper)
    timer.start()
    return timer
