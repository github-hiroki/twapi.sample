# Copyright 2019- Hiroki.H

def main():
    from config import Config as cfg
    import twitter
    auth = twitter.OAuth(
        cfg().access_token,
        cfg().access_token_secret,
        cfg().consumer_key,
        cfg().consumer_secret_key,
    )
    tw = twitter.Twitter(auth=auth)
    for timeline in tw.statuses.home_timeline():
        tl = "({id}) [{username}]:{text}".format(
            id=timeline["id"],
            username=timeline["user"]["name"],
            text=timeline["text"],
        )
        print(tl)
        pass
    pass

if __name__ == "__main__":
    main()
    pass
