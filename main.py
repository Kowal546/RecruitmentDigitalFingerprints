import numpy as np


def hash_snowflake(snowflake: list) -> tuple:
    min_index = min(range(len(snowflake)), key=lambda i: snowflake[i:] + snowflake[:i])
    normalized_snowflake = snowflake[min_index:] + snowflake[:min_index]
    return tuple(normalized_snowflake)


def find_identical_snowflakes(input_vectors: list[list]) -> dict:
    snowflake_dict = {}

    for i, snowflake in enumerate(input_vectors):
        normalized_snowflake = hash_snowflake(snowflake)
        if normalized_snowflake in snowflake_dict:
            snowflake_dict[normalized_snowflake].append(i)
        else:
            normalized_snowflake_reverse = hash_snowflake(snowflake[::-1])
            if normalized_snowflake_reverse in snowflake_dict:
                snowflake_dict[normalized_snowflake_reverse].append(i)
            else:
                snowflake_dict[normalized_snowflake] = [i]

    result_dict = {str(snowflake): indices for snowflake, indices in snowflake_dict.items() if len(indices) > 1}
    return result_dict


vectors = np.loadtxt('vectors.txt', delimiter=',', dtype=int).tolist()

output = find_identical_snowflakes(vectors)
print(output)
