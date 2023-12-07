f = open("test.in")
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]

index = 0
seeds = [int(a) for a in lines[index].split()[1:]]
intervals = [(seeds[2 * i], seeds[2 * i + 1]) for i in range(len(seeds) // 2)]
index += 3
dest = intervals

while index < len(lines):
	source = dest.copy()
	transformers = []
	while index < len(lines) and lines[index].strip() != '':
		line = lines[index]
		d, s, num = (int(a) for a in line.split())
		transformers.append( (d, s, num) )
		index += 1
	index += 2
	print("source: ", source)
	print("transformers: ", transformers)

	dest = []
	i = 0
	while i < len(source):
		for tr in transformers:
			d, s, num = tr
			e = s + num
			cur_source_start, cur_num = source[i]
			cur_source_end = cur_source_start + cur_num
			# todo: check intersection and split interval to dest and new smaller source intervals
			# if we split an interval, then we need to delete original from source list
			# if we don't split then keep it and then move to dest 

			if s >= cur_source_end:
				continue  # no intersection
			if cur_source_start >= e:
				continue  # no intersection

			if s <= cur_source_start < e:
				step = cur_source_start - s
				cur_dest_start = d + step
				if cur_source_end <= e:
					# fully convert cur_source to dest
					dest.append((cur_dest_start, cur_num))
					# remove cur_source, it was converted
					source.pop(i)
					i -= 1
					break
				else:
					num_converted = e - cur_source_start
					# add converted part
					dest.append((cur_dest_start, num_converted))
					# shorten non-converted part of cur_source
					source[i] = (e, cur_num - num_converted)
					i -= 1
					break
			else:
				assert cur_source_start < s
				if s < cur_source_end <= e:
					num_non_converted = s - cur_source_start
					# shorten non-converted part of cur_source
					source[i] = (cur_source_start, num_non_converted)
					# add converted part
					num_converted = cur_source_end - s
					dest.append((d, num_converted))
					i -= 1
					break
				else:
					num_non_converted = s - cur_source_start
					# shorten left non-converted part of cur_source
					source[i] = (cur_source_start, num_non_converted)
					# shorten right non-converted part of cur_source
					num_non_converted = cur_source_end - e
					source.insert(i + 1, (e, num_non_converted))
					# add converted part
					dest.append((d, num))  # whole 
					i -= 1
					break

		i += 1

	dest.extend(source)
	print("dest: ", dest)

print(min([a[0] for a in dest]))