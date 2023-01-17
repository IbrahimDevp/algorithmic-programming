S = input()

if S[0:int((len(S)-1)/2)] == S[int(((len(S)+3)/2))-1:]:
    print('Yes')
else:
    print('No')