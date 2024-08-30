# IG Follower Stats

## Description

This program uses `instaloader` to get statistics from Instagram profiles.
Requires login information and can only access public profiles or profiles followed by the logged in profile.

## Usage

Requires `instaloader` to be installed via `pip install instaloader`.
Most likely you will have to run via a virtual environment in your terminal.
The commands are below:

```bash
cd igfollowerstats
python3 -m venv path/to/venv
source path/to/venv/bin/activate
python3 -m pip install instaloader
python main.py
```

Be careful not to login too many times successively as Instagram may rate limit access.

## Features

1. Retrieve followers and following count from any profile that the logged in account can access.
2. Print list of followers who do not follow a profile back.

## To-do

- [ ] Save followers and following to a local txt file
- [ ] Ghost followers function

## Tags

- Language: Python
- Uses: [instaloader](https://instaloader.github.io/)