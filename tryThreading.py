# import threading

# def printThread( id ):
#     print( "print thread: {id}".format( id = id ) )
#     return

# threads = []
# for i in range(5):
#     t = threading.Thread( target=printThread, args=(i,) )
#     threads.append( t )
#     t.start()


################################################


# import logging
# import threading
# import time

# def worker(arg):
#     while not arg['stop']:
#         logging.debug('Hi from myfunc')
#         time.sleep(0.5)

# def main():
#     logging.basicConfig(level=logging.DEBUG, format='%(relativeCreated)6d %(threadName)s %(message)s')
#     info = {'stop': False}
#     thread = threading.Thread(target=worker, args=(info,))
#     thread.start()
#     while True:
#         try:
#             logging.debug('Hello from main')
#             time.sleep(0.75)
#         except KeyboardInterrupt:
#             info['stop'] = True
#             break
#     thread.join()

# if __name__ == '__main__':
#     main()



################################################

# import threading
# import time
# import logging

# logging.basicConfig(level=logging.DEBUG,
#                     format='(%(threadName)-10s) %(message)s',
#                     )

# def daemon():
#     logging.debug('Starting')
#     time.sleep(3)
#     logging.debug('Exiting')

# d = threading.Thread(name='daemon', target=daemon)
# d.setDaemon(True)

# def non_daemon():
#     logging.debug('Starting')
#     logging.debug('Exiting')

# t = threading.Thread(name='non-daemon', target=non_daemon)

# d.start()
# t.start()

# d.join(3)
# print(d.isAlive())
# t.join()

##################################

# import random
# import threading
# import time
# import logging

# logging.basicConfig(level=logging.DEBUG,
#                     format='(%(threadName)-10s) %(message)s',
#                     )

# def worker():
#     """thread worker function"""
#     t = threading.currentThread()
#     pause = random.randint(1,5)
#     logging.debug('sleeping %s', pause)
#     time.sleep(pause)
#     logging.debug('ending')
#     return

# for i in range(3):
#     t = threading.Thread(target=worker)
#     t.setDaemon(True)
#     t.start()

# main_thread = threading.currentThread()
# for t in threading.enumerate():
#     if t is main_thread:
#         continue
#     logging.debug('joining %s', t.getName())
#     t.join()

################################################


import threading
import logging

logging.basicConfig(level=logging.DEBUG,
					format='(%(threadName)-10s) %(message)s)')

class MyThread(threading.Thread):

	def run(self):
		logging.debug('running')
		return

for i in range(5):
	t = MyThread()
	t.start()