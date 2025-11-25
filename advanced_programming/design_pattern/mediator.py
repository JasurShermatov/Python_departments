from abc import ABC, abstractmethod


class IMediator(ABC):
    @abstractmethod
    def add_user(self, user: "IUser"):
        pass

    @abstractmethod
    def send_message(self, message: str, sender: "IUser"):
        pass


class ChatRoom(IMediator):
    def __init__(self):
        self.user = []

    def add_user(self, user: "IUser"):
        self.user.append(user)

    def send_message(self, message: str, sender: "IUser"):
        for user in self.user:
            if sender is not user:
                user.receive(message, sender)


class IUser(ABC):
    def __init__(self, mediator: "IMediator", name: str):
        self.mediator = mediator
        self.name = name

    @abstractmethod
    def send(self, message: str):
        pass

    @abstractmethod
    def receive(self, message: str, sender: "IUser"):
        pass


class ChatUser(IUser):
    def send(self, message: str):
        self.mediator.send_message(message=message, sender=self)

    def receive(self, message: str, sender: "IUser"):
        print(f"Send {message} to {self.name} from {sender.name}")


if __name__ == "__main__":
    chat_room = ChatRoom()

    alice = ChatUser(chat_room, "Alice")
    bob = ChatUser(chat_room, "Bob")
    kyle = ChatUser(chat_room, "Kyle")

    chat_room.add_user(alice)
    chat_room.add_user(bob)
    chat_room.add_user(kyle)

    alice.send(f"Hello!")
    bob.send(f"Hello!")