import re
# patterns=['term1','term2']
# text="text for term1,not term 2"
#
# for pattern in patterns:
#     print("I'm searching for:",pattern)
#
#     if re.search(pattern,text):
#         print('match')
#     else:
#         print('no')
# print(re.findall('match','match in match for match'))
def multirefind(patterns,phrase):
    for pat in patterns:
        print('Searching ofr pattern {}'.format(pat))
        print(re.findall(pat,phrase))
        print("\n")
test_phrase = 'This is a string! But it has punctuation. How can we remove it?'

# test_patterns = [ 'sd*',     # s followed by zero or more d's
#                 # 'sd+',          # s followed by one or more d's
#                 'sd?'          # s followed by zero or one d's
#                 # 'sd{3}',        # s followed by three d's
#                 # 'sd{2,3}',      # s followed by two to three d's
#                 ]
test_patterns=['[^!.?]']
multirefind(test_patterns,test_phrase)
