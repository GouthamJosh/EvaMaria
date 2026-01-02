class script(object):

    START_TXT = """👋 Hello {},
My name is <a href=https://t.me/{}>{}</a>.

🎬 I can help you find and access movies easily!
➕ Just add me to your group and enjoy the experience 😍
"""

    HELP_TXT = """👋 Hey {},
Here’s a quick guide to all my available commands and features.
Use the buttons below to explore more 👇
"""

    ABOUT_TXT = """✨ <b>About Me</b>

✯ <b>Name:</b> {}
✯ <b>Creator:</b> <a href=https://t.me/TeamEvamaria>Team Eva Maria</a>
✯ <b>Library:</b> Pyrogram
✯ <b>Language:</b> Python 3
✯ <b>Database:</b> MongoDB
✯ <b>Server:</b> Heroku
✯ <b>Build Status:</b> v1.0.1 [BETA]
"""

    SOURCE_TXT = """<b>📌 NOTE:</b>
• Eva Maria is an open-source project.
• Source Code: https://github.com/EvamariaTG/EvaMaria

<b>👨‍💻 Developers:</b>
• <a href=https://t.me/TeamEvamaria>Team Eva Maria</a>
"""

    MANUELFILTER_TXT = """<b>📂 Filters Help</b>

Filters allow admins to set automated replies for specific keywords.
Whenever a keyword is detected, Eva Maria will respond automatically.

<b>⚠️ Notes:</b>
1. Eva Maria must have admin privileges.
2. Only admins can add filters.
3. Alert buttons are limited to 64 characters.

<b>🛠 Commands:</b>
• /filter – <code>Add a filter</code>
• /filters – <code>List all filters</code>
• /del – <code>Delete a specific filter</code>
• /delall – <code>Delete all filters (Owner only)</code>
"""

    BUTTON_TXT = """<b>🔘 Buttons Help</b>

Eva Maria supports both URL buttons and alert buttons.

<b>⚠️ Notes:</b>
1. Buttons cannot be sent without content.
2. All Telegram media types are supported.
3. Buttons must follow correct Markdown format.

<b>🌐 URL Button:</b>
<code>[Button Text](buttonurl:https://t.me/EvaMariaBot)</code>

<b>🚨 Alert Button:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>
"""

    AUTOFILTER_TXT = """<b>🤖 Auto Filter Help</b>

<b>⚠️ Notes:</b>
1. Make me admin if your channel is private.
2. Do not add camrips, adult, or fake files.
3. Forward the latest message from your channel with quotes.

I will automatically index all files into my database.
"""

    CONNECTION_TXT = """<b>🔗 Connections Help</b>

Connections link your group with PM for easier filter management
and help reduce group spam.

<b>⚠️ Notes:</b>
1. Only admins can create connections.
2. Send <code>/connect</code> in the group.

<b>🛠 Commands:</b>
• /connect – <code>Connect a chat to PM</code>
• /disconnect – <code>Disconnect from a chat</code>
• /connections – <code>List all connected chats</code>
"""

    EXTRAMOD_TXT = """<b>➕ Extra Modules</b>

Additional useful features available in Eva Maria.

<b>🛠 Commands:</b>
• /id – <code>Get user ID</code>
• /info – <code>Get user information</code>
• /imdb – <code>Fetch movie details from IMDb</code>
• /search – <code>Search movie info from multiple sources</code>
"""

    ADMIN_TXT = """<b>🛡 Admin Commands</b>

⚠️ These commands are restricted to bot admins only.

<b>🛠 Commands:</b>
• /logs – <code>View recent errors</code>
• /stats – <code>Database statistics</code>
• /delete – <code>Delete a file from DB</code>
• /users – <code>List all users</code>
• /chats – <code>List all chats</code>
• /leave – <code>Leave a chat</code>
• /disable – <code>Disable a chat</code>
• /ban – <code>Ban a user</code>
• /unban – <code>Unban a user</code>
• /channel – <code>List connected channels</code>
• /broadcast – <code>Send message to all users</code>
"""

    STATUS_TXT = """📊 <b>Bot Statistics</b>

★ Total Files: <code>{}</code>
★ Total Users: <code>{}</code>
★ Total Chats: <code>{}</code>
★ Used Storage: <code>{}</code> MiB
★ Free Storage: <code>{}</code> MiB
"""

    LOG_TEXT_G = """#NewGroupAdded
🏷 Group: {} (<code>{}</code>)
👥 Members: <code>{}</code>
➕ Added By: {}
"""

    LOG_TEXT_P = """#NewUserStarted
🆔 ID: <code>{}</code>
👤 Name: {}
"""
