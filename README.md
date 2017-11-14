# weechat-pushover

Notifies of hilights and private messages using pushover.net.

## Installtion

Install dependencies and put script in `$HOME/.weechat/python/`

```bash
$ pip install -r requirements
$ cp pushover.py $HOME/.weechat/python
```

To load the script when weechat starts

```bash
$ ln -s $HOME/.weechat/python/pushover.py $HOME/.weechat/python/autoload 
```

## Options

The options `user_key` and `app_token` need to be set for the script to work.

* `user_key` – Pushover user key, can be found in the top right when logged in
  on pushover.net
* `app_token` – Pushover Application/API token
* `blacklist` – Comma-separated list of server/buffers to ignore. Will partially
  match full buffer name from the beginning. `freenode` will match
  `freenode.weechat` and `freenode.chat`, for example.
