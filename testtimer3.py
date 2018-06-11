from statsd import StatsClient

statsd = StatsClient()

foo_timer = statsd.timer('foo')
foo_timer.start()
# Do something fun.
foo_timer.stop()
