class User:
    def __init__(self, name, engagement):
        self.name = name
        self.engagement_metrics = engagement
        
    def __repr__(self):
        return f"<User: {self.name}>"
    
def email_engaged_users(user):
    try:
        perform_calculation(user.engagement_metrics)
    except KeyError:
        print("Incorrect values provided to our calculation function.")
        #raise #to bubble up the error
    else: #this will only run if the try block does not raise an error
        send_engagement_notification(user.name)
        
def perform_calculation(metrics):
    return metrics['clicks'] * 5 + metrics['hits'] * 2

def send_engagement_notification(user):
    print(f"Notification sent to {user}.")
    
my_user = User("John Doe", {'clicks': 61, 'hits': 100})
email_engaged_users(my_user)