<div align="center">

# ⚡ Discord Emoji Uploader

### Bulk upload Discord application emojis in seconds.

A lightweight Python utility that uploads local PNG, JPG, JPEG and GIF files to your Discord application, handles naming automatically, skips duplicates, and generates ready-to-use emoji references.

<br>

<a href="https://guns.lol/meduu">
<img src="https://img.shields.io/badge/Developer-Medu-7C3AED?style=for-the-badge&logo=discord&logoColor=white">
</a>
<a href="https://github.com/meduuv/discord-emoji-uploader">
<img src="https://img.shields.io/badge/GitHub-Repository-18181B?style=for-the-badge&logo=github&logoColor=white">
</a>

<br><br>

<img src="https://img.shields.io/badge/Python-3.9%2B-3776AB?style=flat-square&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/Discord-API%20v10-5865F2?style=flat-square&logo=discord&logoColor=white">
<img src="https://img.shields.io/badge/License-MIT-22C55E?style=flat-square">
<img src="https://img.shields.io/badge/Status-Active-10B981?style=flat-square">

</div>

---

## ✦ What is this?

Uploading custom emojis individually through Discord gets annoying when you're working with a large collection.

**Discord Emoji Uploader** turns the process into a simple workflow:

```text
📁 Put emojis in a folder
        ↓
⚡ Run one command
        ↓
🤖 Discord API
        ↓
📋 Get ready-to-use emoji IDs
```

No manually uploading every image.

No manually copying every emoji ID.

---

# 🚀 Features

<table>
<tr>
<td width="50%">

### ⚡ Bulk Upload

Upload an entire folder of emoji files automatically.

</td>

<td width="50%">

### 🧹 Automatic Naming

Messy filenames are converted into Discord-compatible emoji names.

</td>
</tr>

<tr>
<td>

### ♻️ Duplicate Detection

Existing emoji names are detected and skipped.

</td>

<td>

### 🖼️ Multiple Formats

Supports PNG, JPG, JPEG and GIF files.

</td>
</tr>

<tr>
<td>

### 🔐 Environment Variables

Keep your Discord bot token outside the source code.

</td>

<td>

### 📋 Automatic Output

Generates ready-to-paste `<:name:id>` references.

</td>
</tr>
</table>

---

# 🧠 Why use it?

Suppose you have:

```text
emojis/
├── apeiron.png
├── warning.png
├── success.png
├── economy_coin.png
├── staff.gif
├── server_logo.png
└── cool_reaction.png
```

Normally, you'd have to upload these manually.

With this tool:

```bash
python uploader.py
```

That's it.

The script checks your existing application emojis, uploads only what's missing, and prints the resulting emoji references.

---

# 📦 Installation

## 1. Clone the repository

```bash
git clone https://github.com/meduuv/discord-emoji-uploader.git
cd discord-emoji-uploader
```

## 2. Install dependencies

```bash
pip install requests python-dotenv
```

## 3. Create the emoji folder

Create:

```text
emojis/
```

Your project should look like:

```text
discord-emoji-uploader/
│
├── emojis/
│   ├── apeiron.png
│   ├── warning.png
│   ├── success.png
│   └── staff.gif
│
├── uploader.py
├── .env
├── .gitignore
└── README.md
```

---

# 🔑 Configuration

Create a `.env` file in the project directory:

```env
DISCORD_TOKEN=YOUR_BOT_TOKEN
```

The script also supports:

```env
BOT_TOKEN=YOUR_BOT_TOKEN
```

### Keep your token private

Add this to `.gitignore`:

```text
.env
```

> [!CAUTION]
> Never commit your Discord bot token to GitHub.
>
> If your token is exposed, reset it immediately through the Discord Developer Portal.

---

# ▶️ Usage

Put your emoji files inside:

```text
emojis/
```

Then run:

```bash
python uploader.py
```

### Example output

```text
uploaded: apeiron -> 142938475629384756
uploaded: warning -> 142938475629384757
skip: staff
uploaded: economy_coin -> 142938475629384758

EMOJIS = {
    "apeiron": "<:apeiron:142938475629384756>",
    "economy_coin": "<:economy_coin:142938475629384758>",
    "staff": "<:staff:142938475629384759>",
}
```

Copy the generated `EMOJIS` dictionary into your Discord bot.

---

# 🧹 Automatic filename cleanup

You don't need to manually rename your files.

For example:

```text
Cool Reaction.png
        ↓
Cool_Reaction
```

```text
server!!!logo.png
        ↓
server_logo
```

```text
economy coin.png
        ↓
economy_coin
```

The uploader removes unsupported characters, cleans repeated underscores and keeps names within Discord's naming limits.

