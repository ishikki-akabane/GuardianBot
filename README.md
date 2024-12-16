# GuardianBot
GuardianBot is a powerful, open-source Telegram bot that helps administrators maintain a secure and pleasant environment in their groups. Leveraging the Telehook library for efficient webhook-based operations, GuardianBot provides a range of moderation tools to combat spam, filter NSFW content, and monitor message edits.

# Features
- Spam Detection: Automatically identifies and removes spam messages using advanced algorithms.
- NSFW Content Filter: Detects and removes inappropriate images and text.
- Edit Monitoring: Tracks message edits to prevent malicious content changes.
- Custom Word Filters: Allows administrators to set up custom word blacklists.
- User Management: Provides tools for managing user permissions and bans.
- Logging: Keeps detailed logs of moderation actions for transparency.

# Requirements
- Python 3.6 or higher
- Telegram Bot API token

# Installation
### VPS/Terminal
- Clone the repository:
```bash
git clone https://github.com/ishikki-akabane/GuardianBot.git
cd GuardianBot
```
- Install the required dependencies:
```bash
pip install -r requirements.txt
```
- Set up your Telegram Bot API token:
  - Create a new bot via BotFather on Telegram
  - Copy the API token
  - Add inside the config.py:

- To run GuardianBot, execute the following command in your terminal:
```bash
python -m bot
```
- Make sure your webhook is properly set up as per Telehook's documentation.
# Configuration
Customize GuardianBot's behavior by modifying the config.py file. You can adjust spam detection thresholds, add custom word filters, and configure NSFW detection sensitivity.

# Contributing
We welcome contributions to GuardianBot! Please read our CONTRIBUTING.md file for guidelines on how to submit pull requests, report issues, and suggest improvements.
# License
GuardianBot is released under the MIT License. See the LICENSE file for more details.
# Support
For support, questions, or feature requests, please open an issue on the GitHub repository or join our Telegram support group at [link to support group].
# Acknowledgements
Thanks to ishikki-akabane for creating the Telehook library.
Special thanks to all contributors and the open-source community.
Protect your Telegram groups with GuardianBot - because a safe community is a thriving community!
