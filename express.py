"""Happy."""

import this

mxdiflg=lambda a,b:(a>[]<b)-1or max(abs(len(u)-len(v))for u in a for v in b)

longest_consec=lambda a,k:0<k<=len(a)>0and max((''.join(a[i:i+k])for i in range(len(a))),key=len)or''

longest_consec=lambda a,k:k>0and max([''.join(a[i:i+k])for i in range(len(a)-k+1)]+[''],key=len)or''

capitalize=lambda s:[''.join(chr(ord(c)-i%2*32)for i,c in enumerate(s,n))for n in[1,0]]

