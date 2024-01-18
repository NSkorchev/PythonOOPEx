from abc import ABC, abstractmethod


class IContent(ABC):
    def __init__(self, text):
        self.text = text

    @abstractmethod
    def format(self):
        ...


class MyML(IContent):

    def format(self):
        return '\n'.join(['<myML>', self.text, '</myML>'])


class IEmail(ABC):

    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class Email(IEmail):

    def __init__(self, protocol):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender):  # fix
        self.__sender = sender.format()

    def set_receiver(self, receiver):  # fix
        self.__receiver = receiver.format()

    def set_content(self, content: IContent):
        self.__content = content.format()

    def __repr__(self):
        return f"Sender: {self.__sender}\nReceiver: {self.__receiver}\nContent:\n{self.__content}"


myml = MyML('Hello there!')
email = Email('IM')
email.set_sender('qmal')
email.set_receiver('james')
email.set_content(myml)
print(email)
