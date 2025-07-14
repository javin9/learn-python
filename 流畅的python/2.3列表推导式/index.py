from collections import abc

result = issubclass(tuple, abc.Sequence)
print(result)

symbols = '$¢£¥€¤'
codes = [ord(symbol) for symbol in symbols]
print(codes)

# >>> symbols = '$¢£¥€¤'
# >>> tuple(ord(symbol) for symbol in symbols)  ❶
# (36, 162, 163, 165, 8364, 164)
# >>> import array
# >>> array.array('I', (ord(symbol) for symbol in symbols))  ❷
# array('I', [36, 162, 163, 165, 8364, 164]

result = tuple(ord(symbol) for symbol in symbols)
print(result)

# >>> colors = ['black', 'white']
# >>> sizes = ['S', 'M', 'L']
# >>> for tshirt in (f'{c} {s}' for c in colors for s in sizes):  ❶
# ...     print(tshirt)
# ...
# black S
# black M
# black L
# white S
# white M
# white L

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in (f'{c} {s}' for c in colors for s in sizes):
    print(tshirt)

# >>> lax_coordinates = (33.9425, -118.408056)  ❶
# >>> city, year, pop, chg, area = ('Tokyo', 2003, 32_450, 0.66, 8014)  ❷
# >>> traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'),  ❸
# ...     ('ESP', 'XDA205856')]
# >>> for passport in sorted(traveler_ids):  ❹
# ...     print('%s/%s' % passport)   ❺
# ...
# BRA/CE342567
# ESP/XDA205856
# USA/31195855
# >>> for country, _ in traveler_ids:  ❻
# ...     print(country)
# ...
# USA
# BRA
# ESP
