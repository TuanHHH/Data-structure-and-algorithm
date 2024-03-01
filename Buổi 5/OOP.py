class StarCookie:
    def __init__(self,color,weight) -> None:
        self.color = color
        self.weight = weight

star_cookie1 = StarCookie("Red",16)
print(star_cookie1.color)
print(star_cookie1.weight)

class Youtube:
    def __init__(self,username,subscribers=0,subscriptions = 0) -> None:
        self.username = username
        self.subscribers = subscribers
        self.subscriptions = subscriptions

    def subscribe(self,user):
        user.subscribers += 1
        self.subscriptions += 1

user1 = Youtube("Elshad")
print(user1.username)
print(user1.subscribers)

user2 = Youtube("Renad")
user2.subscribers = 5
print(user2.username)
print(user2.subscribers)

user1.subscribe(user2)
user2.subscribe(user1)
print(f'User 1 subscribers: {user1.subscribers}')
print(f'User 1 subscriptions: {user1.subscriptions}')
print(f'User 2 subscribers: {user2.subscribers}')
print(f'User 2 subscriptions: {user2.subscriptions}')
