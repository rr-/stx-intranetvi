Simple tool to edit timesheets in STXNext Intranet
--------------------------------------------------

### Usage

Create `intranetvi.ini` file in your `$XDG_CONFIG_HOME` dir
(usually `~/.config`) and provide following values there:

```ini
user-id=<your intranet user id>
session-id=<your intranet cookie>
```

You can get these values from your browser:

1. Navigate to https://intranet.stxnext.pl/
2. Open dev tools and the JS console
3. Type `Globals.user.id` and save the number under the `user-id` key
4. Type `document.cookie` and save the whole string under the `session-id` key

Now you can use use tool like so:

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
