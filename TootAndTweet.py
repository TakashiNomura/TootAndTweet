import datetime, twython
c_key  = "Consumer Key (API Key)"
cs_key = "Consumer Secret (API Secret)"
a_key  = "Access Token"
as_key = "Access Token Secret"

def tweet(s):
    api = twython.Twython(c_key, cs_key, a_key, as_key)
    api.update_status(status=s)


from mastodon import Mastodon
def toot(s):
    mastodon = Mastodon(
                        client_id="app_key.txt",
                        access_token="user_key.txt",
                        api_base_url = "https://mstdn.jp")
    mastodon.toot(s)

def toot_and_tweet(s):
    tweet(s)
    toot(s)


if __name__ == '__main__':
    import fire
    fire.Fire(toot_and_tweet)
