from instapy import InstaPy
from instapy import smart_run
from threading import Thread
import os


print('app started')
def func1():
    session = InstaPy(username=os.environ['USERNAME'], password=os.environ['PASSWORD'], headless_browser=False)

    with smart_run(session):
        """ Activity flow """		
        # general settings		
        session.set_dont_include(["friend1", "friend2", "friend3"])		

        # activity		
        session.like_by_tags(["natgeo"], amount=10)

        # Joining Engagement Pods

        session.join_pods(topic='sports', engagement_mode='no_comments')
        session.set_do_like(enabled=True, percentage=70)
        session.set_do_comment(enabled=True, percentage=35)
        session.set_comments(['Awesome', 'Really Cool', 'I like your stuff'])
    print('Success')
func1()
#Thread(target = func1).start()
#Thread(target = func1).start()