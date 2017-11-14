#!/usr/bin/env python2
import requests

import_ok = True
try:
    import weechat
except Exception:
    print "This script must be run under WeeChat."
    print "Get WeeChat now at: http://www.weechat.org/"
    import_ok = False

script_name = "pushover"
script_author = "marksu"
script_version = "1.0"
script_license = "GPL3"
script_desc = "Notifies of hilights and private messages via pushover.net"
script_options = {"user_key": "", "app_token": "", "blacklist": ""}


def msg_cb(data, bufferp, date, tagsn, isdisplayed, ishilight, prefix, message):
    isaway = weechat.buffer_get_string(bufferp, "localvar_away") != ""
    isprivate = weechat.buffer_get_string(bufferp, "localvar_type") == "private"
    isblacklisted = weechat.buffer_get_string(bufferp, "name").startswith(
        tuple(weechat.config_get_plugin("blacklist").split(",")))
    if isaway and (isprivate or int(ishilight)) and not isblacklisted:
        if int(ishilight) and not isprivate:
            title = (weechat.buffer_get_string(bufferp, "short_name") or
                     weechat.buffer_get_string(bufferp, "name"))
        else:
            title = prefix
        send_push(title, message)
    return weechat.WEECHAT_RC_OK


def send_push(title, message):
    user_key = weechat.config_get_plugin("user_key")
    app_token = weechat.config_get_plugin("app_token")
    if user_key != "" and app_token != "":
        payload = {
            "user": user_key,
            "token": app_token,
            "title": title,
            "message": message
        }
        r = requests.post(
            "https://api.pushover.net/1/messages.json", data=payload)


if __name__ == "__main__":
    if import_ok and weechat.register(script_name, script_author,
                                      script_version, script_license,
                                      script_desc, "", ""):
        for k, v in script_options.items():
            if weechat.config_get_plugin(k) == "":
                weechat.config_set_plugin(k, v)

        weechat.hook_print("", "notify_message", "", 1, "msg_cb", "")
        weechat.hook_print("", "notify_private", "", 1, "msg_cb", "")
