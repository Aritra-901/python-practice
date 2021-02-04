st = "Gfg is best . Gfg also has Classes now. Classes help understand better . "
st_arr = st.split(' ')
replace_arr = ['It','They']
count = 0
for i in range(len(st_arr)):

    if(st_arr[i]=='Gfg'):
        count += 1
        if(count>1):
            st_arr[i] = replace_arr[0]

ct = 0
for i in range(len(st_arr)):

    if(st_arr[i]=='Classes'):
        ct += 1
        if(ct>1):
            st_arr[i] = replace_arr[1]

print(' '.join(st_arr))