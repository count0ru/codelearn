dec_number = input().strip()
bin_number = "{0:2b}".format(int(dec_number))

max_ones_count, ones_count = 0,0
for chr in bin_number:
    if chr is '1':
        ones_count += 1
    else:
        if max_ones_count < ones_count:
            max_ones_count = ones_count
        ones_count = 0

if max_ones_count > ones_count:
    print(max_ones_count)
else:
    print(ones_count)

