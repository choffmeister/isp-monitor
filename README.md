# isp-monitor

A simple script to monitor your internet connection over time.

## Usage

~~~ bash
# start a monitoring process to regulary ping some well known public servers
$ ./isp-monitor monitor

# generate a plot
$ ./isp-monitor report
~~~

## Run as daemon

If you are using a recent version of Ubuntu (or any other distribution that supports upstart), then create a file `/etc/init/isp-monitor.conf` with the following content:

~~~
description "ISP Monitor Daemon Upstart Script"

start on startup
start on runlevel [2345]
stop on runlevel [016]

respawn

nice -5

exec start-stop-daemon --start --exec /path/to/isp-monitor/isp-monitor -- monitor
~~~

Now you can start/stop the daemon by executing `start isp-monitor` and `stop isp-monitor`.

## License

Licensed under the permissive [MIT License](http://opensource.org/licenses/MIT).
