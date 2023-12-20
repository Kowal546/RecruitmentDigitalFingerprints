def hash_snowflake(snowflake):
    min_index = min(range(len(snowflake)), key=lambda i: snowflake[i:] + snowflake[:i])
    normalized_snowflake = snowflake[min_index:] + snowflake[:min_index]
    return tuple(normalized_snowflake)


def find_identical_snowflakes(input_vectors):
    snowflake_dict = {}

    for i, snowflake in enumerate(input_vectors):
        normalized_snowflake = hash_snowflake(snowflake)
        normalized_snowflake_reverse = hash_snowflake(snowflake[::-1])
        if normalized_snowflake in snowflake_dict:
            snowflake_dict[normalized_snowflake].append(i)
        elif normalized_snowflake_reverse in snowflake_dict:
            snowflake_dict[normalized_snowflake_reverse].append(i)
        else:
            snowflake_dict[normalized_snowflake] = [i]

    result_dict = {str(snowflake): indices for snowflake, indices in snowflake_dict.items() if len(indices) > 1}
    return result_dict


vectors = [
    [3, 10, 9, 6, 4, 8], [4, 7, 8, 5, 6, 10], [4, 3, 2, 10, 2, 10],
    [8, 6, 7, 2, 8, 2], [5, 1, 8, 9, 4, 1], [9, 3, 5, 10, 2, 3],
    [2, 7, 4, 8, 9, 4], [3, 4, 7, 1, 3, 4], [6, 9, 10, 3, 8, 4],
    [4, 1, 3, 4, 8, 4], [1, 3, 3, 2, 7, 2], [8, 9, 4, 1, 5, 1], [1, 1, 1, 2, 3, 4], [3, 4, 1, 1, 1, 2],
    [1, 2, 3, 4, 5, 6], [2, 3, 4, 5, 6, 1]
]

output = find_identical_snowflakes(vectors)
print(output)
