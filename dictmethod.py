user_info={
    'name':'ankit',
    'age':20,
    'cast':'brahman',
    'religious':'hindu',
    'nation':'hindustan'
}

# user_info['intrest']=['always work']
# print(user_info)


# popped_item=user_info.pop('age')
# print(user_info)


# more_info={
#     'study':'b.tech',
#     'specilization':'cse'
# }
# user_info.update(more_info)
# print(user_info)


d={
    'name':'unknown',
    'age':'unknown'
}
d=dict.fromkeys(['name','age'],'unknown')
print(d)