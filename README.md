# Discord server insights

Get a list of all offline/online members in a discord server. Uses [Selenium](https://selenium-python.readthedocs.io/) to crawl invite links.

## Config

- Download [Chrome driver](https://chromedriver.chromium.org/downloads) according to your chrome version into the project directory.
- By default, the invites and output files are `invites.xlsx` and `output.xlsx` respectively, and can be modified by changing the `invites_file` and `output_file` variables.

## _Note_

- `invites.xlsx` must have only one column with the _invite links_, and **no** column name.
- If any invite link is invalid/expired, it will be reported in the console as well as in `output.xlsx`.