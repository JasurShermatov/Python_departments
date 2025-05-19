from abc import ABC, abstractmethod
from typing import List, Dict, Any
from datetime import datetime
import uuid


class LibraryResource(ABC):
    def __init__(self, resource_id: str, title: str, author: str):
        self.resource_id = resource_id
        self.title = title
        self.author = author
        self.checkout_status = False
        self.checkout_date = None
        self.return_date = None

    def checkout(self):
        self.checkout_status = True
        self.checkout_date = datetime.now()
        return self.checkout_status

    def return_resource(self):
        self.checkout_status = False
        self.return_date = datetime.now()
        return self.checkout_status

    @abstractmethod
    def get_type(self) -> str:
        pass

    def to_dict(self) -> Dict:
        return {
            "resource_id": self.resource_id,
            "title": self.title,
            "author": self.author,
            "type": self.get_type(),
            "checkout_status": self.checkout_status,
            "checkout_date": self.checkout_date,
            "return_date": self.return_date,
        }


class Book(LibraryResource):
    def __init__(
        self, resource_id: str, title: str, author: str, isbn: str, pages: int
    ):
        super().__init__(resource_id, title, author)
        self.isbn = isbn
        self.pages = pages

    def get_type(self) -> str:
        return "book"

    def to_dict(self) -> Dict:
        data = super().to_dict()
        data.update({"isbn": self.isbn, "pages": self.pages})
        return data


class Journal(LibraryResource):
    def __init__(
        self, resource_id: str, title: str, author: str, volume: int, issue: int
    ):
        super().__init__(resource_id, title, author)
        self.volume = volume
        self.issue = issue

    def get_type(self) -> str:
        return "journal"

    def to_dict(self) -> Dict:
        data = super().to_dict()
        data.update({"volume": self.volume, "issue": self.issue})
        return data


class DigitalMedia(LibraryResource):
    def __init__(
        self,
        resource_id: str,
        title: str,
        author: str,
        format_type: str,
        size_mb: float,
    ):
        super().__init__(resource_id, title, author)
        self.format_type = format_type
        self.size_mb = size_mb

    def get_type(self) -> str:
        return "digital_media"

    def to_dict(self) -> Dict:
        data = super().to_dict()
        data.update({"format_type": self.format_type, "size_mb": self.size_mb})
        return data


class ResourceFactory:
    @staticmethod
    def create_resource(resource_type: str, data: Dict) -> LibraryResource:
        resource_id = data.get("resource_id", str(uuid.uuid4()))
        title = data.get("title", "")
        author = data.get("author", "")

        if resource_type == "book":
            isbn = data.get("isbn", "")
            pages = data.get("pages", 0)
            return Book(resource_id, title, author, isbn, pages)

        elif resource_type == "journal":
            volume = data.get("volume", 0)
            issue = data.get("issue", 0)
            return Journal(resource_id, title, author, volume, issue)

        elif resource_type == "digital_media":
            format_type = data.get("format_type", "")
            size_mb = data.get("size_mb", 0.0)
            return DigitalMedia(resource_id, title, author, format_type, size_mb)

        else:
            raise ValueError(f"Unknown resource type: {resource_type}")


class NotificationChannel(ABC):
    @abstractmethod
    def send(self, recipient: str, subject: str, message: str) -> bool:
        pass


class EmailNotification(NotificationChannel):
    def send(self, recipient: str, subject: str, message: str) -> bool:
        return True


class SMSNotification(NotificationChannel):
    def send(self, recipient: str, subject: str, message: str) -> bool:
        return True


class PushNotification(NotificationChannel):
    def send(self, recipient: str, subject: str, message: str) -> bool:
        return True


class NotificationManager(ABC):
    @abstractmethod
    def notify(self, recipient: str, subject: str, message: str) -> bool:
        pass


