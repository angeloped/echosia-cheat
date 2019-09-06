: '

This script will wrap cheat program in Tor.
Execute this when you have Tor installed.
And for anonymity as well as bypassing request limits.

'

for ((;;)) do
	{ # try
		for ((;;)) do torify python cheat.py; done
	} || { # catch
		for ((;;)) do proxychains python cheat.py; done
	}
done
