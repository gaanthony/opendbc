#!/usr/bin/env python3
import os

chrysler_to_ram = {
  "_stellantis_common_ram_dt_generated.dbc": {
    258: 35,
    264: 37,
    280: 181,
    284: 121,
    320: 131,
    344: 139,
    464: 464,
    500: 153,
    501: 232,
    544: 49,
    571: 177,
    559: 157,
    678: 250,
    720: 720,
    792: 792,
    820: 657,
  },
  "_stellantis_common_ram_hd_generated.dbc": {
    571: 570,
    678: 629,
  },
}

if __name__ == "__main__":
  src = '_stellantis_common.dbc'
  chrysler_path = os.path.dirname(os.path.realpath(__file__))

  for out, addr_lookup in chrysler_to_ram.items():
    with open(os.path.join(chrysler_path, src)) as in_f, open(os.path.join(chrysler_path, out), 'w') as out_f:
      out_f.write(f'CM_ "Generated from {src}"\n\n')

      wrote_addrs = set()
      for line in in_f.readlines():
        if line.startswith('BO_'):
          sl = line.split(' ')
          addr = int(sl[1])
          wrote_addrs.add(addr)

          sl[1] = str(addr_lookup.get(addr, addr))
          line = ' '.join(sl)
        out_f.write(line)

      missing_addrs = set(addr_lookup.keys()) - wrote_addrs
      assert len(missing_addrs) == 0, f"Missing addrs from {src}: {missing_addrs}"
