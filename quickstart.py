from instapy import InstaPy

insta_username = 'abheeshtstark'
insta_password = 'qwerty098'

# set headless_browser=True if you want to run InstaPy on a server
try:
    session = InstaPy(username=insta_username,
                      password=insta_password,
                      nogui=True)
    session.login()

    # settings

session.set_upper_follower_count(limit = 250)
session.set_lower_follower_count(limit = 10)
session.like_by_tags(['#marvel','#runaways','#avengers','#thor','iamfrankie','spacex','space'], amount=500)

session.set_user_interact(amount=5, random=True, percentage=50, media='Photo')


session.set_do_comment(enabled=True, percentage=25)
session.set_comments(['Awesome', 'Really Cool', 'I like your stuff'])
# you can also set comments for specific media types (Photo / Video)
session.set_comments(['Nice shot!'], media='Photo')
session.set_comments(['Great Video!'], media='Video'

    # actions
 

finally:
    # end the bot session
    session.end()
