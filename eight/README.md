# Eigth

## Description
> I've heard that bit-a-bit cryptography is secure... so a byte-a-byte encryption is 8 times more secure!

*Author: [@Artio](https://github.com/AndreaArtioli)*
## Flag
`havceCTF{d0_n0t_x0r_w1th_kn0wn_pl41nt3xt}`

## Solution

The "flag format" is eight bytes long `havceCTF`, that means that we know the first eight bytes of what
is encoded, but the key is also eight bytes. This way we can entirely recover the key by xoring the first
eight bytes of ciphertext with `havceCTF`, then we can recover the rest of the flag.