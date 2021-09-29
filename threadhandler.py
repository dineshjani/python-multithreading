from customthread import CustomThread as Thread
class ThreadHandler():
    __default_instance__ = None

    def __init__(self):
        self.__threadDict = {}

    def register_thread(self,action,name,*arguments):
        if name in self.__threadDict:
            raise Exception(f"thread with name {name} already exists")
        else:
            if arguments==None:                     
                t1=Thread(target=action)
            else:
                t1=Thread(target=action,args=(arguments),name=name)
            self.__threadDict[name]=t1

    def stop_thread(self,name):

        if name not in self.__threadDict:
            raise Exception(f"thread with name {name} not exists")
        else:
            self.__threadDict[name].stop()
            del (self.__threadDict[name])


    def start_thread(self,name):

        if name not in self.__threadDict:
            raise Exception(f"thread with name {name} not registered")
        else:
            self.__threadDict[name].start()

    def join_thread(self,name):
        if name not in self.__threadDict:
            raise Exception(f"thread with name {name} not registered")
        else:
            self.__threadDict[name].join()
        
        

    @staticmethod
    def get_default_instance():
        """
        Function to get default instance of the thraedHandler class
        """
        if ThreadHandler.__default_instance__ is None:
            instance = ThreadHandler()
            ThreadHandler.__default_instance__ = instance
        return ThreadHandler.__default_instance__            



thread_handler = ThreadHandler.get_default_instance()

"""
thread_handler.register_thread(target=venue,name="venue_thread",args=(venues))
thread_handler.register_thread(wedding_card,"weddding_thread")
thread_handler.register_thread(card_distribution,"card_thread")
thread_handler.start_thread("venue_thread")
thread_handler.start_thread("weddding_thread")
thread_handler.start_thread("card_thread")

"""