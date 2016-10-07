import threading
import time
import Queue
import sys
import traceback

"""
To run single_lift.py
python single_lift.py - on one terminal
then
tail -f /tmp/lift - on other terminal to see lift status
"""



class Lift(object):

    UP = 'up'
    DOWN = 'down'

    def __init__(self, max_load=10, speed=2, floors=10, output='/tmp/lift'):
        self.max_load = max_load
        self.speed = speed
        self.floors = floors
        self.requests = {i: False for i in range(1, self.floors+1)}
        self.any_requests = False
        self.output = output
        self.current_floor = self.floors
        self.dirc = None

    def move(self):
        self.current_floor = self.current_floor + self.dirc
        self.log('Current floor: ' + str(self.current_floor))

    def request(self, floor):
        if floor >= 1 and floor <= self.floors:
            self.requests[floor] = int(time.time())
            self.update_requests()
            self.log("Requested floor {}".format(floor))
        else:
            self.log("Cant request !!")

    def next_stop(self):
        sorted_reqs = sorted(self.requests.items(), key = lambda x: x[1], reverse=True)
        sorted_reqs = [x for x in sorted_reqs if x[1]]

        if any(self.requests.values()):
            dest_floor, time = sorted_reqs.pop()

            if dest_floor > self.current_floor:
                self.dirc = 1
            else:
                self.dirc = -1
        else:
            self.dirc = 0

    def is_requested(self):
        if self.requests[self.current_floor]:
            self.requests[self.current_floor] = False
            self.log("Stopped at {}".format(self.current_floor))

    def update_requests(self):
        self.any_requests = any(self.requests.values())

    def run(self):
        self.next_stop()
        self.move()
        self.is_requested()

    def log(self, mess):
        with open(self.output, 'a') as out:
            out.writelines(str(mess) + '\n')


def get_messages(q):
    messages = []

    while q.qsize():
        messages.append(q.get())

    return messages


def consume_lift_messages(lift, messages):
    for mes in messages:
        if mes == 'q':
            raise Exception("Shutting down Lift")

        lift.request(int(mes))


def print_st():
    exc_type, exc_value, exc_traceback = sys.exc_info();
    traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)
    traceback.print_exception(exc_type, exc_value, exc_traceback, limit=2, file=sys.stdout)


def worker(q):
    lift = Lift()
    try:
        lift.log('Lift Bootup')
        while True:
            messages = get_messages(q)
            consume_lift_messages(lift, messages)
            lift.run()

            time.sleep((lift.speed/2) or 1)

            if lift.dirc != 0:
                lift.log(".")

            time.sleep((lift.speed/2) or 1)
    except Exception as e:
        print str(e)
        print_st()
        lift.log(str(e))


def start():
    q = Queue.Queue()
    t = threading.Thread(target=worker, args=(q,))
    t.start()

    dirc = {
        'd': Lift.DOWN,
        'u': Lift.UP
    }

    try:
        while True:
            req = raw_input('Enter floor-direction eg 1\n')
            q.put(req)

            time.sleep(1)
    except Exception as e:
        q.put('q')
        print e
    except KeyboardInterrupt:
        q.put('q')
        pass


if __name__ == '__main__':
    start()