class ResourceNotificationManager(NotificationManager):
    def __init__(self, notification_channel: NotificationChannel):
        self.notification_channel = notification_channel
        self.notification_history = []

    def notify(self, recipient: str, subject: str, message: str) -> bool:
        result = self.notification_channel.send(recipient, subject, message)

        if result:
            self.notification_history.append(
                {
                    "timestamp": datetime.now(),
                    "recipient": recipient,
                    "subject": subject,
                    "message": message,
                    "status": "sent",
                }
            )
        else:
            self.notification_history.append(
                {
                    "timestamp": datetime.now(),
                    "recipient": recipient,
                    "subject": subject,
                    "message": message,
                    "status": "failed",
                }
            )

        return result

    def get_notification_history(self) -> List[Dict]:
        return self.notification_history


class LibrarySystem:
    def __init__(self):
        self.resources = {}
        self.resource_factory = ResourceFactory()

        self.email_notification = EmailNotification()
        self.sms_notification = SMSNotification()
        self.push_notification = PushNotification()

        self.notification_manager = ResourceNotificationManager(self.email_notification)

    def add_resource(self, resource_type: str, data: Dict) -> LibraryResource:
        resource = self.resource_factory.create_resource(resource_type, data)
        self.resources[resource.resource_id] = resource
        return resource

    def get_resource(self, resource_id: str) -> LibraryResource:
        return self.resources.get(resource_id)

    def get_all_resources(self) -> List[LibraryResource]:
        return list(self.resources.values())

    def checkout_resource(self, resource_id: str, user_email: str) -> bool:
        resource = self.get_resource(resource_id)
        if not resource:
            return False

        if resource.checkout_status:
            return False

        resource.checkout()

        subject = f"Library Resource Checkout: {resource.title}"
        message = f"You have checked out '{resource.title}' by {resource.author}."
        self.notification_manager.notify(user_email, subject, message)

        return True

    def return_resource(self, resource_id: str, user_email: str) -> bool:
        resource = self.get_resource(resource_id)
        if not resource:
            return False

        if not resource.checkout_status:
            return False

        resource.return_resource()

        subject = f"Library Resource Return: {resource.title}"
        message = f"You have returned '{resource.title}' by {resource.author}."
        self.notification_manager.notify(user_email, subject, message)

        return True

    def set_notification_channel(self, channel_type: str):
        if channel_type == "email":
            self.notification_manager = ResourceNotificationManager(
                self.email_notification
            )
        elif channel_type == "sms":
            self.notification_manager = ResourceNotificationManager(
                self.sms_notification
            )
        elif channel_type == "push":
            self.notification_manager = ResourceNotificationManager(
                self.push_notification
            )
        else:
            raise ValueError(f"Unknown notification channel: {channel_type}")

    def get_notification_history(self) -> List[Dict]:
        return self.notification_manager.get_notification_history()


from fastapi import FastAPI, HTTPException

app = FastAPI(title="Library Management System API")
library_system = LibrarySystem()


@app.post("/resources")  # Bridge Pattern Implementation
def create_resource(resource_type: str, data: Dict[str, Any]):
    try:
        resource = library_system.add_resource(resource_type, data)
        return resource.to_dict()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/resources/{resource_id}")
def get_resource(resource_id: str):
    resource = library_system.get_resource(resource_id)
    if not resource:
        raise HTTPException(status_code=404, detail="Resource not found")
    return resource.to_dict()


@app.get("/resources")
def get_all_resources():
    resources = library_system.get_all_resources()
    return [r.to_dict() for r in resources]


@app.post("/notifications")
def send_notification(
    recipient: str, subject: str, message: str, channel: str = "email"
):
    try:
        library_system.set_notification_channel(channel)
        result = library_system.notification_manager.notify(recipient, subject, message)
        return {"success": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/notifications/history")
def get_notification_history():
    return library_system.get_notification_history()


@app.post("/resources/{resource_id}/checkout")
def checkout_resource(resource_id: str, user_email: str):
    result = library_system.checkout_resource(resource_id, user_email)
    if not result:
        raise HTTPException(status_code=400, detail="Unable to checkout resource")
    return {"success": True}


@app.post("/resources/{resource_id}/return")
def return_resource(resource_id: str, user_email: str):
    result = library_system.return_resource(resource_id, user_email)
    if not result:
        raise HTTPException(status_code=400, detail="Unable to return resource")
    return {"success": True}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
