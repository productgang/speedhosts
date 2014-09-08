# Speedhosts

When you're using MAMP Pro you'll notice that Google Chrome will sometimes take while "resolving host". This is due to MAMP Pro creating a single line for each entry, and you'll end up with something like this in your `/etc/hosts`:

```
127.0.0.1       localhost       # MAMP PRO - Do NOT remove this entry!
127.0.0.1       api.tracklist   # MAMP PRO - Do NOT remove this entry!
127.0.0.1       br.local        # MAMP PRO - Do NOT remove this entry!
```

The [solution](https://coderwall.com/p/fmjbrq) is to put them all into a single line like so:

`127.0.0.1 localhost api.tracklist br.local`

Since MAMP Pro recreates all the lines on every modification of your virtual hosts, I have created this Python script that rearranges your `/etc/hosts` entries.


## Usage

`sudo python speedhosts.py`

(Just in case, speedhosts creates a backup of your hosts file in `/etc/hosts.bak`)