---

# ♻️ Duplicate protection

Already-uploaded emojis are automatically skipped.

```text
uploaded: apeiron
uploaded: warning
skip: apeiron
skip: warning
uploaded: new_emoji
```

You can safely run the uploader again after adding new files.

---

# 📋 Using the generated emojis

The tool generates:

```python
EMOJIS = {
    "apeiron": "<:apeiron:123456789>",
    "warning": "<:warning:123456789>",
}
```

You can then use them in your bot:

```python
await ctx.send(f"{EMOJIS['apeiron']} Welcome!")
```

Or:

```python
await ctx.send(EMOJIS["warning"])
```

---

# 🖼️ Supported formats

|  Format | Support |
| :-----: | :-----: |
|  `.png` |    🟢   |
|  `.jpg` |    🟢   |
| `.jpeg` |    🟢   |
|  `.gif` |    🟢   |
| `.webp` |    🔴   |

---

# 🔄 How the uploader works

```text
             ┌──────────────────┐
             │      emojis/      │
             │                  │
             │  PNG JPG GIF ... │
             └────────┬─────────┘
                      │
                      ▼
             ┌──────────────────┐
             │  Discord Emoji   │
             │     Uploader     │
             └────────┬─────────┘
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
       Clean       Check        Encode
       names      existing      image
          │           │           │
          └───────────┼───────────┘
                      ▼
                Discord API
                      │
                      ▼
             ┌──────────────────┐
             │ Uploaded Emojis  │
             └────────┬─────────┘
                      │
                      ▼
                EMOJIS = {...}
```

---

# 📁 Project structure

```text
discord-emoji-uploader/
│
├── 📁 emojis/          Your emoji images
│
├── 🐍 uploader.py      Main uploader
│
├── 🔐 .env             Discord token
│
├── 🚫 .gitignore       Files Git should ignore
│
└── 📖 README.md        Documentation
```

---

# 🛠️ Requirements

| Requirement         | Version  |
| ------------------- | -------- |
| Python              | 3.9+     |
| Discord API         | v10      |
| requests            | Latest   |
| python-dotenv       | Latest   |
| Discord Application | Required |

Install the Python dependencies with:

```bash
pip install requests python-dotenv
```

---

# ❓ FAQ

<details>
<summary><b>Does this upload emojis to a Discord server?</b></summary>

No.

The tool uploads emojis to your **Discord application** using the Discord API.

</details>

<details>
<summary><b>Can I run it multiple times?</b></summary>

Yes.

Existing emoji names are detected and skipped.

</details>

<details>
<summary><b>Does it modify my original images?</b></summary>

No.

The files are read and encoded for the API request. Your original files remain untouched.

</details>

<details>
<summary><b>Where do I get my Discord bot token?</b></summary>

From the Bot section of your application in the Discord Developer Portal.

</details>

<details>
<summary><b>Why did an emoji fail to upload?</b></summary>

Discord may reject an upload because of authentication problems, application limits, invalid image data, invalid names or API restrictions.

The script prints the HTTP status code when an upload fails.

</details>

---

# 🔒 Security

This project requires a Discord bot token because the Discord API needs authentication.

The recommended setup is:

```text
.env
```

with:

```env
DISCORD_TOKEN=YOUR_BOT_TOKEN
```

and:

```text
.env
```

inside `.gitignore`.

**Never share your token publicly.**

---

# 🎯 Use cases

Discord Emoji Uploader is useful for:

* 🤖 Discord bot developers
* 🏠 Community owners
* 🎨 Custom bot branding
* 🔄 Bot migrations
* 📦 Large emoji collections
* 🧩 Bot UI systems
* ⚙️ Development workflows
* 🛠️ Discord application management

---

# 🧪 Example workflow

```text
1. Create your Discord application
              ↓
2. Get your bot token
              ↓
3. Add token to .env
              ↓
4. Put images inside emojis/
              ↓
5. Run uploader.py
              ↓
6. Existing emojis are detected
              ↓
7. New emojis are uploaded
              ↓
8. Copy generated EMOJIS dictionary
              ↓
9. Use them in your bot
```

---

<div align="center">

# Made by Medu

### POWERFUL · SECURE · LIMITLESS · RELIABLE

<br>

<a href="https://guns.lol/meduu">
<img src="https://img.shields.io/badge/Visit%20guns.lol%2Fmeduu-7C3AED?style=for-the-badge&logo=firefox&logoColor=white">
</a>

<br><br>

<sub>Python • Discord API v10 • Developer Utility</sub>

<br><br>

⭐ If this project helped you, consider starring the repository.

</div>
