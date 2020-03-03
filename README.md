Simple tool to edit timesheets in STXNext Intranet
==================================================

### Setting it up

First, install the package:

```
git clone https://github.com/rr-/stx-intranetvi
cd stx-intranetvi
python3 -m pip install --user .
```

Then, provide your credentials by creating `intranetvi.ini` file in your
`$XDG_CONFIG_HOME` directory (usually `~/.config`) with the following values:

```ini
user-id=<your intranet user id>
session-id=<your intranet cookie>
```

You can get these values from your browser:

1. Navigate to https://intranet.stxnext.pl/
2. Open dev tools and the JS console
3. Type `Globals.user.id` and save the number under the `user-id` key
4. Type `document.cookie` and save the whole string under the `session-id` key

### Usage

Now you can use the tool like so:

```console
intranetvi
```

This will launch `$EDITOR` in interactive mode, where you can edit your
timesheet. It'll look like this:

```
# vim: syntax=config
# when adding a new work log, leave the id column empty.

# 2020-03-03 - total time: 1:15:00
# id    | duration | project_id | ticket | description
1376074 | 1:00:00  | 231        | 3007   | code review
1376073 | 0:15:00  | 231        | M1     | daily
```

For more options, make sure to check `--help`.
