import time, threading
"""Very naive implementation of this exercise. The book so far hasn't mentioned
anything beyond this code. So this is why I opted to implement the problem in
this way."""

#global variable shared between class instances

shared_buffer = [0] * 10

class Sender:

    def __init__(self,name):
        self._name = name

    def send(self):
        global shared_buffer
        threading.Timer(2,self.send).start()
        if self.ready_to_send():
            shared_buffer = [1] * 10
            print("**********{0} is sending {1}".format(self._name,shared_buffer))
        else:
            print("**********{0} not ready to continue sending {1}".format(self._name,shared_buffer))

    def ready_to_send(self):
        """This function is not used directly because we periodically generate data"""
        global shared_buffer
        var = [k for k in shared_buffer if k != 0]
        result = True if len(var) == 0 else False
        print("sender.ready_to_send = {0},{1}".format(result,shared_buffer))
        return result

class Process:

    def __init__(self,sender,receiver):
        self._sender = sender
        self._receiver = receiver
        self._sender.send()

    def monitor_activity(self):
        print("monitoring process")
        while True:
            if self._receiver.ready_to_receive():
                self._receiver.receive()
            else:
                print("xxxxxxxxNot ready to receive")
            time.sleep(3)

class Receiver:

    def __init__(self,name):
        self._name = name

    def receive(self):
        global shared_buffer
        shared_buffer = [0] * 10
        print("**********{0} is receiving".format(self._name))

    def ready_to_receive(self):
        global shared_buffer
        var = [k for k in shared_buffer if k != 0]
        result = True if len(var) == len(shared_buffer) else False
        print("receiver.ready_to_receive = {0},{1}".format(result,shared_buffer))
        return result


if __name__ == '__main__':

    mySender = Sender("Alice")
    myReceiver = Receiver("Bob")

    monitor = Process(mySender,myReceiver)


    monitor.monitor_activity()

