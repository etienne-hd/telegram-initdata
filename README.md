# Telegram InitData

This project is a Python script that retrieves `InitData` from a Telegram bot's WebView using the Pyrogram library. The `InitData` is typically used to interact with Telegram's web applications.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Special Thanks](#special-thanks)

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.7 or later
- pip (Python package installer)

You will also need a valid Telegram API ID and API hash. You can obtain these by registering your application on [my.telegram.org](https://my.telegram.org).

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/etienne-hd/telegram-initdata
   cd telegram-initdata
   ```

2. Install the required packages:

   ```bash
   pip install pyrogram python-dotenv
   ```

3. Create a `.env` file in the project directory with the following content:

   ```plaintext
   api_id=YOUR_API_ID
   api_hash=YOUR_API_HASH
   phone_number=YOUR_PHONE_NUMBER
   ```

   Replace `YOUR_API_ID`, `YOUR_API_HASH`, and `YOUR_PHONE_NUMBER` with your actual credentials.

## Usage

Run the script using Python:

```bash
python initdata.py
```

## How It Works

1. **Load Environment Variables**: The script starts by loading the API credentials from a `.env` file using the `dotenv` library.

2. **Initialize the Client**: A new `Client` instance is created using the provided credentials. This instance will allow you to interact with the Telegram API.

3. **Resolve Peer**: The bot's username is resolved to obtain the corresponding peer information.

4. **Request WebView**: The script invokes a `RequestWebView` method to load the specified URL associated with the bot. This simulates opening a web application in a WebView.

5. **Extract InitData**: The URL returned by the WebView is parsed to extract the `tgWebAppData` parameter, which contains the `InitData`. This data is then URL-decoded for further use.

6. **Output**: Finally, the extracted `InitData` is printed to the console.

## Special Thanks

The original code was taken from [@shamhi](https://github.com/shamhi), I modified and simplified it.