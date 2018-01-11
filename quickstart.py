from instapy import InstaPy

session = InstaPy(username='abheeshtstark', password='qwerty098', nogui=True)

session.login()
session.set_upper_follower_count(limit = 250)
session.set_lower_follower_count(limit = 10)
session.like_by_tags(['#marvel','#runaways','#avengers','#thor','iamfrankie','spacex','space'], amount=500)

session.set_user_interact(amount=5, random=True, percentage=50, media='Photo')


session.set_do_comment(enabled=True, percentage=25)
session.set_comments(['Awesome', 'Really Cool', 'I like your stuff'])
# you can also set comments for specific media types (Photo / Video)
session.set_comments(['Nice shot!'], media='Photo')
session.set_comments(['Great Video!'], media='Video')
# session.follow_by_list(['selenagomez', 'katyperry'], times=1)

session.end()
