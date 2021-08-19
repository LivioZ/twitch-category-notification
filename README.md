# Twitch streamer category changed notification (Linux)
I've found myself in the situation where a streamer is online but I only want to watch him when he switches to the next game/category.

So I made this script that checks the category every 5 minutes and, if it has been changed, sends a notification directly to my desktop.

## Usage
Create a file named `data.json` with the following content:
```
{
  "client_id": "your_client_id",
  "client_secret": "your_client_secret",
  "grant_type": "client_credentials"
}
```
Follow the [Twitch guide](https://dev.twitch.tv/docs/api/) to get `client_id` and `client_secret` and paste them in the file.

Open the script with your preferred editor and change the `TWITCH_NAME` variable to the streamer's username.

### Notes
The localization is italian. Change it if you wish.