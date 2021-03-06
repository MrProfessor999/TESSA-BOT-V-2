__help__ = """

｢ Anti-Spam Settings 」*
             /antispam <on/off/yes/no>: Change antispam security settings in the group, or return your current settings(when no arguments)."
            This helps protect you and your groups by removing spam flooders as quickly as possible._"
             /setflood <int/'no'/'off'>: enables or disables flood control"
             /setfloodmode <ban/kick/mute/tban/tmute> <value>: Action to perform when user have exceeded flood limit. ban/kick/mute/tmute/tban
            Antiflood allows you to take action on users that send more than x messages in a row. Exceeding the set flood will result in restricting that user._
             /addblacklist <triggers>: Add a trigger to the blacklist. Each line is considered one trigger, so using different lines will allow you to add multiple triggers.
             /blacklistmode <off/del/warn/ban/kick/mute/tban/tmute>: Action to perform when someone sends blacklisted words.
            Blacklists are used to stop certain triggers from being said in a group. Any time the trigger is mentioned, the message will immediately be deleted. A good combo is sometimes to pair this up with warn filters!
             /reports <on/off>: Change report setting, or view current status.
            • If done in pm, toggles your status.
            • If in chat, toggles that chat's status.
            If someone in your group thinks someone needs reporting, they now have an easy way to call all admins._
             /lock <type>: Lock items of a certain type (not available in private)
             /locktypes: Lists all possible locktypes
            The locks module allows you to lock away some common items in the telegram world; the bot will automatically delete them!
             /addwarn <keyword> <reply message>: Sets a warning filter on a certain keyword. If you want your keyword to be a sentence, encompass it with quotes, as such: /addwarn "very angry" This is an angry user.
             /warn <userhandle>: Warns a user. After 3 warns, the user will be banned from the group. Can also be used as a reply.
             /strongwarn <on/yes/off/no>: If set to on, exceeding the warn limit will result in a ban. Else, will just kick.
            If you're looking for a way to automatically warn users when they say certain things, use the /addwarn command.
             /welcomemute <off/soft/strong>: All users that join, get muted"
            A button gets added to the welcome message for them to unmute themselves. This proves they aren't a bot! soft - restricts users ability to post media for 24 hours. strong - mutes on join until they prove they're not bots.*"""

__mod_name__ = "Anti-Spam🤐"            
