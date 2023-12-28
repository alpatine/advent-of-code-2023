def split_data_into_blocks(raw_data):
    blocks = [[]]
    current_block = blocks[0]

    for line in raw_data.splitlines():
        if line != '':
            current_block.append(line)
        else: 
            current_block = []
            blocks.append(current_block)

    return blocks
